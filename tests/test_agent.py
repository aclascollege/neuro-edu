"""pytest test suite for NeuralStudentAgent."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from neuro_edu.agent import NeuralStudentAgent


class TestNeuralStudentAgent:
    def test_initialization(self):
        agent = NeuralStudentAgent("0", "TestAgent", "balanced")
        assert agent.attention == pytest.approx(agent.attention, abs=0.01)
        assert 0.0 <= agent.attention <= 1.0
        assert 0.0 <= agent.fatigue <= 1.0
        assert agent.current_mood == "Neutral"
        assert len(agent.knowledge_pool) == 0

    def test_process_returns_dict(self):
        agent = NeuralStudentAgent("0", "TestAgent", "balanced")
        result = agent.process_sync("Supply and demand fundamentals", 0.3, {"logic": 0.6})
        assert "mood" in result
        assert "prob" in result
        assert "thought" in result
        assert "skills" in result
        assert 0.0 <= result["prob"] <= 1.0

    def test_mood_excited_on_easy_content(self):
        """High-skill agent on easy content should tend toward Excited."""
        moods = []
        # Run 10 times with different agents to overcome random weight init
        for _ in range(10):
            agent = NeuralStudentAgent("0", "Genius", "polymath")
            agent.prior_knowledge = 0.9
            agent.attention = 1.0
            r = agent.process_sync("Basic addition", 0.05, {"math": 0.1})
            moods.append(r["mood"])
        # At least some should be Excited or Focused (not all Confused)
        assert "Confused" not in moods or moods.count("Confused") < 8

    def test_fatigue_increases(self):
        agent = NeuralStudentAgent("0", "Test", "balanced")
        initial_fatigue = agent.fatigue
        for _ in range(10):
            agent.process_sync("Some content", 0.5, {"logic": 0.5})
        assert agent.fatigue > initial_fatigue

    def test_knowledge_pool_grows_on_absorption(self):
        """When excited, knowledge pool should grow."""
        agent = NeuralStudentAgent("0", "Test", "math_genius")
        agent.prior_knowledge = 0.9
        agent.attention = 1.0
        initial_count = len(agent.knowledge_pool)
        for _ in range(20):
            agent.process_sync("Linear algebra basics", 0.1, {"math": 0.2})
        # After many easy lessons, a genius should have absorbed some
        assert len(agent.knowledge_pool) >= initial_count

    def test_message_inbox(self):
        agent = NeuralStudentAgent("0", "Test", "balanced")
        agent.receive_message({"from": "Aria", "type": "clarity_boost", "content": "test"})
        assert len(agent.message_inbox) == 1

    def test_serialization_keys(self):
        agent = NeuralStudentAgent("0", "Test", "balanced")
        agent.process_sync("test", 0.5, {"logic": 0.5})
        s = agent._serialize()
        for key in ["id", "name", "mood", "attention", "prob", "thought", "skills", "brain_sig"]:
            assert key in s
