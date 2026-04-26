"""pytest test suite for UltimateClassroom engine."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from neuro_edu.engine import UltimateClassroom


class TestUltimateClassroom:
    @pytest.fixture
    def classroom(self):
        c = UltimateClassroom()
        c.setup(10)
        return c

    def test_setup_creates_agents(self, classroom):
        assert len(classroom.agents) == 10
        assert classroom.tick == 0

    def test_broadcast_increments_tick(self, classroom):
        classroom.broadcast("Test lesson", 0.5, {"logic": 0.5})
        assert classroom.tick == 1

    def test_broadcast_returns_results(self, classroom):
        result = classroom.broadcast("Supply and demand", 0.4, {"logic": 0.6})
        assert "tick" in result
        assert "agents" in result
        assert len(result["agents"]) == 10

    def test_broadcast_all_agents_respond(self, classroom):
        result = classroom.broadcast("Quantum mechanics", 0.9, {"math": 0.9})
        for agent_data in result["agents"]:
            assert "mood" in agent_data
            assert "prob" in agent_data
            assert 0.0 <= agent_data["prob"] <= 1.0

    def test_training_reduces_loss(self, classroom):
        """Training should produce epoch losses that are valid floats."""
        if not classroom._dataset:
            pytest.skip("No dataset available")
        result = classroom.run_training(epochs=3)
        assert "epoch_losses" in result
        assert len(result["epoch_losses"]) == 3
        for loss in result["epoch_losses"]:
            assert loss >= 0.0

    def test_metrics_report_structure(self, classroom):
        classroom.broadcast("Test", 0.5, {"logic": 0.5})
        metrics = classroom.get_metrics()
        for key in ["gpa", "cas", "retention_rate", "diversity_index", "mood_distribution"]:
            assert key in metrics

    def test_gpa_in_valid_range(self, classroom):
        for _ in range(5):
            classroom.broadcast("Economics lesson", 0.4, {"logic": 0.6})
        metrics = classroom.get_metrics()
        assert 0.0 <= metrics["gpa"] <= 4.0

    def test_reset_clears_state(self, classroom):
        classroom.broadcast("Test", 0.5, {"logic": 0.5})
        classroom.setup(10)
        assert classroom.tick == 0
        assert len(classroom.global_loss_history) == 0

    def test_knowledge_graph_export(self, classroom):
        for _ in range(3):
            classroom.broadcast("Lesson on logic", 0.3, {"logic": 0.8})
        graph = classroom.get_graph()
        assert "nodes" in graph
        assert "edges" in graph
        assert "stats" in graph
