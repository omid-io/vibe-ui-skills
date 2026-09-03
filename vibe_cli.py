#!/usr/bin/env python3
"""
vibe_cli.py — Vibe UI V3 Master Unified CLI & Orchestrator
Production-grade interface connecting Design Director, Recommendation, Genome, Critic, Refiner & Verifier.
"""

import sys
import json
import argparse
from pathlib import Path

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR))

from vibe_core.director import DesignDirector
from vibe_core.recommendation import RecommendationEngine
from vibe_core.generator import InterfaceGenerator
from vibe_core.critic import DesignCritic
from vibe_core.refiner import AutoRefiner
from vibe_core.verifier import VerificationEngine

def cmd_search(args):
    director = DesignDirector()
    engine = RecommendationEngine()
    intent = director.infer_intent(args.query)
    decision = engine.recommend(intent, user_style_preference=args.style)
    brief = {
        "query": args.query,
        "domain": intent["product_domain"],
        "confidence": intent["confidence"]["overall"],
        "style": decision["selected_style"],
        "score": decision["composite_score"],
        "typography": decision["genome"]["typography"],
        "color": decision["genome"]["color"]
    }
    print(json.dumps(brief, indent=2, ensure_ascii=False))

def cmd_plan(args):
    director = DesignDirector()
    engine = RecommendationEngine()
    intent = director.infer_intent(args.query)
    decision = engine.recommend(intent, user_style_preference=args.style)
    print(json.dumps(decision, indent=2, ensure_ascii=False))

def cmd_generate(args):
    director = DesignDirector()
    engine = RecommendationEngine()
    generator = InterfaceGenerator()
    critic = DesignCritic()
    refiner = AutoRefiner()
    verifier = VerificationEngine()

    print(f"[1/5] Extracting Intent & Directing: '{args.query}'...")
    intent = director.infer_intent(args.query)
    print(f"      Domain: {intent['product_domain']} (Confidence: {intent['confidence']['overall']})")

    print("[2/5] Synthesizing Decision & Genome...")
    decision = engine.recommend(intent, user_style_preference=args.style)
    print(f"      Style: {decision['selected_style']} (Score: {decision['composite_score']})")

    print("[3/5] Generating Initial Interface Artifact...")
    html = generator.generate_html(decision, prompt_title=args.query)

    print("[4/5] Evaluating with Independent Design Critic...")
    critique = critic.critique(html, decision, iteration=1)
    print(f"      Critic Score: {critique['quality_score']}/100 (Status: {critique['acceptance_status']})")

    if critique["acceptance_status"] != "ACCEPTED":
        print("[4.5] Applying Priority Auto-Refinement...")
        html, critique = refiner.refine(html, decision, max_iterations=2)
        print(f"      Refined Score: {critique['quality_score']}/100 (Status: {critique['acceptance_status']})")

    print("[5/5] Executing Physical Verification Proof (Verification 2.0)...")
    verification = verifier.verify_html(html, args.output or "output.html")
    print(f"      Verification: {verification['overall_status']} ({verification['checks_summary']['passed']}/{verification['checks_summary']['total']} checks passed)")

    out_path = Path(args.output).resolve() if args.output else (ROOT_DIR / "examples" / "generated_output.html").resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\n[SUCCESS] Completed autonomous pipeline. Artifact saved to: {out_path.relative_to(ROOT_DIR)}")

def cmd_critique(args):
    path = Path(args.file)
    if not path.exists():
        print(f"[FAIL] File not found: {args.file}", file=sys.stderr)
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    critic = DesignCritic()
    report = critic.critique(content)
    print(json.dumps(report, indent=2, ensure_ascii=False))

def cmd_verify(args):
    path = Path(args.file)
    if not path.exists():
        print(f"[FAIL] File not found: {args.file}", file=sys.stderr)
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    verifier = VerificationEngine()
    report = verifier.verify_html(content, path.name)
    print(json.dumps(report, indent=2, ensure_ascii=False))

def main():
    parser = argparse.ArgumentParser(description="Vibe UI Master CLI")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # search
    p_search = subparsers.add_parser("search", help="Search Knowledge Base (<10ms)")
    p_search.add_argument("query", help="Prompt or query")
    p_search.add_argument("-s", "--style", help="Style override")

    # plan
    p_plan = subparsers.add_parser("plan", help="Synthesize DesignDecisionContract")
    p_plan.add_argument("query", help="Prompt or query")
    p_plan.add_argument("-s", "--style", help="Style override")

    # generate
    p_gen = subparsers.add_parser("generate", help="Run full autonomous generation pipeline")
    p_gen.add_argument("query", help="Prompt or query")
    p_gen.add_argument("-o", "--output", help="Output HTML file path")
    p_gen.add_argument("-s", "--style", help="Style override")

    # critique
    p_crit = subparsers.add_parser("critique", help="Run independent Design Critic on HTML file")
    p_crit.add_argument("file", help="Path to HTML file")

    # verify
    p_ver = subparsers.add_parser("verify", help="Run Verification 2.0 evidence checks on HTML file")
    p_ver.add_argument("file", help="Path to HTML file")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "search":
        cmd_search(args)
    elif args.command == "plan":
        cmd_plan(args)
    elif args.command == "generate":
        cmd_generate(args)
    elif args.command == "critique":
        cmd_critique(args)
    elif args.command == "verify":
        cmd_verify(args)

if __name__ == "__main__":
    main()
