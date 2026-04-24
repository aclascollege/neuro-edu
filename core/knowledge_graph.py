"""
Lightweight knowledge graph builder.
Tracks concept nodes and their relations as agents learn.
Exports a D3.js-compatible JSON format for live visualization.
"""
from typing import Dict, List, Any


class KnowledgeGraph:
    """
    Builds a dynamic knowledge graph from agent learning events.
    No external dependencies — pure Python.
    """

    def __init__(self):
        self.nodes: Dict[str, Dict] = {}
        self.edges: List[Dict] = []
        self._edge_set: set = set()

    def add_concept(self, concept: str, category: str, strength: float = 1.0):
        cid = concept[:30].strip()
        if not cid:
            return
        if cid not in self.nodes:
            self.nodes[cid] = {
                "id": cid,
                "label": cid,
                "category": category,
                "strength": round(strength, 3),
                "count": 1,
            }
        else:
            self.nodes[cid]["count"] += 1
            self.nodes[cid]["strength"] = round(
                min(1.0, self.nodes[cid]["strength"] + 0.05), 3
            )

    def add_relation(self, source: str, target: str, weight: float = 0.5):
        src = source[:30].strip()
        tgt = target[:30].strip()
        if not src or not tgt or src == tgt:
            return
        key = f"{src}→{tgt}"
        if key not in self._edge_set:
            self._edge_set.add(key)
            self.edges.append({
                "source": src,
                "target": tgt,
                "weight": round(weight, 3),
            })

    def build_from_agents(self, agents: List) -> Dict:
        self.nodes = {}
        self.edges = []
        self._edge_set = set()

        for agent in agents:
            pool = agent.knowledge_pool
            dominant = agent.skill_matrix.dominant_skill()
            for i, concept in enumerate(pool[-10:]):
                self.add_concept(concept, dominant, agent.attention)
                if i > 0:
                    self.add_relation(pool[max(0, len(pool) - i - 2)], concept,
                                      getattr(agent, "last_prob", 0.5))
        return self.export()

    def export(self) -> Dict[str, Any]:
        return {
            "nodes": list(self.nodes.values()),
            "edges": self.edges,
            "stats": {
                "total_concepts": len(self.nodes),
                "total_relations": len(self.edges),
            },
        }

    def reset(self):
        self.nodes = {}
        self.edges = []
        self._edge_set = set()
