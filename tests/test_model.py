"""pytest test suite for TinyCognitionModel."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import numpy as np
from core.model import TinyCognitionModel, NeuralLayer


class TestNeuralLayer:
    def test_forward_shape(self):
        layer = NeuralLayer(5, 8)
        x = np.ones((1, 5))
        out = layer.forward(x)
        assert out.shape == (1, 8)

    def test_backward_shape(self):
        layer = NeuralLayer(5, 8)
        x = np.ones((1, 5))
        layer.forward(x)
        grad = np.ones((1, 8))
        dx = layer.backward(grad)
        assert dx.shape == (1, 5)

    def test_he_init_scale(self):
        layer = NeuralLayer(100, 50)
        # He init: std ≈ sqrt(2/100) = 0.141
        std = np.std(layer.weights)
        assert 0.05 < std < 0.5, f"Unexpected weight std: {std}"


class TestTinyCognitionModel:
    def test_predict_range(self):
        model = TinyCognitionModel()
        x = np.array([[0.5, 0.8, 0.6, 0.1, 0.4]])
        prob = model.predict(x)
        assert 0.0 <= prob <= 1.0

    def test_predict_deterministic(self):
        """Same input same weights → same output."""
        model = TinyCognitionModel()
        x = np.array([[0.3, 0.7, 0.5, 0.2, 0.4]])
        p1 = model.predict(x)
        p2 = model.predict(x)
        assert abs(p1 - p2) < 1e-10

    def test_train_step_returns_loss(self):
        model = TinyCognitionModel()
        x = np.array([[0.5, 0.8, 0.6, 0.1, 0.4]])
        loss = model.train_step(x, 0.85)
        assert isinstance(loss, float)
        assert loss >= 0.0

    def test_loss_decreases_over_training(self):
        """After 200 steps on same sample, loss should be lower than initial."""
        np.random.seed(42)
        model = TinyCognitionModel()
        x = np.array([[0.3, 0.9, 0.8, 0.0, 0.6]])
        y = 0.9
        initial_loss = model.train_step(x, y)
        for _ in range(200):
            model.train_step(x, y)
        final_loss = model.loss_history[-1]
        assert final_loss < initial_loss, f"Loss did not decrease: {initial_loss} → {final_loss}"

    def test_batch_train(self):
        model = TinyCognitionModel()
        dataset = [
            {"input": [0.3, 0.9, 0.8, 0.0, 0.6], "expected_absorption": 0.9},
            {"input": [0.8, 0.3, 0.2, 0.5, 0.1], "expected_absorption": 0.1},
        ]
        loss = model.batch_train(dataset)
        assert isinstance(loss, float)
        assert loss >= 0.0

    def test_architecture_summary(self):
        model = TinyCognitionModel(input_dim=5, hidden_dims=[16, 8])
        summary = model.get_architecture_summary()
        assert summary["architecture"] == [5, 16, 8, 1]
        assert summary["total_params"] > 0

    def test_weights_signature(self):
        model = TinyCognitionModel()
        sig = model.get_weights_signature()
        assert isinstance(sig, float)
        assert sig > 0
