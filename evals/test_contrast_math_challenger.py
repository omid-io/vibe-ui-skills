#!/usr/bin/env python3
"""
🧪 Empirical Challenger Test Harness: WCAG Contrast Engine & Colorimetry
Tests mathematical rigor, boundary conditions, OKLCH conversion, and CLI JSON purity
in `evals/run_evals.py`.
"""

import json
import math
import subprocess
import sys
from pathlib import Path

# Add repo root to path to import run_evals
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "evals"))

import run_evals

def run_test_suite():
    failures = []
    tests_run = 0

    def assert_eq(actual, expected, msg, tolerance=1e-6):
        nonlocal tests_run
        tests_run += 1
        if isinstance(expected, (int, float)) and isinstance(actual, (int, float)):
            if abs(actual - expected) > tolerance:
                failures.append(f"FAIL: {msg} - Expected {expected}, got {actual} (diff: {abs(actual - expected)})")
            else:
                print(f"  [PASS] {msg} (= {actual})")
        else:
            if actual != expected:
                failures.append(f"FAIL: {msg} - Expected {expected!r}, got {actual!r}")
            else:
                print(f"  [PASS] {msg} (= {actual})")

    def assert_true(condition, msg):
        nonlocal tests_run
        tests_run += 1
        if not condition:
            failures.append(f"FAIL: {msg}")
        else:
            print(f"  [PASS] {msg}")

    print("=" * 70)
    print("TEST SUITE 1: WCAG Relative Luminance & Boundary Conditions")
    print("=" * 70)

    # 1. Pure black vs pure white
    lum_black = run_evals.parse_color_to_luminance("#000000")
    lum_white = run_evals.parse_color_to_luminance("#ffffff")
    assert_eq(lum_black, 0.0, "Luminance of pure black #000000")
    assert_eq(lum_white, 1.0, "Luminance of pure white #ffffff")

    cr_bw = run_evals.contrast_ratio(lum_black, lum_white)
    assert_eq(cr_bw, 21.0, "Contrast ratio of pure black vs pure white must equal exactly 21.0:1", tolerance=1e-9)

    cr_wb = run_evals.contrast_ratio(lum_white, lum_black)
    assert_eq(cr_wb, 21.0, "Contrast ratio commutativity: white vs black must equal exactly 21.0:1", tolerance=1e-9)

    # 2. Identical colors
    cr_black_black = run_evals.contrast_ratio(lum_black, lum_black)
    assert_eq(cr_black_black, 1.0, "Contrast ratio of #000000 vs #000000 must equal exactly 1.0:1", tolerance=1e-9)

    cr_white_white = run_evals.contrast_ratio(lum_white, lum_white)
    assert_eq(cr_white_white, 1.0, "Contrast ratio of #ffffff vs #ffffff must equal exactly 1.0:1", tolerance=1e-9)

    lum_mid_gray = run_evals.parse_color_to_luminance("#808080")
    cr_gray_gray = run_evals.contrast_ratio(lum_mid_gray, lum_mid_gray)
    assert_eq(cr_gray_gray, 1.0, "Contrast ratio of #808080 vs #808080 must equal exactly 1.0:1", tolerance=1e-9)

    # Short hex variations (#000, #fff, #1234, #12345678)
    lum_short_black = run_evals.parse_color_to_luminance("#000")
    assert_eq(lum_short_black, 0.0, "Luminance of short hex #000")
    lum_short_white = run_evals.parse_color_to_luminance("#fff")
    assert_eq(lum_short_white, 1.0, "Luminance of short hex #fff")

    # 3. Body copy threshold boundary (4.5:1)
    # Background = #ffffff (lum = 1.0). Target lum for 4.5:1 is: (1.0 + 0.05)/4.5 - 0.05 = 1.05/4.5 - 0.05 = 7/30 - 0.05 = 0.18333333333333335
    # #767676 (rgb 118, 118, 118): sRGB norm = 118/255 = 0.462745. Linear = ((0.462745 + 0.055)/1.055)**2.4 = 0.180258.
    # Contrast vs #ffffff = 1.05 / (0.180258 + 0.05) = 1.05 / 0.230258 = 4.5599:1 -> passes >= 4.5:1
    # #777777 (rgb 119, 119, 119): sRGB norm = 119/255 = 0.466667. Linear = 0.183951.
    # Contrast vs #ffffff = 1.05 / (0.183951 + 0.05) = 1.05 / 0.233951 = 4.4881:1 -> fails < 4.5:1
    lum_767676 = run_evals.parse_color_to_luminance("#767676")
    cr_767676_white = run_evals.contrast_ratio(lum_white, lum_767676)
    assert_true(cr_767676_white >= 4.5, f"#767676 vs #ffffff must pass body threshold (ratio: {cr_767676_white:.4f}:1 >= 4.5:1)")

    lum_777777 = run_evals.parse_color_to_luminance("#777777")
    cr_777777_white = run_evals.contrast_ratio(lum_white, lum_777777)
    assert_true(cr_777777_white < 4.5, f"#777777 vs #ffffff must fail body threshold (ratio: {cr_777777_white:.4f}:1 < 4.5:1)")

    # Synthetic exact boundaries for 4.5:1
    lum_exact_4_5 = 1.05 / 4.5 - 0.05  # ~ 0.18333333
    cr_exact_4_5 = run_evals.contrast_ratio(1.0, lum_exact_4_5)
    assert_eq(cr_exact_4_5, 4.5, "Exact 4.5:1 boundary calculation", tolerance=1e-7)
    assert_true(cr_exact_4_5 >= 4.5, "Exact 4.5:1 ratio satisfies >= 4.5")

    cr_below_4_5 = run_evals.contrast_ratio(1.0, lum_exact_4_5 + 0.001)
    assert_true(cr_below_4_5 < 4.5, f"Just below 4.5:1 boundary ({cr_below_4_5:.5f}) fails >= 4.5")

    cr_above_4_5 = run_evals.contrast_ratio(1.0, lum_exact_4_5 - 0.001)
    assert_true(cr_above_4_5 > 4.5, f"Just above 4.5:1 boundary ({cr_above_4_5:.5f}) passes >= 4.5")

    # 4. Large text / Header threshold boundary (3.0:1)
    # Background = #ffffff (lum = 1.0). Target lum for 3.0:1 is: (1.0 + 0.05)/3.0 - 0.05 = 0.35 - 0.05 = 0.30
    # #949494 (rgb 148, 148, 148): linear = 0.29707. Contrast vs #ffffff = 1.05 / (0.29707 + 0.05) = 3.025:1 -> passes >= 3.0:1
    # #959595 (rgb 149, 149, 149): linear = 0.30188. Contrast vs #ffffff = 1.05 / (0.30188 + 0.05) = 2.984:1 -> fails < 3.0:1
    lum_949494 = run_evals.parse_color_to_luminance("#949494")
    cr_949494_white = run_evals.contrast_ratio(lum_white, lum_949494)
    assert_true(cr_949494_white >= 3.0, f"#949494 vs #ffffff must pass header threshold (ratio: {cr_949494_white:.4f}:1 >= 3.0:1)")

    lum_959595 = run_evals.parse_color_to_luminance("#959595")
    cr_959595_white = run_evals.contrast_ratio(lum_white, lum_959595)
    assert_true(cr_959595_white < 3.0, f"#959595 vs #ffffff must fail header threshold (ratio: {cr_959595_white:.4f}:1 < 3.0:1)")

    # Synthetic exact boundaries for 3.0:1
    lum_exact_3_0 = 1.05 / 3.0 - 0.05  # 0.30
    cr_exact_3_0 = run_evals.contrast_ratio(1.0, lum_exact_3_0)
    assert_eq(cr_exact_3_0, 3.0, "Exact 3.0:1 boundary calculation", tolerance=1e-7)
    assert_true(cr_exact_3_0 >= 3.0, "Exact 3.0:1 ratio satisfies >= 3.0")

    cr_below_3_0 = run_evals.contrast_ratio(1.0, lum_exact_3_0 + 0.001)
    assert_true(cr_below_3_0 < 3.0, f"Just below 3.0:1 boundary ({cr_below_3_0:.5f}) fails >= 3.0")

    cr_above_3_0 = run_evals.contrast_ratio(1.0, lum_exact_3_0 - 0.001)
    assert_true(cr_above_3_0 > 3.0, f"Just above 3.0:1 boundary ({cr_above_3_0:.5f}) passes >= 3.0")

    print("\n" + "=" * 70)
    print("TEST SUITE 2: OKLCH Color Conversion & Reference Colorimetry")
    print("=" * 70)

    # 1. Achromatic values (C = 0)
    # L=0, C=0 -> Black
    r, g, b = run_evals.oklch_to_linear_srgb(0.0, 0.0, 0.0)
    assert_eq(r, 0.0, "Linear sRGB Red for oklch(0 0 0)")
    assert_eq(g, 0.0, "Linear sRGB Green for oklch(0 0 0)")
    assert_eq(b, 0.0, "Linear sRGB Blue for oklch(0 0 0)")
    assert_eq(run_evals.parse_color_to_luminance("oklch(0 0 0)"), 0.0, "Luminance of oklch(0 0 0)")

    # L=1, C=0 -> White
    r, g, b = run_evals.oklch_to_linear_srgb(1.0, 0.0, 0.0)
    assert_eq(r, 1.0, "Linear sRGB Red for oklch(1 0 0)")
    assert_eq(g, 1.0, "Linear sRGB Green for oklch(1 0 0)")
    assert_eq(b, 1.0, "Linear sRGB Blue for oklch(1 0 0)")
    assert_eq(run_evals.parse_color_to_luminance("oklch(1 0 0)"), 1.0, "Luminance of oklch(1 0 0)")

    # Percentage notation support: oklch(100% 0 0)
    assert_eq(run_evals.parse_color_to_luminance("oklch(100% 0 0)"), 1.0, "Luminance of oklch(100% 0 0)")
    assert_eq(run_evals.parse_color_to_luminance("oklch(0% 0 0)"), 0.0, "Luminance of oklch(0% 0 0)")

    # L=0.5, C=0 -> Achromatic mid-tone: L^3 = 0.5^3 = 0.125
    lum_oklch_mid = run_evals.parse_color_to_luminance("oklch(0.5 0 0)")
    assert_eq(lum_oklch_mid, 0.125, "Luminance of achromatic oklch(0.5 0 0) = L^3 = 0.125", tolerance=1e-4)

    # 2. Standard sRGB primary coordinates in OKLCH
    # Reference values from CSS Color 4 / Björn Ottosson:
    # Pure sRGB Red (#ff0000) -> OKLCH L ≈ 0.627955, C ≈ 0.257683, H ≈ 29.233885°
    # Expected relative luminance for Red: 0.2126
    lum_red_oklch = run_evals.parse_color_to_luminance("oklch(0.627955 0.257683 29.233885)")
    assert_eq(lum_red_oklch, 0.2126, "Relative luminance of sRGB Red via OKLCH coordinates", tolerance=0.005)

    # Pure sRGB Green (#00ff00) -> OKLCH L ≈ 0.86644, C ≈ 0.29483, H ≈ 142.495°
    # Expected relative luminance for Green: 0.7152
    lum_green_oklch = run_evals.parse_color_to_luminance("oklch(0.86644 0.29483 142.495)")
    assert_eq(lum_green_oklch, 0.7152, "Relative luminance of sRGB Green via OKLCH coordinates", tolerance=0.005)

    # Pure sRGB Blue (#0000ff) -> OKLCH L ≈ 0.45201, C ≈ 0.31321, H ≈ 264.052°
    # Expected relative luminance for Blue: 0.0722
    lum_blue_oklch = run_evals.parse_color_to_luminance("oklch(0.45201 0.31321 264.052)")
    assert_eq(lum_blue_oklch, 0.0722, "Relative luminance of sRGB Blue via OKLCH coordinates", tolerance=0.005)

    # Pure sRGB Yellow (#ffff00) -> OKLCH L ≈ 0.96798, C ≈ 0.21101, H ≈ 109.769°
    # Expected relative luminance: 0.2126 + 0.7152 = 0.9278
    lum_yellow_oklch = run_evals.parse_color_to_luminance("oklch(0.96798 0.21101 109.769)")
    assert_eq(lum_yellow_oklch, 0.9278, "Relative luminance of sRGB Yellow via OKLCH coordinates", tolerance=0.005)

    # 3. Design System Production Tokens
    # Minimalist SaaS: Canvas = oklch(0.985 0.002 247.839), Text Ink = oklch(0.145 0.005 285.823)
    lum_saas_bg = run_evals.parse_color_to_luminance("oklch(0.985 0.002 247.839)")
    lum_saas_fg = run_evals.parse_color_to_luminance("oklch(0.145 0.005 285.823)")
    cr_saas = run_evals.contrast_ratio(lum_saas_bg, lum_saas_fg)
    assert_true(cr_saas >= 15.0, f"Minimalist SaaS token contrast {cr_saas:.2f}:1 exceeds 15.0:1")

    # Deg suffix support: oklch(0.9 0.05 120deg)
    lum_deg = run_evals.parse_color_to_luminance("oklch(0.9 0.05 120deg)")
    assert_true(lum_deg > 0.0, "oklch with 'deg' suffix parsed successfully")

    # Alpha notation support: oklch(0.9 0.05 120 / 0.8)
    lum_alpha = run_evals.parse_color_to_luminance("oklch(0.9 0.05 120 / 0.8)")
    assert_true(lum_alpha > 0.0, "oklch with alpha slash syntax parsed successfully")

    # CSS comments stripping: "oklch(0.9 0 0) /* paper */"
    lum_comment = run_evals.parse_color_to_luminance("oklch(0.9 0 0) /* paper */")
    assert_eq(lum_comment, 0.9 ** 3, "oklch with trailing comment stripped correctly", tolerance=1e-3)

    print("\n" + "=" * 70)
    print("TEST SUITE 3: CLI Machine-Readable JSON Output Purity")
    print("=" * 70)

    python_exe = sys.executable

    # 1. Full suite run with --json
    cmd_full = [python_exe, str(REPO_ROOT / "evals" / "run_evals.py"), "--json"]
    proc_full = subprocess.run(cmd_full, cwd=str(REPO_ROOT), capture_output=True, text=True)

    assert_eq(proc_full.returncode, 0, "Full suite --json must exit code 0")
    assert_eq(proc_full.stderr.strip(), "", "Full suite --json stderr must be empty")

    stdout_raw = proc_full.stdout
    # Test stdout starts with '{' and ends with '}'
    stripped_out = stdout_raw.strip()
    assert_true(stripped_out.startswith("{") and stripped_out.endswith("}"),
                "stdout starts and ends with JSON braces (no stray prefix/suffix)")

    parsed_json = None
    try:
        parsed_json = json.loads(stdout_raw)
        assert_true(True, "stdout is 100% parseable JSON")
    except Exception as e:
        assert_true(False, f"stdout failed JSON parsing: {e}")

    if parsed_json:
        assert_eq(parsed_json.get("suite"), "Vibe UI Evaluation Suite", "JSON payload contains suite name")
        assert_eq(parsed_json.get("overall_status"), "PASS", "overall_status is PASS")
        assert_eq(parsed_json.get("exit_code"), 0, "exit_code field is 0")
        assert_true("summary" in parsed_json, "JSON summary object exists")
        assert_true("targets" in parsed_json, "JSON targets array exists")
        assert_true(parsed_json["summary"]["failed_targets"] == 0, "failed_targets is 0")

    # 2. Standalone fixture runner with --json (valid fixture)
    cmd_fix_val = [
        python_exe,
        str(REPO_ROOT / "evals" / "run_evals.py"),
        "--json",
        "--fixture",
        str(REPO_ROOT / "evals" / "fixtures" / "valid_design_spec.json"),
    ]
    proc_val = subprocess.run(cmd_fix_val, cwd=str(REPO_ROOT), capture_output=True, text=True)
    assert_eq(proc_val.returncode, 0, "Valid fixture with --json must exit code 0")
    try:
        val_json = json.loads(proc_val.stdout)
        assert_eq(val_json.get("overall_status"), "PASS", "Valid fixture JSON status is PASS")
        assert_eq(val_json.get("exit_code"), 0, "Valid fixture JSON exit_code is 0")
        assert_eq(len(val_json.get("errors", [])), 0, "Valid fixture has 0 errors")
    except Exception as e:
        assert_true(False, f"Valid fixture JSON parsing failed: {e}")

    # 3. Standalone fixture runner with --json (negative fixtures -> exit code 1, pure JSON)
    neg_fixtures = [
        ("invalid_archetype.json", "domain_archetype"),
        ("out_of_range_entropy.json", "entropy_heuristic"),
        ("touch_target_below_24px.json", "min_touch_target_px"),
    ]
    for fix_name, expected_keyword in neg_fixtures:
        cmd_neg = [
            python_exe,
            str(REPO_ROOT / "evals" / "run_evals.py"),
            "--json",
            "--fixture",
            str(REPO_ROOT / "evals" / "fixtures" / fix_name),
        ]
        proc_neg = subprocess.run(cmd_neg, cwd=str(REPO_ROOT), capture_output=True, text=True)
        assert_eq(proc_neg.returncode, 1, f"Negative fixture '{fix_name}' must exit code 1")
        try:
            neg_json = json.loads(proc_neg.stdout)
            assert_eq(neg_json.get("overall_status"), "FAIL", f"Negative fixture '{fix_name}' JSON status is FAIL")
            assert_eq(neg_json.get("exit_code"), 1, f"Negative fixture '{fix_name}' JSON exit_code is 1")
            errors = neg_json.get("errors", [])
            assert_true(len(errors) > 0, f"Negative fixture '{fix_name}' returns >= 1 errors")
            assert_true(any(expected_keyword in err for err in errors),
                        f"Error in '{fix_name}' correctly mentions '{expected_keyword}'")
        except Exception as e:
            assert_true(False, f"Negative fixture '{fix_name}' JSON parsing failed: {e}")

    print("\n" + "=" * 70)
    print(f"SUMMARY: {tests_run} tests executed. {len(failures)} failure(s).")
    print("=" * 70)

    if failures:
        print("\nFAILURES:")
        for f in failures:
            print(f"  ❌ {f}")
        return 1
    else:
        print("\n✅ ALL EMPIRICAL CHALLENGER TESTS PASSED WITH 100% PRECISION!")
        return 0

if __name__ == "__main__":
    sys.exit(run_test_suite())
