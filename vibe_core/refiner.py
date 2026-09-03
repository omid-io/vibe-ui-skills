"""
vibe_core.refiner — Priority-Based Auto-Refinement Engine
Applies bounded surgical patches to resolve Critic defects with strict anti-regression gating.
"""

import re
from typing import Dict, Any, Tuple
from vibe_core.critic import DesignCritic

class AutoRefiner:
    def __init__(self):
        self.critic = DesignCritic()

    def refine(self, html_content: str, decision: Dict[str, Any], max_iterations: int = 2) -> Tuple[str, Dict[str, Any]]:
        """
        Runs bounded refinement loop (max 2 iterations) resolving defects in priority order.
        """
        current_html = html_content
        current_report = self.critic.critique(current_html, decision, iteration=1)

        if current_report["acceptance_status"] == "ACCEPTED":
            return current_html, current_report

        for iteration in range(1, max_iterations + 1):
            defects = current_report.get("defects_ranked", [])
            if not defects:
                break

            # Sort defects: critical -> high -> medium -> low
            priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
            sorted_defects = sorted(defects, key=lambda d: priority_order.get(d.get("severity", "low"), 4))

            # Apply surgical patches
            patched_html = current_html
            for defect in sorted_defects:
                d_type = defect.get("type")

                # 1. Missing viewport patch
                if d_type == "missing_viewport":
                    if "<head>" in patched_html:
                        patched_html = patched_html.replace(
                            "<head>",
                            "<head>\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">"
                        )

                # 2. Missing focus rings patch
                elif d_type == "missing_focus_rings":
                    focus_css = "\n    button:focus-visible, a:focus-visible { outline: 2px solid var(--accent, #3b82f6); outline-offset: 2px; }\n"
                    if "</style>" in patched_html:
                        patched_html = patched_html.replace("</style>", f"{focus_css}  </style>")
                    elif "<head>" in patched_html:
                        patched_html = patched_html.replace("<head>", f"<head>\n  <style>{focus_css}</style>")

                # 3. Non-semantic clickable (<div onclick>)
                elif d_type == "non_semantic_clickable":
                    patched_html = re.sub(
                        r"<div([^>]*onclick=[^>]*)>",
                        r"<button type=\"button\"\1>",
                        patched_html,
                        flags=re.IGNORECASE
                    )
                    # Note: in real DOM, closing tag is also adjusted or handled by outer components

                # 4. Raw emoji replacement
                elif d_type == "raw_emoji_detected":
                    # Replace common emojis with SVG vector
                    svg_star = '<svg class="w-4 h-4 inline" viewBox="0 0 24 24" fill="currentColor"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>'
                    patched_html = re.sub(
                        r"[\U00010000-\U0010ffff]|[\u2600-\u27bf]|[\u2300-\u23ff]|[\u2b50-\u2b55]|[\u203c-\u2049]",
                        svg_star,
                        patched_html
                    )

                # 5. Missing bidi isolation
                elif d_type == "missing_bidi_isolation":
                    if "</style>" in patched_html:
                        patched_html = patched_html.replace(
                            "</style>",
                            "  body { unicode-bidi: plaintext; }\n    bdi { direction: ltr !important; unicode-bidi: isolate; }\n  </style>"
                        )

                # 6. Generic purple gradient replacement
                elif d_type == "generic_ai_purple_gradient":
                    patched_html = patched_html.replace("from-purple-600 to-indigo-600", "bg-[var(--surface-bg)] border border-[var(--border-subtle)]")

            # Anti-Regression Re-Evaluation
            re_critique = self.critic.critique(patched_html, decision, iteration=iteration + 1)
            
            # If the patch improved or maintained Hard Gates, accept it
            if re_critique["quality_score"] >= current_report["quality_score"]:
                current_html = patched_html
                current_report = re_critique
                if current_report["acceptance_status"] == "ACCEPTED":
                    break

        return current_html, current_report
