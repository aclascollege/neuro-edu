"""
UltimateClassroom Engine v3
- Real multi-agent message bus (social learning / knowledge cascading)
- Aggregate loss curve from all agent brains
- Integrated CognitiveEvaluator for full metric reporting
"""
import json
import random
from pathlib import Path
from typing import List, Dict, Any

from .agent import NeuralStudentAgent
from .evaluator import CognitiveEvaluator
from .knowledge_graph import KnowledgeGraph

PROFILES = ["balanced", "math_genius", "linguist", "creative_soul", "memorizer", "polymath"]
NAMES = [
    "Aria", "Blaze", "Cyrus", "Dex", "Echo", "Flux", "Gaia", "Helix",
    "Iris", "Jinx", "Kira", "Lumen", "Mira", "Nova", "Onyx", "Plex",
    "Quinn", "Rho", "Seren", "Talon", "Uma", "Vex", "Wren", "Xen", "Yael", "Zeno",
]

DATA_PATH = Path(__file__).parent.parent / "data" / "knowledge_base.json"


class UltimateClassroom:
    """
    Manages a multi-agent cognitive simulation environment.
    Features:
    - Social Learning Bus (knowledge cascading between agents)
    - Real training on structured dataset
    - Full metric evaluation per tick
    - Knowledge graph construction
    """

    def __init__(self):
        self.agents: List[NeuralStudentAgent] = []
        self.tick: int = 0
        self.global_loss_history: List[float] = []
        self.evaluator = CognitiveEvaluator()
        self.knowledge_graph = KnowledgeGraph()
        self._dataset: List[Dict] = []
        self._load_dataset()

    def _load_dataset(self):
        try:
            with open(DATA_PATH, "r", encoding="utf-8") as f:
                raw = json.load(f)
                self._dataset = raw.get("training_samples", [])
        except Exception:
            self._dataset = []

    def setup(self, count: int = 20):
        self.agents = []
        self.tick = 0
        self.global_loss_history = []
        self.knowledge_graph.reset()

        for i in range(count):
            profile = PROFILES[i % len(PROFILES)]
            name = NAMES[i % len(NAMES)]
            self.agents.append(NeuralStudentAgent(str(i), name, profile))

    def broadcast(self, instruction: str, complexity: float, skills_req: Dict[str, float]) -> Dict:
        """
        Single teaching step:
        1. All agents process the instruction via their MLP
        2. High-performers broadcast knowledge cascade messages to confused peers
        3. Metrics are computed and returned
        """
        self.tick += 1
        results = []

        # Step 1: Process instruction
        for agent in self.agents:
            res = agent.process_sync(instruction, complexity, skills_req)
            results.append(res)

        # Step 2: Social Learning Bus — knowledge cascading
        excited = [a for a in self.agents if a.current_mood == "Excited"]
        confused = [a for a in self.agents if a.current_mood == "Confused"]
        for src in excited:
            # Each excited agent sends a boost signal to up to 2 confused peers
            targets = random.sample(confused, min(2, len(confused)))
            for tgt in targets:
                tgt.receive_message({
                    "from": src.name,
                    "type": "clarity_boost",
                    "content": src.knowledge_pool[-1] if src.knowledge_pool else instruction[:20],
                })

        # Step 3: Aggregate loss (from all agent brains)
        all_losses = []
        for a in self.agents:
            if a.brain.loss_history:
                all_losses.append(a.brain.loss_history[-1])
        avg_loss = round(float(sum(all_losses) / len(all_losses)), 6) if all_losses else None
        if avg_loss is not None:
            self.global_loss_history.append(avg_loss)

        # Step 4: Update knowledge graph
        self.knowledge_graph.build_from_agents(self.agents)

        return {
            "tick": self.tick,
            "agents": results,
            "avg_loss": avg_loss,
            "cascade_events": len(excited),
        }

    def run_training(self, epochs: int = 3) -> Dict:
        """
        Federated training: each agent trains its own MLP on the shared dataset.
        Returns aggregated loss curve.
        """
        if not self._dataset:
            return {"error": "No dataset loaded", "loss": []}

        epoch_losses = []
        for epoch in range(epochs):
            epoch_loss = 0.0
            for agent in self.agents:
                loss = agent.brain.batch_train(self._dataset)
                epoch_loss += loss
            avg = round(epoch_loss / len(self.agents), 6)
            epoch_losses.append(avg)
            self.global_loss_history.append(avg)

        return {
            "epochs": epochs,
            "samples_per_agent": len(self._dataset),
            "epoch_losses": epoch_losses,
            "final_loss": epoch_losses[-1] if epoch_losses else None,
        }

    def get_metrics(self) -> Dict:
        combined_loss = []
        for a in self.agents:
            combined_loss.extend(a.brain.get_loss_curve(20))
        return self.evaluator.full_report(self.agents, self.tick, self.global_loss_history[-50:])

    def get_graph(self) -> Dict:
        return self.knowledge_graph.export()
