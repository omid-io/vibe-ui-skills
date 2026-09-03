#!/usr/bin/env python3
"""
test_search.py — Unit and Regression Tests for Search & Recommendation Engine.
"""

import sys
import json
import time
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

def run_tests():
    print("[INFO] Running Unit & Performance Tests for Search & Recommendation Engine...")
    director = DesignDirector()
    engine = RecommendationEngine()

    failures = []

    # Test 1: Persian Beauty Clinic
    t0 = time.perf_counter()
    intent1 = director.infer_intent("کلینیک پوست و مو و زیبایی")
    dec1 = engine.recommend(intent1)
    ms1 = (time.perf_counter() - t0) * 1000

    if intent1["product_domain"] != "beauty_clinical_wellness":
        failures.append(f"Test 1 Failed: Expected beauty_clinical_wellness, got {intent1['product_domain']}")
    if dec1["selected_style"] != "quiet_luxury":
        failures.append(f"Test 1 Failed: Expected quiet_luxury, got {dec1['selected_style']}")
    if ms1 > 25.0:
        failures.append(f"Test 1 Failed: Performance threshold exceeded ({ms1:.2f}ms > 25ms)")
    print(f"  [PASS] Test 1: Persian Beauty Clinic -> quiet_luxury ({ms1:.2f}ms)")

    # Test 2: Crypto Exchange Dashboard
    t0 = time.perf_counter()
    intent2 = director.infer_intent("crypto exchange trading orderbook dashboard")
    dec2 = engine.recommend(intent2)
    ms2 = (time.perf_counter() - t0) * 1000

    if intent2["product_domain"] != "crypto_trading_web3":
        failures.append(f"Test 2 Failed: Expected crypto_trading_web3, got {intent2['product_domain']}")
    if intent2["product_mode"] != "operate":
        failures.append(f"Test 2 Failed: Expected operate mode, got {intent2['product_mode']}")
    if dec2["selected_style"] not in ["linear_dark", "data_dense_terminal"]:
        failures.append(f"Test 2 Failed: Expected linear_dark or data_dense_terminal, got {dec2['selected_style']}")
    print(f"  [PASS] Test 2: Crypto Exchange Dashboard -> {dec2['selected_style']} ({ms2:.2f}ms)")

    # Test 3: Conflict Resolution (Neobrutalism on Banking)
    intent3 = director.infer_intent("سامانه بانک و وام بانکی")
    dec3 = engine.recommend(intent3, user_style_preference="neobrutalism")
    resolutions = dec3["decision_trace"].get("conflict_resolutions", [])
    if not resolutions:
        failures.append("Test 3 Failed: Conflict resolution was not recorded for neobrutalism in fintech_banking")
    else:
        print(f"  [PASS] Test 3: Conflict Resolution recorded: {resolutions[0]['resolved_outcome']}")

    # Test 4: Low-confidence VoI Candidate Directions
    intent4 = director.infer_intent("xyz random undefined query")
    if intent4["confidence"]["overall"] >= 0.8:
        failures.append(f"Test 4 Failed: Expected low confidence for random query, got {intent4['confidence']['overall']}")
    if not intent4.get("candidate_directions"):
        failures.append("Test 4 Failed: Expected 3 candidate directions under ambiguity")
    print(f"  [PASS] Test 4: Low-confidence VoI emitted {len(intent4.get('candidate_directions', []))} candidate directions")

    if failures:
        print("\n[FAIL] Test Failures:", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1

    print("\n[SUCCESS] All Search & Recommendation unit tests passed.")
    return 0

if __name__ == "__main__":
    sys.exit(run_tests())
