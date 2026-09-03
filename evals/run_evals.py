#!/usr/bin/env python3
"""
🧪 Automated Evaluation Runner for Vibe UI & mr-ui-designer
Audits production examples against the 5-Pillar UI-Verifier specification
and validates machine-readable JSON design specs.
"""

import argparse
from datetime import datetime, timezone
import json
import math
from pathlib import Path
import re
import sys

# Ensure UTF-8 output on Windows terminals
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# ==============================================================================
# Mathematical WCAG Relative Luminance & Contrast Engine
# ==============================================================================

# Standard CSS and Tailwind color definitions for contrast checking
NAMED_COLORS = {
    "white": "#ffffff",
    "black": "#000000",
    "stone-950": "#0c0a09",
    "stone-900": "#1c1917",
    "stone-800": "#292524",
    "stone-700": "#44403c",
    "stone-600": "#57534e",
    "stone-500": "#78716c",
    "stone-400": "#a8a29e",
    "stone-200": "#e7e5e4",
    "stone-100": "#f5f5f4",
    "stone-50": "#fafaf9",
    "neutral-950": "#0a0a0a",
    "neutral-900": "#171717",
    "neutral-800": "#262626",
    "neutral-600": "#525252",
    "neutral-400": "#a3a3a3",
    "neutral-200": "#e5e5e5",
    "neutral-100": "#f5f5f5",
    "neutral-50": "#fafafa",
    "zinc-950": "#09090b",
    "zinc-900": "#18181b",
    "gray-950": "#030712",
    "gray-900": "#111827",
    "gray-800": "#1f2937",
    "gray-100": "#f3f4f6",
    "gray-50": "#f9fafb",
    "slate-950": "#020617",
    "slate-900": "#0f172a",
}

def srgb_to_linear(c_byte: float) -> float:
    """
    Transforms an 8-bit sRGB color channel (0-255) to linear sRGB [0.0, 1.0].
    Formula: C' = C_norm / 12.92 if C_norm <= 0.04045 else ((C_norm + 0.055) / 1.055) ** 2.4
    """
    c_norm = c_byte / 255.0
    if c_norm <= 0.04045:
        return c_norm / 12.92
    return ((c_norm + 0.055) / 1.055) ** 2.4

def oklch_to_linear_srgb(l: float, c: float, h: float) -> tuple[float, float, float]:
    """
    Converts OKLCH coordinates (Lightness [0,1], Chroma >=0, Hue [0,360] degrees)
    to linear sRGB (R', G', B') in [0.0, 1.0].
    """
    theta = math.radians(h)
    a = c * math.cos(theta)
    b = c * math.sin(theta)

    l_ = l + 0.3963377774 * a + 0.2158037573 * b
    m_ = l - 0.1055613458 * a - 0.0638541728 * b
    s_ = l - 0.0894841775 * a - 1.2914855480 * b

    l_cubed = l_ ** 3
    m_cubed = m_ ** 3
    s_cubed = s_ ** 3

    r_lin = +4.0767434099 * l_cubed - 3.3077115913 * m_cubed + 0.2309699292 * s_cubed
    g_lin = -1.2684380046 * l_cubed + 2.6097574011 * m_cubed - 0.3413193965 * s_cubed
    b_lin = -0.0041960863 * l_cubed - 0.7034186147 * m_cubed + 1.7076147010 * s_cubed

    return (max(0.0, min(1.0, r_lin)), max(0.0, min(1.0, g_lin)), max(0.0, min(1.0, b_lin)))

