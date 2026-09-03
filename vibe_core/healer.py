"""
vibe_core.healer — Self-Healing Agent Loop
Transforms Critic defect reports into structured Correction Prompts that AI agents can
consume to self-correct generated interfaces without requiring manual iteration.

Architecture:
  1. SelfHealingLoop.build_correction_prompt() → Converts CriticReport defects to a
     machine-readable, LLM-consumable prompt block.
  2. SelfHealingLoop.heal() → Runs bounded static-refine + correction-prompt generation
     loop, returning the best achievable HTML and a correction prompt for any residual issues.

The Self-Healing Loop is the architectural bridge missing from v3.0.0:
  Critic (detects) → Refiner (patches statically) → Healer (generates AI correction prompt)
"""

from __future__ import annotations

from typing import Dict, Any, List, Optional, Tuple
from vibe_core.critic import DesignCritic
from vibe_core.refiner import AutoRefiner

# Severity → priority weight for ordering correction instructions
_SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}


class SelfHealingLoop:
    """
    Bridges the gap between static patching (AutoRefiner) and LLM-driven correction.

    Usage:
        healer = SelfHealingLoop()
        final_html, final_report, correction_prompt = healer.heal(html, decision)
        if correction_prompt:
            # Feed correction_prompt back to the generating LLM for next iteration
            print(correction_prompt)
    """

    def __init__(self) -> None:
        self._critic = DesignCritic()
        self._refiner = AutoRefiner()

    # ─────────────────── Public API ───────────────────

    def build_correction_prompt(
        self,
        critique_report: Dict[str, Any],
        original_prompt: str = "",
        max_defects: int = 5,
    ) -> str:
        """
        Converts a CriticReport into a structured Correction Prompt for LLM consumption.

        The prompt follows the format:
            [VIBE-UI CORRECTION REQUEST]
            Your previous code failed verification. Here are the exact errors and required patches:
            1. [CRITICAL] <message> → Patch: <suggested_patch>
            ...
            Rewrite the component applying ONLY these fixes. Do not change anything else.

        Args:
            critique_report: Output dict from DesignCritic.critique().
            original_prompt:  The original user prompt (included for context).
            max_defects:      Maximum defects to include (avoids context bloat).

        Returns:
            A formatted string ready to be injected into an LLM conversation.
            Returns empty string if there are no defects (all clear).
        """
        defects: List[Dict[str, Any]] = critique_report.get("defects_ranked", [])
        hard_failures: List[Dict[str, Any]] = critique_report.get("hard_gate_failures", [])
        acceptance = critique_report.get("acceptance_status", "ACCEPTED")

        if acceptance == "ACCEPTED" and not defects:
            return ""

        # Sort defects by severity
        sorted_defects = sorted(
            defects,
            key=lambda d: _SEVERITY_ORDER.get(d.get("severity", "low"), 4)
        )[:max_defects]

        lines: List[str] = [
            "[VIBE-UI CORRECTION REQUEST]",
            f"Status: {acceptance} | Score: {critique_report.get('quality_score', 0)}/100",
        ]

        if original_prompt:
            lines.append(f"Original task: {original_prompt}")

        lines.append("")

        if hard_failures:
            lines.append("⛔ HARD GATE FAILURES (must fix before acceptance):")
            for hf in hard_failures:
                lines.append(f"  • [{hf.get('gate', 'Unknown Gate')}] {hf.get('message', '')}")
            lines.append("")

        if sorted_defects:
            lines.append("🔧 REQUIRED PATCHES (apply in order):")
            for i, defect in enumerate(sorted_defects, 1):
                severity = defect.get("severity", "low").upper()
                message = defect.get("message", "")
                patch = defect.get("suggested_patch", "No patch specified")
                lines.append(f"  {i}. [{severity}] {message}")
                lines.append(f"     → Patch: {patch}")
            lines.append("")

        lines += [
            "Instructions:",
            "  • Rewrite the component applying ONLY the patches listed above.",
            "  • Do not change visual layout, color palette, or content that is not mentioned.",
            "  • Return the complete corrected HTML/component, no partial snippets.",
            "[END CORRECTION REQUEST]",
        ]

        return "\n".join(lines)

    def heal(
        self,
        html_content: str,
        decision: Optional[Dict[str, Any]] = None,
        original_prompt: str = "",
        max_rounds: int = 2,
    ) -> Tuple[str, Dict[str, Any], str]:
        """
        Runs a bounded heal loop:
          1. First applies AutoRefiner (static surgical patches, max 2 iters).
          2. If still not ACCEPTED, generates a Correction Prompt for the residual issues.

        Args:
            html_content:    Raw HTML to heal.
            decision:        DesignDecisionContract from RecommendationEngine.
            original_prompt: The user's original design prompt (for context in correction prompt).
            max_rounds:      Max AutoRefiner rounds (default 2, matching refiner contract).

        Returns:
            (final_html, final_critique_report, correction_prompt_str)
            correction_prompt_str is "" if the artifact is ACCEPTED.
        """
        decision = decision or {}

        # Phase 1: Static surgical patching via AutoRefiner
        refined_html, final_report = self._refiner.refine(
            html_content, decision, max_iterations=max_rounds
        )

        # Phase 2: If still not ACCEPTED, build a correction prompt for LLM
        correction_prompt = ""
        if final_report.get("acceptance_status") != "ACCEPTED":
            correction_prompt = self.build_correction_prompt(final_report, original_prompt)

        return refined_html, final_report, correction_prompt

    def format_heal_summary(self, final_report: Dict[str, Any], correction_prompt: str) -> str:
        """Returns a human-readable terminal summary of the heal result."""
        status = final_report.get("acceptance_status", "UNKNOWN")
        score = final_report.get("quality_score", 0)
        gates_pass = final_report.get("hard_gates_pass", False)

        lines = [
            f"  ┌─ Heal Result ──────────────────────",
            f"  │  Status : {status}",
            f"  │  Score  : {score}/100",
            f"  │  Gates  : {'✓ All passed' if gates_pass else '✗ Gate failures present'}",
        ]

        if correction_prompt:
            lines += [
                f"  │  Action : Correction prompt generated ({len(correction_prompt)} chars)",
                f"  │           Feed back to AI agent for next iteration.",
            ]
        else:
            lines.append("  │  Action : No further action required.")

        lines.append("  └────────────────────────────────────")
        return "\n".join(lines)
