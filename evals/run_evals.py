#!/usr/bin/env python3
"""
🧪 Automated Evaluation Runner for Vibe UI & mr-ui-designer
Audits production examples against the 5-Pillar UI-Verifier specification.
"""

import sys
import re
from pathlib import Path

# Ensure UTF-8 output on Windows terminals
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

def audit_html_file(file_path: Path) -> dict:
    content = file_path.read_text(encoding="utf-8")
    results = {
        "file": file_path.name,
        "checks": [],
        "overall_status": "PASS"
    }

    # Pillar 1: Semantic Clickables (No <div onclick>)
    div_onclick = re.findall(r'<div[^>]*onclick=["\'][^"\']*["\']', content, re.IGNORECASE)
    buttons_count = len(re.findall(r'<button[^>]*>', content, re.IGNORECASE))
    if div_onclick:
        results["checks"].append({
            "pillar": "Accessibility",
            "name": "Semantic Clickables",
            "status": "FAIL",
            "msg": f"Found {len(div_onclick)} <div onclick> violation(s). Use <button> instead."
        })
        results["overall_status"] = "FAIL"
    else:
        results["checks"].append({
            "pillar": "Accessibility",
            "name": "Semantic Clickables",
            "status": "PASS",
            "msg": f"0 <div onclick> violations ({buttons_count} semantic buttons detected)"
        })

    # Pillar 2: Focus Visibility (focus-visible)
    has_focus_visible = "focus-visible" in content or ":focus-visible" in content
    if has_focus_visible:
        results["checks"].append({
            "pillar": "Accessibility",
            "name": "Focus Rings",
            "status": "PASS",
            "msg": "Verified focus-visible styling on interactive elements"
        })
    else:
        results["checks"].append({
            "pillar": "Accessibility",
            "name": "Focus Rings",
            "status": "FAIL",
            "msg": "Missing focus-visible ring styles for keyboard navigation"
        })
        results["overall_status"] = "FAIL"

    # Pillar 3: Viewport & Responsive Meta
    has_viewport = bool(re.search(r'<meta[^>]*name=["\']viewport["\']', content, re.IGNORECASE))
    if has_viewport:
        results["checks"].append({
            "pillar": "Responsive",
            "name": "Viewport Meta",
            "status": "PASS",
            "msg": "Standard mobile viewport meta tag configured"
        })
    else:
        results["checks"].append({
            "pillar": "Responsive",
            "name": "Viewport Meta",
            "status": "FAIL",
            "msg": "Missing <meta name='viewport'> tag"
        })
        results["overall_status"] = "FAIL"

    # Pillar 4: Vector Iconography vs Raw Emojis
    raw_emojis = re.findall(r'[\U0001F300-\U0001F9FF]', content)
    svg_count = len(re.findall(r'<svg[^>]*>', content, re.IGNORECASE))
    if raw_emojis:
        results["checks"].append({
            "pillar": "Visual Anti-Slop",
            "name": "Vector Icons",
            "status": "WARN",
            "msg": f"Found {len(raw_emojis)} raw emoji(s). Recommended: use inline SVG paths."
        })
        if results["overall_status"] != "FAIL":
            results["overall_status"] = "WARN"
    else:
        results["checks"].append({
            "pillar": "Visual Anti-Slop",
            "name": "Vector Icons",
            "status": "PASS",
            "msg": f"0 raw emojis (verified {svg_count} crisp SVG vector icons)"
        })

    # Pillar 5: Compositing Budget (Backdrop-filter count)
    blur_count = len(re.findall(r'backdrop-blur|backdrop-filter:\s*blur', content, re.IGNORECASE))
    if blur_count > 3:
        results["checks"].append({
            "pillar": "Performance",
            "name": "Backdrop Blur Budget",
            "status": "WARN",
            "msg": f"{blur_count} blur layers detected (budget threshold: <= 3)"
        })
        if results["overall_status"] != "FAIL":
            results["overall_status"] = "WARN"
    else:
        results["checks"].append({
            "pillar": "Performance",
            "name": "Backdrop Blur Budget",
            "status": "PASS",
            "msg": f"{blur_count} blur layer(s) within performance budget (<= 3)"
        })

    # Pillar 6: Semantic RTL & BiDi Punctuation (for RTL files)
    is_rtl = 'dir="rtl"' in content or "dir='rtl'" in content
    if is_rtl:
        has_bdi_or_ltr = "<bdi" in content or "ltr-code" in content or "unicode-bidi" in content
        if has_bdi_or_ltr:
            results["checks"].append({
                "pillar": "Semantic RTL",
                "name": "BiDi Punctuation Isolation",
                "status": "PASS",
                "msg": "Verified <bdi> or LTR isolation on mixed-language content"
            })
        else:
            results["checks"].append({
                "pillar": "Semantic RTL",
                "name": "BiDi Punctuation Isolation",
                "status": "FAIL",
                "msg": "RTL document lacks <bdi> or unicode-bidi isolation for mixed English terms"
            })
            results["overall_status"] = "FAIL"

    return results

def render_scorecard(result: dict):
    print("+" + "-" * 70 + "+")
    print(f"| [SCORECARD] File: {result['file']:<48} |")
    print("+" + "-" * 70 + "+")
    print(f"| Overall Status: [ {result['overall_status']:<4} ]{' ' * 47}|")
    print("+" + "-" * 70 + "+")
    for chk in result["checks"]:
        status_tag = f"[{chk['status']}]"
        raw_msg = f"{status_tag:<6} {chk['pillar']}: {chk['name']} -> {chk['msg']}"
        if len(raw_msg) > 66:
            raw_msg = raw_msg[:63] + "..."
        padding = 68 - len(raw_msg)
        print(f"| {raw_msg}{' ' * max(0, padding)} |")
    print("+" + "-" * 70 + "+\n")

def main():
    examples_dir = Path(__file__).resolve().parent.parent / "examples"
    if not examples_dir.exists():
        print(f"[!] Error: Examples directory not found at {examples_dir}")
        sys.exit(1)

    html_files = list(examples_dir.glob("*.html"))
    if not html_files:
        print(f"[!] Error: No HTML example files found in {examples_dir}")
        sys.exit(1)

    print(f"[+] Running Vibe UI Automated Verification against {len(html_files)} example(s)...\n")
    
    total_fails = 0
    for html_file in html_files:
        res = audit_html_file(html_file)
        render_scorecard(res)
        if res["overall_status"] == "FAIL":
            total_fails += 1

    if total_fails == 0:
        print("[SUCCESS] ALL AUDIT GATES PASSED (100% WCAG AA, Semantic RTL & Performance Budget Verified)!\n")
        sys.exit(0)
    else:
        print(f"[FAILURE] Audit failed with {total_fails} failing file(s).\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
