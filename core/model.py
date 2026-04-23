"""
ACLAS Tiny-Cognition (ATC) v2
Pure NumPy multi-layer perceptron with full backpropagation.
This is the on-device neural kernel powering every student agent.
"""
import numpy as np
from typing import List, Dict, Tuple


class NeuralLayer:
    """Single fully-connected layer with He initialization."""

    def __init__(self, input_dim: int, output_dim: int):
        # He initialization — correct for ReLU activations
        self.weights = np.random.randn(input_dim, output_dim) * np.sqrt(2.0 / input_dim)
        self.bias = np.zeros((1, output_dim))
        self.last_input: np.ndarray = None
        self.grad_w: np.ndarray = None
        self.grad_b: np.ndarray = None

    def forward(self, x: np.ndarray) -> np.ndarray:
        self.last_input = x
        return np.dot(x, self.weights) + self.bias

    def backward(self, grad_output: np.ndarray) -> np.ndarray:
        self.grad_w = np.dot(self.last_input.T, grad_output)
        self.grad_b = np.sum(grad_output, axis=0, keepdims=True)
        return np.dot(grad_output, self.weights.T)

    def update(self, lr: float, clip: float = 5.0):
        # Gradient clipping for stability
        self.grad_w = np.clip(self.grad_w, -clip, clip)
        self.grad_b = np.clip(self.grad_b, -clip, clip)
        self.weights -= lr * self.grad_w
        self.bias -= lr * self.grad_b


class TinyCognitionModel:
    """
    ACLAS Tiny-Cognition (ATC) v2
    Architecture: Input(5) → Dense(16) → ReLU → Dense(8) → ReLU → Dense(1) → Sigmoid
    Task: Predict cognitive absorption probability given student state features.
    Input features: [complexity, attention, skill_match, fatigue, prior_knowledge]
    Output: absorption_probability ∈ (0, 1)
    """

    def __init__(self, input_dim: int = 5, hidden_dims: List[int] = None):
        if hidden_dims is None:
            hidden_dims = [16, 8]
        dims = [input_dim] + hidden_dims + [1]
        self.layers = [NeuralLayer(dims[i], dims[i + 1]) for i in range(len(dims) - 1)]
        self.lr = 0.005
        self.loss_history: List[float] = []
        self._pre_activations: List[np.ndarray] = []
        self._activations: List[np.ndarray] = []

    # --- Activations ---
    @staticmethod
    def _relu(x: np.ndarray) -> np.ndarray:
        return np.maximum(0.0, x)

    @staticmethod
    def _relu_grad(x: np.ndarray) -> np.ndarray:
        return (x > 0).astype(np.float64)

    @staticmethod
    def _sigmoid(x: np.ndarray) -> np.ndarray:
        return 1.0 / (1.0 + np.exp(-np.clip(x, -500, 500)))

    # --- Forward pass ---
    def predict(self, features: np.ndarray) -> float:
        """Run inference. features shape: (1, input_dim)"""
        self._pre_activations = []
        self._activations = [features]
        x = features.copy()

        for i, layer in enumerate(self.layers):
            z = layer.forward(x)
            self._pre_activations.append(z)
            if i < len(self.layers) - 1:
                x = self._relu(z)
            else:
                x = self._sigmoid(z)
            self._activations.append(x)

        return float(x[0][0])

    # --- Backpropagation (SGD) ---
    def train_step(self, x: np.ndarray, y_true: float) -> float:
        """
        One backprop step.
        Loss: Mean Squared Error (MSE)
        Optimizer: Stochastic Gradient Descent with gradient clipping
        """
        pred = self.predict(x)
        y_arr = np.array([[y_true]])
        pred_arr = np.array([[pred]])

        # MSE loss
        loss = float(np.mean((pred_arr - y_arr) ** 2))
        self.loss_history.append(loss)

        # Output gradient (MSE + Sigmoid combined)
        delta = (pred_arr - y_arr) * pred_arr * (1.0 - pred_arr)

        # Backprop through layers in reverse
        for i in reversed(range(len(self.layers))):
            layer = self.layers[i]
            if i < len(self.layers) - 1:
                delta = delta * self._relu_grad(self._pre_activations[i])
            delta = layer.backward(delta)
            self.layers[i].update(self.lr)

        return loss

    def batch_train(self, dataset: List[Dict]) -> float:
        """Train on a list of {'input': [...], 'expected_absorption': float} samples."""
        if not dataset:
            return 0.0
        total_loss = 0.0
        for sample in dataset:
            x = np.array([sample["input"]], dtype=np.float64)
            y = float(sample["expected_absorption"])
            total_loss += self.train_step(x, y)
        return round(total_loss / len(dataset), 6)

    # --- Utilities ---
    def get_weights_signature(self) -> float:
        """Mean absolute weight of layer 0 — represents 'brain activity level'."""
        return float(np.mean(np.abs(self.layers[0].weights)))

    def get_loss_curve(self, last_n: int = 50) -> List[float]:
        return [round(v, 6) for v in self.loss_history[-last_n:]]

    def get_architecture_summary(self) -> Dict:
        dims = [l.weights.shape[0] for l in self.layers] + [self.layers[-1].weights.shape[1]]
        return {
            "architecture": dims,
            "total_params": sum(l.weights.size + l.bias.size for l in self.layers),
            "optimizer": "SGD",
            "loss_fn": "MSE",
            "activation": "ReLU+Sigmoid",
        }
