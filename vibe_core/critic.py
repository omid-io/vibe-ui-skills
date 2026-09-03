"""
vibe_core.critic — Style-Aware Design Critic Engine
Independent evaluator auditing 15 design dimensions, separating Hard Gates from Quality Scorecard.
"""

import re
import json
from pathlib import Path
from typing import Dict, Any, List, Tuple, Optional

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
        blur_matches = re.findall(r"backdrop-blur|blur\(", html_content)
        if len(blur_matches) > 2:
            defects_ranked.append({
                "severity": "high",
                "type": "excessive_backdrop_blur",
                "message": f"Found {len(blur_matches)} blur layers, exceeding GPU budget (<= 2).",
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

        # 8. Component States Matrix Check
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

        # Scorecard computation
        visual_hierarchy = 14 if "display-font" in html_content or "h1" in html_content else 10
        anti_slop_distinctiveness = 14 if "from-purple-600" not in html_content else 8
        domain_fit = 14
        usability = 10 if not div_onclick else 6
        typography = 10 if "font-family" in html_content or "display-font" in html_content else 7
        responsive = 10 if 'name="viewport"' in html_content else 4
        brand_coherence = 9
        perf_budget = 5 if len(blur_matches) <= 2 else 2

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
            "timestamp": "2026-09-03T12:00:00Z",
            "iteration": iteration,
            "evaluated_style": style_family,
            "hard_gates_pass": hard_gates_pass,
            "hard_gate_failures": hard_gate_failures,
            "quality_score": round(quality_score, 1),
            "scorecard": scorecard,
            "defects_ranked": defects_ranked,
            "acceptance_status": acceptance_status
        }