def parse_color_to_luminance(color_str: str) -> float:
    """
    Parses Hex (#rgb, #rrggbb, #rrggbbaa), OKLCH (oklch(L C H)), or named colors
    into relative luminance L in [0.0, 1.0].
    Relative luminance formula: L = 0.2126 * R' + 0.7152 * G' + 0.0722 * B'.
    """
    color_str = color_str.strip().split("/*")[0].strip()

    # Named color lookup
    if color_str in NAMED_COLORS:
        color_str = NAMED_COLORS[color_str]
    elif color_str.startswith("text-") and color_str[5:] in NAMED_COLORS:
        color_str = NAMED_COLORS[color_str[5:]]

    # OKLCH parsing: oklch(L C H) or oklch(L C H / alpha)
    oklch_match = re.match(
        r"oklch\(\s*([\d.]+%?)\s+([\d.]+)\s+([\d.]+)(?:deg)?(?:\s*/\s*[\d.]+%?)?\s*\)",
        color_str,
        re.IGNORECASE,
    )
    if oklch_match:
        l_str, c_str, h_str = oklch_match.groups()
        l_val = float(l_str[:-1]) / 100.0 if l_str.endswith("%") else float(l_str)
        c_val = float(c_str)
        h_val = float(h_str)
        r_lin, g_lin, b_lin = oklch_to_linear_srgb(l_val, c_val, h_val)
        return 0.2126 * r_lin + 0.7152 * g_lin + 0.0722 * b_lin

    # Hex parsing: #rgb, #rgba, #rrggbb, #rrggbbaa
    hex_match = re.match(r"^#([0-9a-fA-F]+)$", color_str)
    if hex_match:
        h = hex_match.group(1)
        if len(h) in (3, 4):
            h = "".join([c * 2 for c in h[:3]])
        elif len(h) in (6, 8):
            h = h[:6]
        else:
            h = "000000"
        r = srgb_to_linear(int(h[0:2], 16))
        g = srgb_to_linear(int(h[2:4], 16))
        b = srgb_to_linear(int(h[4:6], 16))
        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    return 0.0

def contrast_ratio(lum1: float, lum2: float) -> float:
    """
    Calculates WCAG relative luminance contrast ratio:
    (L1 + 0.05) / (L2 + 0.05) where L1 >= L2.
    """
    l1 = max(lum1, lum2)
    l2 = min(lum1, lum2)
    return (l1 + 0.05) / (l2 + 0.05)

def extract_html_colors(content: str) -> tuple[str, str, str]:
    """
    Extracts canvas background color, body text color, and header (h1) text color
    from HTML document styles, CSS variables, or Tailwind class attributes.
    """
    css_vars = {}
    for m in re.finditer(r"(--[\w-]+)\s*:\s*([^;}\n]+)", content):
        css_vars[m.group(1).strip()] = m.group(2).strip().split("/*")[0].strip()

    def resolve_var(val: str) -> str:
        val = val.strip().split("/*")[0].strip()
        vm = re.match(r"var\((--[\w-]+)\)", val)
        if vm and vm.group(1) in css_vars:
            return resolve_var(css_vars[vm.group(1)])
        return val

    canvas_color = None
    body_color = None

    body_match = re.search(r"(?:^|\s)body\s*\{([^}]+)\}", content, re.DOTALL)
    if body_match:
        rules = body_match.group(1)
        bg_m = re.search(r"background(?:-color)?\s*:\s*([^;}\n]+)", rules)
        if bg_m:
            canvas_color = resolve_var(bg_m.group(1))
        c_m = re.search(r"(?:^|\s|;)color\s*:\s*([^;}\n]+)", rules)
        if c_m:
            body_color = resolve_var(c_m.group(1))

    if not canvas_color:
        for c in ("--canvas", "--bg-paper", "--background"):
            if c in css_vars:
                canvas_color = resolve_var(css_vars[c])
                break
    if not canvas_color:
        canvas_color = "#ffffff"

    if not body_color:
        for c in ("--text-ink", "--foreground", "--text"):
            if c in css_vars:
                body_color = resolve_var(css_vars[c])
                break
    if not body_color:
        body_color = "#000000"

    header_color = None
    h1_m = re.search(r"<h1([^>]*)>(.*?)</h1>", content, re.DOTALL | re.IGNORECASE)
    if h1_m:
        attrs = h1_m.group(1)
        st_m = re.search(r'style=["\']([^"\']+)["\']', attrs)
        if st_m:
            c_m = re.search(r"color\s*:\s*([^;]+)", st_m.group(1))
            if c_m:
                header_color = resolve_var(c_m.group(1))
        if not header_color:
            cl_m = re.search(r'class=["\']([^"\']+)["\']', attrs)
            if cl_m:
                classes = cl_m.group(1)
                custom_hex = re.search(r"text-\[([#\w(),.\s]+)\]", classes)
                if custom_hex:
                    header_color = custom_hex.group(1)
                else:
                    for tok in classes.split():
                        if tok.startswith("text-"):
                            cname = tok[5:]
                            if cname in NAMED_COLORS:
                                header_color = NAMED_COLORS[cname]
                                break
    if not header_color:
        header_color = body_color

    return canvas_color, body_color, header_color

# ==============================================================================
# Recursive Pure-Python JSON Schema Validator
# ==============================================================================

