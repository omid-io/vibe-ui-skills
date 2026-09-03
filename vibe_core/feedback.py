"""
vibe_core.feedback — Continuous Design Intelligence Feedback Collector
Records user acceptance, correction metrics, and calibration data for continuous tuning.
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional

ROOT_DIR = Path(__file__).resolve().parent.parent
FEEDBACK_FILE = ROOT_DIR / "data" / "feedback_ledger.json"

class FeedbackCollector:
    def __init__(self, file_path: Optional[Path] = None):
        self.file_path = file_path or FEEDBACK_FILE

    def record_feedback(self, decision_id: str, accepted: bool, rating: float = 5.0, notes: str = "", corrections: int = 0) -> Dict[str, Any]:
        """Appends a feedback entry to the durable ledger."""
        entry = {
            "decision_id": decision_id,
            "user_accepted": accepted,
            "corrections_made": corrections,
            "user_rating": rating,
            "user_notes": notes,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }

        records = []
        if self.file_path.exists():
            try:
                with open(self.file_path, "r", encoding="utf-8") as f:
                    records = json.load(f)
            except Exception:
                records = []

        records.append(entry)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(records, f, indent=2, ensure_ascii=False)

        return entry
