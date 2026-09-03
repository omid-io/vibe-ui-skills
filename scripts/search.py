#!/usr/bin/env python3
"""
search.py — Vibe UI Zero-Token Fast Retrieval Engine (CLI)
Queries local Knowledge Base (<15ms) and emits structured Design Brief.
"""

import sys
import json
import time
import argparse
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from vibe_core.director import DesignDirector
from vibe_core.recommendation import RecommendationEngine

def main():
    parser = argparse.ArgumentParser(description="Vibe UI Design Intelligence Search CLI")
    parser.add_argument("query", nargs="?", default="", help="Natural language query or keywords (Persian/English)")
    parser.add_argument("-q", "--query_flag", dest="query_flag", help="Alternative query flag")
    parser.add_argument("-m", "--mode", choices=["persuade", "operate", "read", "experience"], help="Override product mode")
    parser.add_argument("-s", "--style", help="Explicit style override (Expert Mode)")
    parser.add_argument("--json", action="store_true", default=True, help="Emit output in clean JSON format")
    parser.add_argument("--pretty", action="store_true", help="Format JSON with indentation")

    args = parser.parse_args()
    raw_query = args.query or args.query_flag or "general modern saas"

    start_time = time.perf_counter()

    # 1. Intent Extraction
    director = DesignDirector()
    overrides = {}
    if args.mode:
        overrides["product_mode"] = args.mode
    intent = director.infer_intent(raw_query, overrides)

    # 2. Recommendation & Conflict Resolution
    engine = RecommendationEngine()
    decision = engine.recommend(intent, user_style_preference=args.style)

    elapsed_ms = (time.perf_counter() - start_time) * 1000.0

    # 3. Formulate Compact Design Brief
    genome = decision.get("genome", {})
    trace = decision.get("decision_trace", {})

    brief = {
        "status": "SUCCESS",
        "query": raw_query,
        "elapsed_ms": round(elapsed_ms, 2),
        "detected_domain": intent["product_domain"],
        "confidence": intent["confidence"]["overall"],
        "ambiguity": intent["ambiguity_status"],
        "product_mode": intent["product_mode"],
        "recommended_style": decision["selected_style"],
        "composite_score": decision["composite_score"],
        "typography": {
            "display": genome.get("typography", {}).get("display_family"),
            "body": genome.get("typography", {}).get("body_family"),
            "persian": genome.get("typography", {}).get("persian_family")
        },
        "palette": {
            "canvas": genome.get("color", {}).get("canvas"),
            "surface": genome.get("color", {}).get("surface"),
            "accent": genome.get("color", {}).get("accent"),
            "border": genome.get("color", {}).get("border"),
            "text": genome.get("color", {}).get("text")
        },
        "hard_constraints": intent["hard_constraints"],
        "decision_rationale": trace.get("rationale", []),
        "conflicts_resolved": trace.get("conflict_resolutions", [])
    }

    if args.pretty:
        print(json.dumps(brief, indent=2, ensure_ascii=False))
    else:
        print(json.dumps(brief, ensure_ascii=False))

    return 0

if __name__ == "__main__":
    sys.exit(main())
