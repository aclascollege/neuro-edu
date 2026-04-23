"""
Five-dimensional skill matrix for cognitive agent profiling.
Dimensions: Logic, Math, Language, Memory, Creative
"""
import numpy as np
from typing import Dict


SKILL_DIMS = ["logic", "math", "language", "memory", "creative"]

PROFILES = {
    "balanced":      {"logic": 0.55, "math": 0.50, "language": 0.55, "memory": 0.50, "creative": 0.50},
    "math_genius":   {"logic": 0.85, "math": 0.92, "language": 0.30, "memory": 0.65, "creative": 0.25},
    "linguist":      {"logic": 0.40, "math": 0.20, "language": 0.92, "memory": 0.75, "creative": 0.60},
    "creative_soul": {"logic": 0.35, "math": 0.15, "language": 0.65, "memory": 0.40, "creative": 0.95},
    "memorizer":     {"logic": 0.50, "math": 0.45, "language": 0.55, "memory": 0.92, "creative": 0.30},
    "polymath":      {"logic": 0.80, "math": 0.78, "language": 0.75, "memory": 0.70, "creative": 0.72},
}


class SkillMatrix:
    def __init__(self, profile: str = "balanced"):
        base = PROFILES.get(profile, PROFILES["balanced"]).copy()
        # Add small individual variation
        self.skills: Dict[str, float] = {
            k: round(float(np.clip(v + np.random.normal(0, 0.05), 0.05, 1.0)), 3)
            for k, v in base.items()
        }
        self.profile = profile

    def match_content(self, content_skills: Dict[str, float]) -> float:
        """
        Compute weighted skill-match score between content requirements and agent profile.
        Returns value in [0, 1].
        """
        if not content_skills:
            return 0.5
        score = 0.0
        total_weight = 0.0
        for dim, weight in content_skills.items():
            if dim in self.skills:
                score += self.skills[dim] * weight
                total_weight += weight
        return round(score / total_weight if total_weight > 0 else 0.5, 4)

    def dominant_skill(self) -> str:
        return max(self.skills, key=self.skills.get)

    def to_dict(self) -> Dict[str, float]:
        return self.skills.copy()

    def to_vector(self) -> np.ndarray:
        return np.array([self.skills[k] for k in SKILL_DIMS])
