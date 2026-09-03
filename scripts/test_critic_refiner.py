#!/usr/bin/env python3
"""
test_critic_refiner.py — Unit and Regression Tests for Critic & AutoRefiner.
"""

import sys
from pathlib import Path

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from vibe_core.critic import DesignCritic
from vibe_core.refiner import AutoRefiner

def main():
    print("[INFO] Running Unit Tests for Design Critic & AutoRefiner...")
    critic = DesignCritic()
    refiner = AutoRefiner()
    failures = []

    # Test 1: Clean HTML produces ACCEPTED
    clean_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    button:focus-visible { outline: 2px solid blue; }
  </style>
</head>
<body>
  <h1>Clean Page</h1>
  <button type="button">Action</button>
  <div class="skeleton animate-pulse">Loading...</div>
  <div class="empty">No records</div>
  <div class="error">Retry connection</div>
</body>
</html>"""
    report1 = critic.critique(clean_html)
    if not report1["hard_gates_pass"]:
        failures.append("Test 1 Failed: Clean HTML should pass all hard gates")
    if report1["acceptance_status"] != "ACCEPTED":
        failures.append(f"Test 1 Failed: Expected ACCEPTED, got {report1['acceptance_status']}")
    print(f"  [PASS] Test 1: Clean HTML passed with Score {report1['quality_score']}/100")

    # Test 2: Defective HTML (Raw emoji + Missing Viewport)
    defective_html = """<!DOCTYPE html>
<html>
<head>
  <!-- missing viewport -->
</head>
<body>
  <div>Click me 🔥</div>
</body>
</html>"""
    report2 = critic.critique(defective_html)
    if report2["hard_gates_pass"]:
        failures.append("Test 2 Failed: Defective HTML must fail hard gates")
    if report2["acceptance_status"] != "REJECTED_CRITICAL":
        failures.append(f"Test 2 Failed: Expected REJECTED_CRITICAL, got {report2['acceptance_status']}")
    print(f"  [PASS] Test 2: Defective HTML correctly caught {len(report2['hard_gate_failures'])} hard gate failures")

    # Test 3: Auto-Refinement Loop
    refined_html, refined_report = refiner.refine(defective_html, {}, max_iterations=2)
    if not refined_report["hard_gates_pass"]:
        failures.append("Test 3 Failed: AutoRefiner should resolve hard gate blockers")
    if 'name="viewport"' not in refined_html:
        failures.append("Test 3 Failed: Viewport meta was not injected by refiner")
    if "🔥" in refined_html:
        failures.append("Test 3 Failed: Raw emoji was not replaced by refiner")
    print(f"  [PASS] Test 3: AutoRefiner repaired HTML: Quality Score {report2['quality_score']} -> {refined_report['quality_score']}")

    if failures:
        print("\n[FAIL] Critic/Refiner Test Failures:", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1

    print("\n[SUCCESS] All Design Critic and AutoRefiner unit tests passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
