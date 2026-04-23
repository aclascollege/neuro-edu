"""
NeuralStudentAgent v3
- Driven by TinyCognitionModel (real backprop MLP)
- LLM-powered internal monologue via Ollama (with rich template fallback)
- Participates in message bus for social learning
"""
import numpy as np
import random
import httpx
from typing import List, Dict, Optional

from .model import TinyCognitionModel
from .skills import SkillMatrix

# Ollama config — graceful fallback if not running
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "qwen2:0.5b"
OLLAMA_TIMEOUT = 2.0  # seconds — keep it fast

# Rich thought templates (used when Ollama is unavailable)
THOUGHT_BANK: Dict[str, List[str]] = {
    "Excited": [
        "Neural resonance at {prob:.0%}. Concept '{topic}' anchored to {skill} schema. Long-term encoding initiated.",
        "High-confidence absorption ({prob:.0%}). Semantic bridge formed. Prior knowledge activated.",
        "Aha. '{topic}' aligns with existing {skill} cluster. Synaptic reinforcement firing.",
        "Insight cascade: '{topic}' resolves a prior ambiguity in my knowledge graph.",
    ],
    "Focused": [
        "Processing '{topic}' at {prob:.0%} confidence. {skill} pathway active. Partial integration.",
        "Encoding in progress. Complexity within tolerance. Knowledge delta: +{delta:.3f}.",
        "Monitoring instruction stream. Signal-to-noise ratio acceptable. Absorbing.",
        "Working memory engaged. Building mental model for '{topic}'. Confidence: {prob:.0%}.",
    ],
    "Confused": [
        "Semantic gap detected. '{topic}' exceeds current {skill} boundary. Requesting prerequisite.",
        "Cognitive dissonance: complexity {complexity:.2f} >> prior knowledge {prior:.2f}. Integration failure.",
        "Working memory overflow. Chunking failed. Neural backpressure at layer 2.",
        "Cannot index '{topic}'. Missing prerequisite nodes in {skill} knowledge graph.",
    ],
    "Neutral": [
        "Idle. Monitoring knowledge stream for relevant signal.",
        "Low information delta. Consolidating prior session data.",
        "Standby mode. Awaiting axiomatic input with sufficient signal strength.",
    ],
}


def _sample_thought(mood: str, **kwargs) -> str:
    templates = THOUGHT_BANK.get(mood, THOUGHT_BANK["Neutral"])
    tmpl = random.choice(templates)
    try:
        return tmpl.format(**kwargs)
    except KeyError:
        return tmpl


async def _llm_thought(mood: str, topic: str, agent_name: str) -> Optional[str]:
    """Call local Ollama for a genuine LLM-generated internal monologue."""
    prompt = (
        f"You are a student named {agent_name}. "
        f"You just received a lesson on '{topic}'. "
        f"Your cognitive state is: {mood}. "
        f"Write one short sentence (max 20 words) expressing your internal thought right now. "
        f"Be specific and technical. No quotation marks."
    )
    try:
        async with httpx.AsyncClient(timeout=OLLAMA_TIMEOUT) as client:
            resp = await client.post(OLLAMA_URL, json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {"num_predict": 40, "temperature": 0.7},
            })
            if resp.status_code == 200:
                return resp.json().get("response", "").strip()
    except Exception:
        pass
    return None


class NeuralStudentAgent:
    """
    A cognitively realistic student agent.
    Brain: TinyCognitionModel (NumPy MLP, real backprop)
    Skills: 5-dimensional SkillMatrix
    Thought: Ollama LLM → rich template fallback
    """

    def __init__(self, agent_id: str, name: str, profile: str = "balanced"):
        self.id = agent_id
        self.name = name
        self.profile = profile

        # AI core
        self.brain = TinyCognitionModel(input_dim=5, hidden_dims=[16, 8])
        self.skill_matrix = SkillMatrix(profile)

        # Cognitive state
        self.attention: float = round(random.uniform(0.7, 1.0), 3)
        self.fatigue: float = 0.0
        self.prior_knowledge: float = round(random.uniform(0.1, 0.5), 3)

        # Memory
        self.knowledge_pool: List[str] = []
        self.message_inbox: List[Dict] = []  # messages from other agents

        # Persistent state
        self.current_mood: str = "Neutral"
        self.last_thought: str = "Agent initialized. Awaiting instruction stream."
        self.last_prob: float = 0.5

    def _build_features(self, complexity: float, skill_match: float) -> np.ndarray:
        return np.array([[complexity, self.attention, skill_match, self.fatigue, self.prior_knowledge]])

    def process_sync(self, instruction_text: str, complexity: float, skills_req: Dict[str, float]) -> Dict:
        """Synchronous process — runs the MLP and updates state."""
        topic = instruction_text[:30] if instruction_text else "unknown"
        skill_match = self.skill_matrix.match_content(skills_req)

        # MLP inference
        features = self._build_features(complexity, skill_match)
        absorption_prob = self.brain.predict(features)
        self.last_prob = round(absorption_prob, 4)

        # Apply social learning boost from inbox
        if self.message_inbox:
            boost = min(0.15, len(self.message_inbox) * 0.04)
            absorption_prob = min(1.0, absorption_prob + boost)
            self.message_inbox.clear()

        # State transitions
        if absorption_prob > 0.68:
            self.current_mood = "Excited"
            self.attention = min(1.0, self.attention + 0.05)
            concept = topic.strip()
            if concept and concept not in self.knowledge_pool:
                self.knowledge_pool.append(concept)
        elif absorption_prob < 0.32:
            self.current_mood = "Confused"
            self.attention = max(0.05, self.attention - 0.12)
        else:
            self.current_mood = "Focused"
            self.attention = max(0.05, self.attention - 0.02)

        # Fatigue accumulation (Yerkes-Dodson inspired)
        self.fatigue = min(1.0, self.fatigue + 0.025)

        # Generate thought (template mode for sync)
        self.last_thought = _sample_thought(
            self.current_mood,
            prob=absorption_prob,
            topic=topic,
            skill=self.skill_matrix.dominant_skill(),
            complexity=complexity,
            prior=self.prior_knowledge,
            delta=self.last_prob - 0.5,
        )

        return self._serialize()

    def receive_message(self, msg: Dict):
        """Receive a knowledge cascade message from another agent."""
        self.message_inbox.append(msg)

    def _serialize(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "profile": self.profile,
            "mood": self.current_mood,
            "attention": round(self.attention, 3),
            "prob": self.last_prob,
            "fatigue": round(self.fatigue, 3),
            "thought": self.last_thought,
            "skills": self.skill_matrix.to_dict(),
            "knowledge_count": len(self.knowledge_pool),
            "brain_sig": round(self.brain.get_weights_signature(), 5),
        }