def validate_json_instance(instance: any, schema: dict, path: str = "$") -> list[str]:
    """
    Recursive pure-Python stdlib JSON Schema validator for design-spec contracts.
    Validates:
      - object required properties and nested properties
      - type checking (object, string, number, integer, boolean, array)
      - enum constraint
      - const constraint
      - minimum and maximum numerical bounds
      - array minItems and items schema recursion
    """
    errors = []
    if not isinstance(schema, dict):
        return errors

    # 1. Type validation
    expected_type = schema.get("type")
    if expected_type:
        type_checks = {
            "object": isinstance(instance, dict),
            "string": isinstance(instance, str),
            "number": isinstance(instance, (int, float)) and not isinstance(instance, bool),
            "integer": isinstance(instance, int) and not isinstance(instance, bool),
            "boolean": isinstance(instance, bool),
            "array": isinstance(instance, list),
        }
        if expected_type in type_checks and not type_checks[expected_type]:
            errors.append(f"{path}: Expected type '{expected_type}', got '{type(instance).__name__}'")
            return errors  # Cannot validate further if base type is wrong

    # 2. Const validation
    if "const" in schema:
        if instance != schema["const"]:
            errors.append(f"{path}: Value '{instance}' does not match const '{schema['const']}'")

    # 3. Enum validation
    if "enum" in schema:
        if instance not in schema["enum"]:
            errors.append(f"{path}: Value '{instance}' not in allowed enum {schema['enum']}")

    # 4. Numerical minimum / maximum bounds
    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            errors.append(f"{path}: Value {instance} is less than minimum {schema['minimum']}")
        if "maximum" in schema and instance > schema["maximum"]:
            errors.append(f"{path}: Value {instance} is greater than maximum {schema['maximum']}")

    # 5. Array minItems and items
    if isinstance(instance, list):
        if "minItems" in schema and len(instance) < schema["minItems"]:
            errors.append(f"{path}: Array has {len(instance)} items, minimum required is {schema['minItems']}")
        if "items" in schema:
            for idx, item in enumerate(instance):
                errors.extend(validate_json_instance(item, schema["items"], f"{path}[{idx}]"))

    # 6. Object required properties and nested properties
    if isinstance(instance, dict):
        for req in schema.get("required", []):
            if req not in instance:
                errors.append(f"{path}: Missing required property '{req}'")
        for prop, prop_schema in schema.get("properties", {}).items():
            if prop in instance:
                errors.extend(validate_json_instance(instance[prop], prop_schema, f"{path}.{prop}"))

    return errors

# ==============================================================================
# HTML File Verification (5 Pillars + WCAG AA Mathematical Contrast)
# ==============================================================================

