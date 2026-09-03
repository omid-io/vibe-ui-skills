"""
vibe_core.director — Design Director Module
Autonomous intent extraction, domain matching, confidence estimation, and VoI protocol.
"""

import json
import re
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"

def normalize_text(text: str) -> str:
    """Normalizes Persian and English text for robust semantic matching."""
    if not text:
        return ""
    text = text.strip().lower()
    # Normalize Arabic/Persian characters
    text = text.replace("ي", "ی").replace("ك", "ک").replace("ة", "ه").replace("‌", " ")
    # Remove punctuation
    text = re.sub(r"[^\w\s\u0600-\u06FF]", " ", text)
    return " ".join(text.split())

class DesignDirector:
    def __init__(self, data_dir: Optional[Path] = None):
        self.data_dir = data_dir or DATA_DIR
        self.taxonomy = self._load_taxonomy()

    def _load_taxonomy(self) -> List[Dict[str, Any]]:
        tax_path = self.data_dir / "taxonomy.json"
        if not tax_path.exists():
            return []
        with open(tax_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("domains", [])

    def infer_intent(self, prompt: str, user_overrides: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Infers DesignIntentContract from natural language user prompt.
        """
        norm_prompt = normalize_text(prompt)
        user_overrides = user_overrides or {}

        matched_domain, confidence_score, match_reasons = self._match_domain(norm_prompt)
        
        # Determine product mode
        detected_mode = self._detect_product_mode(norm_prompt, matched_domain)

        # Ambiguity determination
        if confidence_score >= 0.80:
            ambiguity_status = "low_ambiguity"
            clarification_needed = False
            candidate_directions = []
        elif confidence_score >= 0.50:
            ambiguity_status = "medium_ambiguity"
            clarification_needed = False
            candidate_directions = self._generate_candidate_directions(matched_domain)
        else:
            ambiguity_status = "high_ambiguity"
            clarification_needed = True
            candidate_directions = self._generate_candidate_directions(matched_domain)

        # Language detection
        has_persian = bool(re.search(r"[\u0600-\u06FF]", prompt))
        language = ["fa", "en"] if has_persian else ["en"]

        # Hard constraints extraction
        hard_constraints = [
            "WCAG AA contrast >= 4.5:1",
            "Zero horizontal overflow on 320px/375px",
            "Touch targets >= 44px"
        ]
        if has_persian:
            hard_constraints.append("RTL punctuation isolation (<bdi> / unicode-bidi)")
            hard_constraints.append("Vazirmatn web font integration")

        # Construct DesignIntentContract
        intent = {
            "product_domain": user_overrides.get("product_domain") or matched_domain["id"],
            "audience": {
                "type": matched_domain.get("name_en", "General Audience"),
                "technical_level": "expert" if "terminal" in matched_domain["id"] or "devops" in matched_domain["id"] else "general",
                "primary_device": "mobile" if matched_domain.get("density") == "airy" else "cross_platform"
            },
            "product_mode": user_overrides.get("product_mode") or detected_mode,
            "business_goal": f"Deliver high-conversion and high-trust experience for {matched_domain['name_en']}",
            "visual_energy": matched_domain.get("visual_energy", "calm_restrained"),
            "density": user_overrides.get("density") or matched_domain.get("density", "balanced"),
            "platform": ["mobile", "tablet", "desktop"],
            "language": language,
            "confidence": {
                "overall": confidence_score,
                "domain": confidence_score,
                "audience": 0.85,
                "product_mode": 0.90
            },
            "ambiguity_status": ambiguity_status,
            "clarification_needed": clarification_needed,
            "candidate_directions": candidate_directions,
            "hard_constraints": hard_constraints,
            "soft_preferences": [
                f"Prioritize {matched_domain.get('visual_energy', 'calm')} aesthetic",
                f"Recommended style family: {matched_domain.get('recommended_styles', ['clean_stripe'])[0]}"
            ],
            "provenance": {
                "product_domain": "user_explicit" if "product_domain" in user_overrides else "inferred",
                "product_mode": "user_explicit" if "product_mode" in user_overrides else "inferred",
                "confidence": "system_policy"
            }
        }
        return intent

    def _match_domain(self, text: str) -> Tuple[Dict[str, Any], float, List[str]]:
        """Matches normalized prompt text against taxonomy aliases."""
        best_domain = None
        best_score = 0.0
        reasons = []

        tokens = set(text.split())

        for domain in self.taxonomy:
            domain_score = 0.0
            matched_aliases = []

            # Exact ID / Name match
            if domain["id"].replace("_", " ") in text:
                domain_score += 0.95
                matched_aliases.append(domain["id"])

            # Alias matching
            for alias in domain.get("aliases", []):
                norm_alias = normalize_text(alias)
                if norm_alias in text:
                    domain_score += 0.45
                    matched_aliases.append(alias)
                elif set(norm_alias.split()).issubset(tokens):
                    domain_score += 0.35
                    matched_aliases.append(alias)

            # Cap score to 0.98 max for non-exact overrides
            domain_score = min(0.98, domain_score)

            if domain_score > best_score:
                best_score = domain_score
                best_domain = domain
                reasons = matched_aliases

        if not best_domain or best_score < 0.30:
            # Fallback to general_modern_saas with honest zero/actual match score
            fallback = next((d for d in self.taxonomy if d["id"] == "general_modern_saas"), self.taxonomy[0] if self.taxonomy else {})
            actual_score = round(best_score, 2) if best_domain else 0.0
            return fallback, actual_score, ["fallback_general_modern_saas", "no_matching_taxonomy"]

        return best_domain, best_score, reasons

    def _detect_product_mode(self, text: str, domain: Dict[str, Any]) -> str:
        """Determines product mode from keywords or domain primary mode."""
        operate_keywords = ["dashboard", "داشبورد", "پنل", "panel", "admin", "ادمین", "ترید", "trading", "console", "مدیریت", "orderbook"]
        read_keywords = ["doc", "docs", "مستندات", "مقاله", "blog", "وبلاگ", "آموزش", "learning", "article"]
        experience_keywords = ["portfolio", "نمونه کار", "showcase", "game", "بازی", "event", "creative"]

        for kw in operate_keywords:
            if kw in text:
                return "operate"
        for kw in read_keywords:
            if kw in text:
                return "read"
        for kw in experience_keywords:
            if kw in text:
                return "experience"

        return domain.get("primary_mode", "persuade")

    def _generate_candidate_directions(self, domain: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generates 3 human-readable directions under medium/high ambiguity."""
        styles = domain.get("recommended_styles", ["clean_stripe", "minimal_swiss", "quiet_luxury"])
        candidates = []
        labels = [
            ("A (Recommended)", "Editorial Prestige & Calm Restraint", "Focuses on high trust and understated elegance"),
            ("B", "Crisp Corporate & Structured SaaS", "Focuses on clarity, metrics, and conversion speed"),
            ("C", "Approachable Humanist & Friendly Warmth", "Focuses on warmth, empathy, and accessibility")
        ]
        for i, style in enumerate(styles[:3]):
            lbl, title, desc = labels[i]
            candidates.append({
                "id": style,
                "label": f"{lbl}: {title}",
                "description": desc,
                "tradeoff": f"Applies {style} visual geometry with optimized domain priors."
            })
        return candidates
