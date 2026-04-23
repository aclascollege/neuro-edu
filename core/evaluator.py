"""
Multi-dimensional cognitive performance evaluator.
Produces GPA, CAS Score, Retention Rate, Diversity Index, and Dropout Risk.
"""
import numpy as np
from typing import List, Dict, Any


class CognitiveEvaluator:
    """
    The ACLAS Evaluation Framework.
    All metrics are grounded in educational psychology literature.
    """

    @staticmethod
    def compute_gpa(agents: List) -> float:
        """
        GPA on a 4.0 scale.
        Weighted: knowledge_pool depth (50%) + attention stability (30%) + prior_knowledge (20%)
        """
        if not agents:
            return 0.0
        scores = []
        for a in agents:
            knowledge_score = min(1.0, len(a.knowledge_pool) * 0.08)
            score = knowledge_score * 0.5 + a.attention * 0.3 + a.prior_knowledge * 0.2
            scores.append(score)
        return round(float(np.mean(scores)) * 4.0, 2)

    @staticmethod
    def compute_cas(agents: List) -> float:
        """
        Cognitive Absorption Score (CAS) — ACLAS proprietary metric.
        CAS = Σ (absorption_prob_i × attention_i) / n
        Range: 0.0 (total cognitive shutdown) → 1.0 (perfect absorption)
        """
        if not agents:
            return 0.0
        vals = [getattr(a, "last_prob", 0.5) * a.attention for a in agents]
        return round(float(np.mean(vals)), 4)

    @staticmethod
    def compute_retention_rate(agents: List) -> float:
        """% of agents actively retaining (have indexed ≥1 concept and are not Confused)."""
        if not agents:
            return 0.0
        retaining = sum(
            1 for a in agents
            if len(a.knowledge_pool) > 0 and a.current_mood != "Confused"
        )
        return round(retaining / len(agents), 3)

    @staticmethod
    def compute_diversity_index(agents: List) -> float:
        """
        Shannon entropy of mood distribution.
        Higher = more cognitively diverse class (some excel, some struggle).
        Low = everyone in same state (good if Focused, bad if Confused).
        """
        if not agents:
            return 0.0
        moods = [a.current_mood for a in agents]
        total = len(moods)
        entropy = 0.0
        for mood in set(moods):
            p = moods.count(mood) / total
            if p > 0:
                entropy -= p * np.log2(p)
        return round(float(entropy), 4)

    @staticmethod
    def compute_dropout_risk(agents: List) -> List[Dict]:
        """
        Dropout Risk Score = (1-attention)×0.5 + fatigue×0.3 + (1-prior_knowledge)×0.2
        Returns agents with risk > 0.55, sorted descending.
        """
        at_risk = []
        for a in agents:
            risk = (1.0 - a.attention) * 0.5 + a.fatigue * 0.3 + (1.0 - a.prior_knowledge) * 0.2
            if risk > 0.55:
                at_risk.append({"name": a.name, "risk": round(risk, 3), "mood": a.current_mood})
        return sorted(at_risk, key=lambda x: -x["risk"])

    @staticmethod
    def compute_skill_distribution(agents: List) -> Dict[str, float]:
        """Average skill levels across the class per dimension."""
        if not agents:
            return {}
        skill_keys = ["logic", "math", "language", "memory", "creative"]
        result = {}
        for k in skill_keys:
            vals = [a.skill_matrix.skills.get(k, 0.5) for a in agents]
            result[k] = round(float(np.mean(vals)), 3)
        return result

    @staticmethod
    def compute_mood_distribution(agents: List) -> Dict[str, int]:
        moods = ["Excited", "Focused", "Confused", "Neutral"]
        return {m: sum(1 for a in agents if a.current_mood == m) for m in moods}

    @classmethod
    def full_report(cls, agents: List, tick: int, loss_curve: List[float]) -> Dict[str, Any]:
        return {
            "tick": tick,
            "gpa": cls.compute_gpa(agents),
            "cas": cls.compute_cas(agents),
            "retention_rate": cls.compute_retention_rate(agents),
            "diversity_index": cls.compute_diversity_index(agents),
            "dropout_risk": cls.compute_dropout_risk(agents),
            "skill_distribution": cls.compute_skill_distribution(agents),
            "mood_distribution": cls.compute_mood_distribution(agents),
            "loss_curve": loss_curve,
        }