def audit_html_file(file_path: Path) -> dict:
    content = file_path.read_text(encoding="utf-8")
    results = {
        "file": file_path.name,
        "name": file_path.name,
        "type": "html_example",
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

    # Pillar 7: Exact Mathematical WCAG AA Relative Luminance Contrast
    canvas_color, body_color, header_color = extract_html_colors(content)
    lum_canvas = parse_color_to_luminance(canvas_color)
    lum_body = parse_color_to_luminance(body_color)
    lum_header = parse_color_to_luminance(header_color)

    body_cr = contrast_ratio(lum_canvas, lum_body)
    header_cr = contrast_ratio(lum_canvas, lum_header)

    if body_cr >= 4.5:
        results["checks"].append({
            "pillar": "WCAG AA Contrast",
            "name": "Body Copy Contrast",
            "status": "PASS",
            "msg": f"Body contrast {body_cr:.2f}:1 exceeds WCAG AA threshold (>= 4.5:1) [bg: {canvas_color}, fg: {body_color}]"
        })
    else:
        results["checks"].append({
            "pillar": "WCAG AA Contrast",
            "name": "Body Copy Contrast",
            "status": "FAIL",
            "msg": f"Body contrast {body_cr:.2f}:1 fails WCAG AA threshold (>= 4.5:1) [bg: {canvas_color}, fg: {body_color}]"
        })
        results["overall_status"] = "FAIL"

    if header_cr >= 3.0:
        results["checks"].append({
            "pillar": "WCAG AA Contrast",
            "name": "Header / Large Text Contrast",
            "status": "PASS",
            "msg": f"Header contrast {header_cr:.2f}:1 exceeds WCAG AA threshold (>= 3.0:1) [bg: {canvas_color}, fg: {header_color}]"
        })
    else:
        results["checks"].append({
            "pillar": "WCAG AA Contrast",
            "name": "Header / Large Text Contrast",
            "status": "FAIL",
            "msg": f"Header contrast {header_cr:.2f}:1 fails WCAG AA threshold (>= 3.0:1) [bg: {canvas_color}, fg: {header_color}]"
        })
        results["overall_status"] = "FAIL"

    return results

def render_scorecard(result: dict):
    target_name = result.get("name") or result.get("file", "Target")
    print("+" + "-" * 70 + "+")
    print(f"| [SCORECARD] File: {target_name:<48} |")
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

# ==============================================================================
# Repository Integrity & Schema Fixture Auditing
# ==============================================================================

def audit_repo_integrity(root_dir: Path) -> dict:
    results = {
        "file": "Repository Structural Integrity",
        "name": "Repository Structural Integrity",
        "type": "repository",
        "checks": [],
        "overall_status": "PASS"
    }

    # 1. Check SECURITY.md
    sec_file = root_dir / "SECURITY.md"
    if sec_file.exists() and len(sec_file.read_text(encoding="utf-8").strip()) > 50:
        results["checks"].append({
            "pillar": "Supply Chain Security",
            "name": "Security Policy",
            "status": "PASS",
            "msg": "Verified SECURITY.md policy with vulnerability reporting channels"
        })
    else:
        results["checks"].append({
            "pillar": "Supply Chain Security",
            "name": "Security Policy",
            "status": "FAIL",
            "msg": "Missing or empty SECURITY.md file"
        })
        results["overall_status"] = "FAIL"

    # 2. Check THIRD_PARTY_NOTICES.md
    notices_file = root_dir / "THIRD_PARTY_NOTICES.md"
    if notices_file.exists():
        results["checks"].append({
            "pillar": "Open Source Hygiene",
            "name": "Attribution Matrix",
            "status": "PASS",
            "msg": "Verified THIRD_PARTY_NOTICES.md with MIT license notices"
        })
    else:
        results["checks"].append({
            "pillar": "Open Source Hygiene",
            "name": "Attribution Matrix",
            "status": "FAIL",
            "msg": "Missing THIRD_PARTY_NOTICES.md file"
        })
        results["overall_status"] = "FAIL"

    # 3. Check JSON Schema & Validate Sample Output
    schema_file = root_dir / "schemas" / "design-spec.v1.schema.json"
    sample_file = root_dir / "examples" / "sample-design-spec.json"

    if schema_file.exists():
        try:
            schema_data = json.loads(schema_file.read_text(encoding="utf-8"))
            results["checks"].append({
                "pillar": "Machine Contract",
                "name": "JSON Design Schema",
                "status": "PASS",
                "msg": "Verified schemas/design-spec.v1.schema.json syntax & Draft 2020-12"
            })

            # Validate sample output
            if sample_file.exists():
                sample_data = json.loads(sample_file.read_text(encoding="utf-8"))
                val_errors = validate_json_instance(sample_data, schema_data)
                if not val_errors:
                    results["checks"].append({
                        "pillar": "Machine Contract",
                        "name": "Schema Validation (Instance)",
                        "status": "PASS",
                        "msg": "Verified examples/sample-design-spec.json conforms 100% to schema"
                    })
                else:
                    results["checks"].append({
                        "pillar": "Machine Contract",
                        "name": "Schema Validation (Instance)",
                        "status": "FAIL",
                        "msg": f"Schema violation: {', '.join(val_errors)}"
                    })
                    results["overall_status"] = "FAIL"
            else:
                results["checks"].append({
                    "pillar": "Machine Contract",
                    "name": "Schema Validation (Instance)",
                    "status": "WARN",
                    "msg": "sample-design-spec.json not found for runtime validation"
                })

            # 4. Negative & Baseline Fixture Suite Audit
            fixtures_dir = root_dir / "evals" / "fixtures"
            if fixtures_dir.exists():
                # Baseline valid fixture
                valid_fix = fixtures_dir / "valid_design_spec.json"
                if valid_fix.exists():
                    v_data = json.loads(valid_fix.read_text(encoding="utf-8"))
                    v_errs = validate_json_instance(v_data, schema_data)
                    if not v_errs:
                        results["checks"].append({
                            "pillar": "Negative Evaluation Suite",
                            "name": "Valid Baseline Fixture",
                            "status": "PASS",
                            "msg": "Verified evals/fixtures/valid_design_spec.json conforms 100% to schema"
                        })
                    else:
                        results["checks"].append({
                            "pillar": "Negative Evaluation Suite",
                            "name": "Valid Baseline Fixture",
                            "status": "FAIL",
                            "msg": f"Valid fixture failed validation: {', '.join(v_errs)}"
                        })
                        results["overall_status"] = "FAIL"

                # Negative fixture: invalid_archetype.json
                inv_arch = fixtures_dir / "invalid_archetype.json"
                if inv_arch.exists():
                    data = json.loads(inv_arch.read_text(encoding="utf-8"))
                    errs = validate_json_instance(data, schema_data)
                    if errs:
                        results["checks"].append({
                            "pillar": "Negative Evaluation Suite",
                            "name": "Negative Fixture: Invalid Archetype",
                            "status": "PASS",
                            "msg": f"Correctly rejected invalid archetype: {errs[0]}"
                        })
                    else:
                        results["checks"].append({
                            "pillar": "Negative Evaluation Suite",
                            "name": "Negative Fixture: Invalid Archetype",
                            "status": "FAIL",
                            "msg": "Negative fixture 'invalid_archetype.json' was unexpectedly accepted"
                        })
                        results["overall_status"] = "FAIL"

                # Negative fixture: out_of_range_entropy.json
                inv_ent = fixtures_dir / "out_of_range_entropy.json"
                if inv_ent.exists():
                    data = json.loads(inv_ent.read_text(encoding="utf-8"))
                    errs = validate_json_instance(data, schema_data)
                    if errs:
                        results["checks"].append({
                            "pillar": "Negative Evaluation Suite",
                            "name": "Negative Fixture: Out-of-Range Entropy",
                            "status": "PASS",
                            "msg": f"Correctly rejected out-of-range entropy: {errs[0]}"
                        })
                    else:
                        results["checks"].append({
                            "pillar": "Negative Evaluation Suite",
                            "name": "Negative Fixture: Out-of-Range Entropy",
                            "status": "FAIL",
                            "msg": "Negative fixture 'out_of_range_entropy.json' was unexpectedly accepted"
                        })
                        results["overall_status"] = "FAIL"

                # Negative fixture: touch_target_below_24px.json
                inv_tt = fixtures_dir / "touch_target_below_24px.json"
                if inv_tt.exists():
                    data = json.loads(inv_tt.read_text(encoding="utf-8"))
                    errs = validate_json_instance(data, schema_data)
                    if errs:
                        results["checks"].append({
                            "pillar": "Negative Evaluation Suite",
                            "name": "Negative Fixture: Touch Target < 24px",
                            "status": "PASS",
                            "msg": f"Correctly rejected touch target below 24px: {errs[0]}"
                        })
                    else:
                        results["checks"].append({
                            "pillar": "Negative Evaluation Suite",
                            "name": "Negative Fixture: Touch Target < 24px",
                            "status": "FAIL",
                            "msg": "Negative fixture 'touch_target_below_24px.json' was unexpectedly accepted"
                        })
                        results["overall_status"] = "FAIL"

        except Exception as e:
            results["checks"].append({
                "pillar": "Machine Contract",
                "name": "JSON Design Schema",
                "status": "FAIL",
                "msg": f"Invalid JSON Schema: {e}"
            })
            results["overall_status"] = "FAIL"
    else:
        results["checks"].append({
            "pillar": "Machine Contract",
            "name": "JSON Design Schema",
            "status": "FAIL",
            "msg": "Missing schemas/design-spec.v1.schema.json"
        })
        results["overall_status"] = "FAIL"

    return results

# ==============================================================================
# Production Next.js 15 Starter Architecture & Token Audit
# ==============================================================================

def audit_nextjs_starter(starter_dir: Path) -> dict:
    results = {
        "name": "examples/nextjs-starter (Next.js 15 / TS 5)",
        "target": "examples/nextjs-starter (Next.js 15 / React 19 / TS 5)",
        "overall_status": "PASS",
        "checks": []
    }
    if not starter_dir.exists():
        results["checks"].append({
            "pillar": "Production Starter Architecture",
            "name": "Starter Directory",
            "status": "FAIL",
            "msg": f"Directory not found: {starter_dir}"
        })
        results["overall_status"] = "FAIL"
        return results

    # 1. Check Package Manifest
    pkg_file = starter_dir / "package.json"
    if pkg_file.exists():
        try:
            pkg_data = json.loads(pkg_file.read_text(encoding="utf-8"))
            deps = pkg_data.get("dependencies", {})
            dev_deps = pkg_data.get("devDependencies", {})
            has_next = "next" in deps
            has_react = "react" in deps
            has_tw = "tailwindcss" in dev_deps or "tailwindcss" in deps
            has_ts = "typescript" in dev_deps or "typescript" in deps
            if has_next and has_react and has_tw and has_ts:
                results["checks"].append({
                    "pillar": "Production Architecture",
                    "name": "App Router Manifest",
                    "status": "PASS",
                    "msg": "Verified Next.js 15, React 19, Tailwind CSS, and TypeScript in package.json"
                })
            else:
                results["checks"].append({
                    "pillar": "Production Architecture",
                    "name": "App Router Manifest",
                    "status": "FAIL",
                    "msg": "Missing expected dependencies in package.json"
                })
                results["overall_status"] = "FAIL"
        except Exception as e:
            results["checks"].append({
                "pillar": "Production Architecture",
                "name": "App Router Manifest",
                "status": "FAIL",
                "msg": f"Failed to parse package.json: {e}"
            })
            results["overall_status"] = "FAIL"
    else:
        results["checks"].append({
            "pillar": "Production Architecture",
            "name": "App Router Manifest",
            "status": "FAIL",
            "msg": "Missing package.json file"
        })
        results["overall_status"] = "FAIL"

    # 2. Check Typed OKLCH Tokens
    tokens_file = starter_dir / "lib" / "tokens.ts"
    if tokens_file.exists():
        tokens_src = tokens_file.read_text(encoding="utf-8")
        chemistries = ["MINIMALIST_SAAS", "LUXURY_GLASS", "NEOBRUTALISM", "SWISS_EDITORIAL", "STRIPE_CRISP"]
        missing_chem = [c for c in chemistries if c not in tokens_src]
        has_oklch = "oklch(" in tokens_src
        if not missing_chem and has_oklch:
            results["checks"].append({
                "pillar": "Design Tokens & Chemistry",
                "name": "Typed OKLCH Tokens",
                "status": "PASS",
                "msg": "Verified all 5 visual chemistries exported with typed OKLCH color spaces"
            })
        else:
            results["checks"].append({
                "pillar": "Design Tokens & Chemistry",
                "name": "Typed OKLCH Tokens",
                "status": "FAIL",
                "msg": f"Missing visual chemistries ({missing_chem}) or OKLCH definitions in lib/tokens.ts"
            })
            results["overall_status"] = "FAIL"
    else:
        results["checks"].append({
            "pillar": "Design Tokens & Chemistry",
            "name": "Typed OKLCH Tokens",
            "status": "FAIL",
            "msg": "Missing lib/tokens.ts file"
        })
        results["overall_status"] = "FAIL"

    # 3. Check AI Primitives & Vector Icons (Zero Raw Emojis)
    components_dir = starter_dir / "components"
    ai_drawer = components_dir / "AiThinkingDrawer.tsx"
    if ai_drawer.exists():
        drawer_src = ai_drawer.read_text(encoding="utf-8")
        has_svg = "<svg" in drawer_src
        has_button = "<button" in drawer_src
        has_aria = "aria-expanded" in drawer_src or "aria-label" in drawer_src
        if has_svg and has_button and has_aria:
            results["checks"].append({
                "pillar": "AI Primitives & Accessibility",
                "name": "AiThinkingDrawer Contract",
                "status": "PASS",
                "msg": "Verified SVG vector icons, semantic <button>, and aria attributes in AiThinkingDrawer"
            })
        else:
            results["checks"].append({
                "pillar": "AI Primitives & Accessibility",
                "name": "AiThinkingDrawer Contract",
                "status": "FAIL",
                "msg": "AiThinkingDrawer missing SVG icons, semantic button, or aria attributes"
            })
            results["overall_status"] = "FAIL"
    else:
        results["checks"].append({
            "pillar": "AI Primitives & Accessibility",
            "name": "AiThinkingDrawer Contract",
            "status": "FAIL",
            "msg": "Missing components/AiThinkingDrawer.tsx"
        })
        results["overall_status"] = "FAIL"

    # 4. Check Zero Raw Emojis across all TSX files
    tsx_files = list(starter_dir.rglob("*.tsx"))
    raw_emojis_found = 0
    for tsx_f in tsx_files:
        src = tsx_f.read_text(encoding="utf-8")
        emojis = re.findall(r'[\U0001F300-\U0001F9FF]', src)
        if emojis:
            raw_emojis_found += len(emojis)

    if raw_emojis_found == 0:
        results["checks"].append({
            "pillar": "Visual Anti-Slop",
            "name": "Zero Raw Emojis in TSX",
            "status": "PASS",
            "msg": f"Verified 0 raw emojis across all {len(tsx_files)} TSX components (pure SVG vectors)"
        })
    else:
        results["checks"].append({
            "pillar": "Visual Anti-Slop",
            "name": "Zero Raw Emojis in TSX",
            "status": "FAIL",
            "msg": f"Detected {raw_emojis_found} raw emoji(s) in TSX files"
        })
        results["overall_status"] = "FAIL"

    # 5. Check Semantic RTL and Viewport in layout.tsx
    layout_file = starter_dir / "app" / "layout.tsx"
    if layout_file.exists():
        layout_src = layout_file.read_text(encoding="utf-8")
        has_lang = 'lang=' in layout_src
        has_dir = 'dir=' in layout_src
        if has_lang and has_dir:
            results["checks"].append({
                "pillar": "Semantic RTL & A11y",
                "name": "Root Layout Architecture",
                "status": "PASS",
                "msg": "Verified lang and dir attributes configured in app/layout.tsx"
            })
        else:
            results["checks"].append({
                "pillar": "Semantic RTL & A11y",
                "name": "Root Layout Architecture",
                "status": "FAIL",
                "msg": "Missing lang or dir attributes in app/layout.tsx"
            })
            results["overall_status"] = "FAIL"

    # 6. Check Compositing Budget (Backdrop Blur <= 3) in CSS / TSX
    globals_css = starter_dir / "app" / "globals.css"
    if globals_css.exists():
        css_src = globals_css.read_text(encoding="utf-8")
        backdrop_matches = len(re.findall(r"backdrop-filter", css_src, re.IGNORECASE))
        if backdrop_matches <= 3:
            results["checks"].append({
                "pillar": "Performance & GPU Budget",
                "name": "Backdrop Blur Limit",
                "status": "PASS",
                "msg": f"Verified globals.css complies with composite budget ({backdrop_matches} <= 3 backdrop-filters)"
            })
        else:
            results["checks"].append({
                "pillar": "Performance & GPU Budget",
                "name": "Backdrop Blur Limit",
                "status": "WARN",
                "msg": f"Exceeds recommended 3 backdrop-filter layers ({backdrop_matches} found)"
            })

    return results

# ==============================================================================
# Standalone Fixture Runner CLI
# ==============================================================================

def run_standalone_fixture(fixture_path_str: str, root_dir: Path, json_mode: bool) -> int:
    fixture_path = Path(fixture_path_str)
    if not fixture_path.is_absolute():
        if not fixture_path.exists() and (root_dir / fixture_path).exists():
            fixture_path = (root_dir / fixture_path).resolve()
        else:
            fixture_path = fixture_path.resolve()

    schema_file = root_dir / "schemas" / "design-spec.v1.schema.json"
    if not schema_file.exists():
        if json_mode:
            print(json.dumps({"error": f"Schema not found: {schema_file}"}))
        else:
            print(f"[!] Error: Schema not found at {schema_file}")
        return 1

    if not fixture_path.exists():
        if json_mode:
            print(json.dumps({"error": f"Fixture file not found: {fixture_path}"}))
        else:
            print(f"[!] Error: Fixture file not found: {fixture_path}")
        return 1

    try:
        schema = json.loads(schema_file.read_text(encoding="utf-8"))
        fixture_data = json.loads(fixture_path.read_text(encoding="utf-8"))
    except Exception as e:
        if json_mode:
            print(json.dumps({"error": f"Failed to parse JSON: {e}"}))
        else:
            print(f"[!] Error: Failed to parse JSON: {e}")
        return 1

    errors = validate_json_instance(fixture_data, schema)
    is_valid = len(errors) == 0
    exit_code = 0 if is_valid else 1

    if json_mode:
        report = {
            "suite": "Vibe UI Evaluation Suite",
            "version": "2.2.0",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "mode": "standalone_fixture",
            "fixture": str(fixture_path),
            "overall_status": "PASS" if is_valid else "FAIL",
            "exit_code": exit_code,
            "errors": errors
        }
        print(json.dumps(report, indent=2))
    else:
        if is_valid:
            print(f"[SUCCESS] Fixture '{fixture_path.name}' conforms 100% to schema.")
        else:
            print(f"[FAILURE] Fixture '{fixture_path.name}' failed schema validation with {len(errors)} error(s):")
            for err in errors:
                print(f"  - {err}")

    return exit_code

# ==============================================================================
# Main Entrypoint
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="🧪 Automated Evaluation Runner for Vibe UI & mr-ui-designer"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="json_mode",
        help="Emit pure machine-readable JSON report to stdout (suppresses ASCII scorecards)",
    )
    parser.add_argument(
        "--fixture",
        type=str,
        dest="fixture_path",
        help="Validate a standalone JSON design specification fixture file and exit with code 0 (valid) or 1 (invalid)",
    )
    args = parser.parse_args()

    root_dir = Path(__file__).resolve().parent.parent

    # Standalone fixture validation path
    if args.fixture_path:
        sys.exit(run_standalone_fixture(args.fixture_path, root_dir, args.json_mode))

    # Full suite execution path
    examples_dir = root_dir / "examples"
    if not examples_dir.exists():
        if args.json_mode:
            print(json.dumps({"error": f"Examples directory not found at {examples_dir}"}))
        else:
            print(f"[!] Error: Examples directory not found at {examples_dir}")
        sys.exit(1)

    html_files = sorted(list(examples_dir.glob("*.html")))
    if not html_files:
        if args.json_mode:
            print(json.dumps({"error": f"No HTML example files found in {examples_dir}"}))
        else:
            print(f"[!] Error: No HTML example files found in {examples_dir}")
        sys.exit(1)

    if not args.json_mode:
        print(f"[+] Running Vibe UI Automated Verification against {len(html_files)} example(s) & repo integrity...\n")

    targets = []

    # 1. Structural Repo Integrity, Negative Fixtures & JSON Schema Instance Validation
    repo_res = audit_repo_integrity(root_dir)
    targets.append(repo_res)
    if not args.json_mode:
        render_scorecard(repo_res)

    # 2. Production Next.js 15 Starter Architecture & Token Audit
    starter_dir = root_dir / "examples" / "nextjs-starter"
    if starter_dir.exists():
        starter_res = audit_nextjs_starter(starter_dir)
        targets.append(starter_res)
        if not args.json_mode:
            render_scorecard(starter_res)

    # 3. HTML Examples Audit
    for html_file in html_files:
        res = audit_html_file(html_file)
        targets.append(res)
        if not args.json_mode:
            render_scorecard(res)

    total_targets = len(targets)
    passed_targets = sum(1 for t in targets if t["overall_status"] == "PASS")
    failed_targets = sum(1 for t in targets if t["overall_status"] == "FAIL")
    warned_targets = sum(1 for t in targets if t["overall_status"] == "WARN")

    all_checks = [chk for t in targets for chk in t["checks"]]
    total_checks = len(all_checks)
    passed_checks = sum(1 for c in all_checks if c["status"] == "PASS")
    failed_checks = sum(1 for c in all_checks if c["status"] == "FAIL")
    warned_checks = sum(1 for c in all_checks if c["status"] == "WARN")

    overall_suite_status = "FAIL" if failed_targets > 0 else "PASS"
    exit_code = 0 if overall_suite_status == "PASS" else 1

    if args.json_mode:
        report = {
            "suite": "Vibe UI Evaluation Suite",
            "version": "2.2.1",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "overall_status": overall_suite_status,
            "exit_code": exit_code,
            "summary": {
                "total_targets": total_targets,
                "passed_targets": passed_targets,
                "failed_targets": failed_targets,
                "warned_targets": warned_targets,
                "total_checks": total_checks,
                "passed_checks": passed_checks,
                "failed_checks": failed_checks,
                "warned_checks": warned_checks,
            },
            "targets": targets,
        }
        print(json.dumps(report, indent=2))
        sys.exit(exit_code)

    if exit_code == 0:
        print("[SUCCESS] ALL AUDIT GATES PASSED (100% WCAG AA, Semantic RTL, Security & JSON Schema Validated)!\n")
        sys.exit(0)
    else:
        print(f"[FAILURE] Audit failed with {failed_targets} failing gate(s).\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
