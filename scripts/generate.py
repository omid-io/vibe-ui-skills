#!/usr/bin/env python3
"""
generate.py — Autonomous Vibe UI Interface Generator (CLI)
Takes a prompt, infers intent, decides architecture, and generates an accessible HTML artifact.
"""

import sys
import argparse
from pathlib import Path

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
from vibe_core.generator import InterfaceGenerator

def main():
    parser = argparse.ArgumentParser(description="Vibe UI Interface Generator")
    parser.add_argument("prompt", help="Natural language prompt")
    parser.add_argument("-o", "--output", help="Output file path (.html)")
    parser.add_argument("-s", "--style", help="Style override")
    parser.add_argument("-m", "--mode", choices=["persuade", "operate", "read", "experience"])

    args = parser.parse_args()

    director = DesignDirector()
    engine = RecommendationEngine()
    generator = InterfaceGenerator()

    overrides = {}
    if args.mode:
        overrides["product_mode"] = args.mode

    print(f"[INFO] Analyzing prompt: '{args.prompt}'...")
    intent = director.infer_intent(args.prompt, overrides)
    decision = engine.recommend(intent, user_style_preference=args.style)

    print(f"  [OK] Matched domain: {intent['product_domain']} (Confidence: {intent['confidence']['overall']})")
    print(f"  [OK] Selected style: {decision['selected_style']} (Score: {decision['composite_score']})")

    html = generator.generate_html(decision, prompt_title=args.prompt)

    out_path = Path(args.output).resolve() if args.output else (ROOT_DIR / "examples" / "generated_preview.html").resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\n[SUCCESS] Generated interface written to {out_path.relative_to(ROOT_DIR)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
