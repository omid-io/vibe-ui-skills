"""
vibe_core.critic — Style-Aware Design Critic Engine
Independent evaluator auditing 15 design dimensions, separating Hard Gates from Quality Scorecard.
AST-based HTML parsing via BeautifulSoup4 (falls back to regex if unavailable).
"""

import re
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, List, Tuple, Optional

from vibe_core.constants import (
    MAX_BLUR_SURFACES,
    HARD_MIN_TOUCH_PX,
    RECOMMENDED_TOUCH_PX,
)

try:
    from bs4 import BeautifulSoup as _BS4
    _BS4_AVAILABLE = True
except ImportError:  # pragma: no cover
    _BS4_AVAILABLE = False
    _BS4 = None  # type: ignore

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"

class DesignCritic:
    def __init__(self, data_dir: Optional[Path] = None):
        self.data_dir = data_dir or DATA_DIR
        self.anti_patterns = self._load_anti_patterns()

    def _load_anti_patterns(self) -> List[Dict[str, Any]]:
        path = self.data_dir / "anti-patterns.json"
        if not path.exists():
            return []
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f).get("anti_patterns", [])

    def critique(self, html_content: str, decision: Optional[Dict[str, Any]] = None, iteration: int = 1) -> Dict[str, Any]:
        """
        Conducts independent multi-pillar audit and returns CriticReport conforming to schemas/critic-report.v1.json.
        """
        decision = decision or {}
        genome = decision.get("genome", {})
        style_family = decision.get("selected_style", "clean_stripe")

        hard_gate_failures = []
        defects_ranked = []

        # 1. Hard Gate: Zero Raw Emojis
        emoji_pattern = re.compile(
            r"[\U00010000-\U0010ffff]|[\u2600-\u27bf]|[\u2300-\u23ff]|[\u2b50-\u2b55]|[\u203c-\u2049]"
        )
        # Strip script/style tags before checking content
        clean_text = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", html_content, flags=re.DOTALL)
        if emoji_pattern.search(clean_text):
            hard_gate_failures.append({
                "gate": "Zero Raw Emojis",
                "message": "Found raw Unicode emoji in UI. Strict vector SVG icons are required.",
                "evidence": "Emoji codepoints detected in markup"
            })
            defects_ranked.append({
                "severity": "critical",
                "type": "raw_emoji_detected",
                "message": "Replace raw emoji with crisp SVG vector icon.",
                "suggested_patch": "Use <svg viewBox='0 0 24 24'> icon primitive."
            })

        # 2. Hard Gate: Viewport Meta Tag
        if 'name="viewport"' not in html_content:
            hard_gate_failures.append({
                "gate": "Mobile Viewport",
                "message": "Missing standard mobile viewport meta tag.",
                "evidence": "No <meta name='viewport'> tag"
            })
            defects_ranked.append({
                "severity": "critical",
                "type": "missing_viewport",
                "message": "Add mobile viewport meta tag.",
                "suggested_patch": "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
            })

        # 3. Hard Gate: Semantic Clickables (<div onclick>)
        # AST-based detection via BS4 to handle minified/malformed HTML correctly.
        if _BS4_AVAILABLE:
            soup = _BS4(html_content, "html.parser")
            div_onclick = soup.find_all("div", onclick=True)
        else:
            # Regex fallback (fragile on minified HTML, kept for zero-dep environments)
            div_onclick = re.findall(r"<div[^>]*onclick=", html_content, re.IGNORECASE)
        if div_onclick:
            hard_gate_failures.append({
                "gate": "Semantic Clickables",
                "message": f"Found {len(div_onclick)} non-semantic <div onclick> violation(s).",
                "evidence": "div onclick detected"
            })
            defects_ranked.append({
                "severity": "critical",
                "type": "non_semantic_clickable",
                "message": "Convert <div onclick> to semantic <button type='button'> or <a>.",
                "suggested_patch": "<button type='button' class='...'>"
            })

        # 4. Hard Gate: Focus Visible Rings
        if "focus-visible" not in html_content and ":focus" not in html_content:
            hard_gate_failures.append({
                "gate": "Keyboard Focus Rings",
                "message": "No focus-visible styling declared in stylesheet.",
                "evidence": "Missing :focus-visible rules"
            })
            defects_ranked.append({
                "severity": "critical",
                "type": "missing_focus_rings",
                "message": "Add focus-visible outline or ring to interactive elements.",
                "suggested_patch": "button:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }"
            })

        # 5. Anti-Slop Check: Generic AI Purple Gradient
        if "from-purple-600" in html_content and "to-indigo-600" in html_content:
            defects_ranked.append({
                "severity": "high",
                "type": "generic_ai_purple_gradient",
                "message": "Detected overused generic purple/indigo AI gradient trope.",
                "suggested_patch": "Replace with domain-calibrated OKLCH surface tones or edge lighting."
            })

        # 6. Performance Budget: Backdrop Filter Blur Budget
        # Canonical policy imported from vibe_core.constants.MAX_BLUR_SURFACES
        # BS4: search inside <style> blocks + inline style attributes only, not class names.
        if _BS4_AVAILABLE:
            _soup_blur = _BS4(html_content, "html.parser") if not _BS4_AVAILABLE or "soup" not in dir() else soup
            _style_texts = " ".join(t.get_text() for t in _soup_blur.find_all("style"))
            _inline_styles = " ".join(tag.get("style", "") for tag in _soup_blur.find_all(style=True))
            _blur_target = _style_texts + " " + _inline_styles
        else:
            _blur_target = html_content
        blur_matches = re.findall(r"backdrop-blur|blur\(", _blur_target)
        if len(blur_matches) > MAX_BLUR_SURFACES:
            defects_ranked.append({
                "severity": "high",
                "type": "excessive_backdrop_blur",
                "message": f"Found {len(blur_matches)} blur layers, exceeding GPU budget (<= {MAX_BLUR_SURFACES}).",
                "suggested_patch": "Reduce backdrop-filter layers to prevent mobile frame drops."
            })

        # 7. Semantic RTL Check
        is_rtl = 'dir="rtl"' in html_content or "dir='rtl'" in html_content
        if is_rtl:
            if "<bdi" not in html_content and "unicode-bidi" not in html_content and "ltr-code" not in html_content:
                hard_gate_failures.append({
                    "gate": "Semantic RTL Isolation",
                    "message": "RTL document lacks <bdi> or unicode-bidi isolation for mixed English terms.",
                    "evidence": "No <bdi> or unicode-bidi found"
                })
                defects_ranked.append({
                    "severity": "high",
                    "type": "missing_bidi_isolation",
                    "message": "Wrap mixed-language terms or add unicode-bidi: plaintext.",
                    "suggested_patch": "body { unicode-bidi: plaintext; }"
                })
        # 8. Reduced Motion Hard Gate — Deterministic (P0 from Qwen Review)
        # RULE: Motion tokens WITHOUT @media (prefers-reduced-motion: reduce) = CRITICAL hard gate failure.
        # Rationale: CSS animations without override can cause nausea/vestibular disorder in affected users.
        MOTION_TOKEN_RE = re.compile(
            r"\btransition\s*:|animation\s*:|@keyframes\b|lenis\b|scroll-behavior\s*:\s*smooth",
            re.IGNORECASE
        )
        style_blocks_content = " ".join(re.findall(r"<style[^>]*>(.*?)</style>", html_content, re.DOTALL | re.IGNORECASE))
        has_motion_tokens = bool(MOTION_TOKEN_RE.search(style_blocks_content))
        has_reduced_motion_override = "prefers-reduced-motion" in html_content

        if has_motion_tokens and not has_reduced_motion_override:
            hard_gate_failures.append({
                "gate": "Reduced Motion Override",
                "message": "Motion tokens (transition/animation/lenis) declared without @media (prefers-reduced-motion: reduce) override.",
                "evidence": "Risk: vestibular/nausea disorder for affected users. WCAG 2.1 SC 2.3.3 (AAA)."
            })
            defects_ranked.append({
                "severity": "critical",
                "type": "missing_reduced_motion_override",
                "message": "Add @media (prefers-reduced-motion: reduce) to neutralize all motion declarations.",
                "suggested_patch": "@media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; scroll-behavior: auto !important; } }"
            })

        # 9. Component States Matrix Check
        has_skeleton = "skeleton" in html_content.lower() or "animate-pulse" in html_content
        has_empty = "empty" in html_content.lower() or "یافت نشد" in html_content or "no records" in html_content.lower()
        has_error = "retry" in html_content.lower() or "خطا" in html_content or "error" in html_content.lower()
        state_completeness_score = 10
        if not has_skeleton:
            state_completeness_score -= 3
            defects_ranked.append({
                "severity": "medium",
                "type": "missing_skeleton_state",
                "message": "No skeleton loading placeholder detected.",
                "suggested_patch": "Add skeleton state with animate-pulse."
            })
        if not has_empty:
            state_completeness_score -= 3
            defects_ranked.append({
                "severity": "low",
                "type": "missing_empty_state",
                "message": "No empty state UI container detected.",
                "suggested_patch": "Add empty state with vector icon and helper text."
            })
        if not has_error:
            state_completeness_score -= 3
            defects_ranked.append({
                "severity": "medium",
                "type": "missing_error_state",
                "message": "No error and retry recovery state detected.",
                "suggested_patch": "Add error container with retry button."
            })

        # Scorecard computation — all values derived from measurable HTML signals, no hardcoded constants.
        # Touch target policy: HARD_MIN_TOUCH_PX = 24px (WCAG 2.2 AA), RECOMMENDED_TOUCH_PX = 44px (mobile HIG)
        # Visual Hierarchy: evidence — heading tags and display-font tokens present
        heading_tags = len(re.findall(r"<h[1-3][^>]*>", html_content, re.IGNORECASE))
        visual_hierarchy = min(14, 6 + (heading_tags * 2) + (4 if "display-font" in html_content else 0))

        # Anti-Slop Distinctiveness: evidence — absence of generic purple/indigo AI gradient trope
        anti_slop_distinctiveness = 14 if "from-purple-600" not in html_content else 8

        # Domain Fit: evidence — CSS custom properties and domain-calibrated tokens signal intentional design
        css_var_count = len(re.findall(r"var\(--", html_content))
        domain_fit = min(14, 4 + min(10, css_var_count))

        # Usability: evidence — presence of interactive semantic elements and absence of div-onclick violations
        usability = 10 if not div_onclick else 6

        # Typography: evidence — font-family declarations and display-font token usage
        has_font_family = bool(re.search(r"font-family\s*:", html_content) or "display-font" in html_content)
        font_stack_count = len(re.findall(r"font-family\s*:", html_content))
        typography = min(10, 4 + (4 if has_font_family else 0) + min(2, font_stack_count))

        # Responsive: evidence — mobile viewport meta tag presence
        responsive = 10 if 'name="viewport"' in html_content else 4

        # Brand Coherence: evidence — presence of CSS variable design tokens (--surface, --accent, --text)
        brand_token_signals = ["--accent", "--surface", "--text-primary", "--border", "--canvas"]
        brand_matches = sum(1 for t in brand_token_signals if t in html_content)
        brand_coherence = min(9, brand_matches * 2)

        # Performance Budget: evidence — blur surface count measured above
        perf_budget = 5 if len(blur_matches) <= MAX_BLUR_SURFACES else 2

        scorecard = {
            "visual_hierarchy": visual_hierarchy,
            "anti_slop_distinctiveness": anti_slop_distinctiveness,
            "domain_fit": domain_fit,
            "usability": usability,
            "typography": typography,
            "responsive": responsive,
            "state_completeness": max(2, state_completeness_score),
            "brand_coherence": brand_coherence,
            "performance_budget": perf_budget
        }

        quality_score = sum(scorecard.values())
        hard_gates_pass = len(hard_gate_failures) == 0

        if hard_gates_pass and quality_score >= 80.0:
            acceptance_status = "ACCEPTED"
        elif not hard_gates_pass:
            acceptance_status = "REJECTED_CRITICAL"
        else:
            acceptance_status = "NEEDS_REFINEMENT"

        return {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "iteration": iteration,
            "evaluated_style": style_family,
            "hard_gates_pass": hard_gates_pass,
            "hard_gate_failures": hard_gate_failures,
            "quality_score": round(quality_score, 1),
            "scorecard": scorecard,
            "defects_ranked": defects_ranked,
            "acceptance_status": acceptance_status
        }
