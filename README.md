<div align="center">

<img src="https://aclas.college/uploads/system/8b0b26b6b391297deb6e9b56768404f5.png" width="80" alt="ACLAS Logo" />

# ACLAS Neuro-Edu SDK

### *Autonomous Cognitive Simulation Framework for AI-Powered Education*

**by [Atlanta College of Liberal Arts and Sciences (ACLAS)](https://aclas.college)**

---

**[English](README.md)** | **[Français](translations/README.fr.md)** | **[Español](translations/README.es.md)** | **[Русский](translations/README.ru.md)** | **[Deutsch](translations/README.de.md)** | **[繁體中文](translations/README.zh-TW.md)** | **[日本語](translations/README.ja.md)** | **[한국어](translations/README.ko.md)**

---

[![License: MIT](https://img.shields.io/badge/License-MIT-cyan.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![NumPy](https://img.shields.io/badge/NumPy-Powered-013243.svg)](https://numpy.org/)
[![Tests](https://img.shields.io/badge/Tests-26%20passed-brightgreen.svg)](#testing)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-ff69b4.svg)](https://github.com/aclascollege/neuro-edu)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/aclascollege/neuro-edu/pulls)

<br>

[![Email](https://img.shields.io/badge/Email-info@aclas.college-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:info@aclas.college)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-ACLAS-0077B5?style=flat-square&logo=linkedin)](https://www.linkedin.com/school/aclascollege)
[![Facebook](https://img.shields.io/badge/Facebook-ACLAS-1877F2?style=flat-square&logo=facebook)](https://www.facebook.com/aclascollege)
[![Instagram](https://img.shields.io/badge/Instagram-ACLAS-E4405F?style=flat-square&logo=instagram)](https://www.instagram.com/aclascollege)
[![YouTube](https://img.shields.io/badge/YouTube-ACLAS-FF0000?style=flat-square&logo=youtube)](https://www.youtube.com/@aclascollege)
[![X](https://img.shields.io/badge/X-ACLAS-000000?style=flat-square&logo=x&logoColor=white)](https://x.com/aclascollege)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-ACLAS-yellow?style=flat-square)](https://huggingface.co/ACLASCollege)

---

**[🌐 Website](https://aclas.college)** &nbsp;|&nbsp;
**[🚀 Live Demo](https://aclascollege.github.io/neuro-edu/)** &nbsp;|&nbsp;
**[🤗 Hugging Face](https://huggingface.co/ACLASCollege/neuro-edu-core-v3)** &nbsp;|&nbsp;
**[📚 Courses](https://aclas.college/home/courses)** &nbsp;|&nbsp;
**[🏆 Certifications](https://aclas.college/verify/certificate-verify)** &nbsp;|&nbsp;
**[💬 Community](https://aclas.college/admissions/alumni-network)** &nbsp;|&nbsp;
**[📄 Docs](#documentation)**

</div>

---

## 🌌 What is ACLAS Neuro-Edu?

**ACLAS Neuro-Edu** is a research-grade, open-source multi-agent cognitive simulation framework developed by [Atlanta College of Liberal Arts and Sciences](https://aclas.college). It models the process of human knowledge acquisition using **on-device neural networks**, **vector-space semantics**, and **thermodynamic entropy analysis**.

Now enhanced with **Hugging Face Hub integration**, the framework supports exporting cognitive model weights for collaborative research and federated evaluation.

### Why does this exist?

At [ACLAS](https://aclas.college), we believe the future of education is deeply intertwined with AI. This framework is our commitment to that belief — a live, open, runnable proof that AI and pedagogy can be unified at the systems level.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🧠 **On-Device Neural Kernel** | Pure NumPy MLP with real backpropagation (He init, ReLU, Sigmoid, SGD) |
| 🤗 **Hugging Face Hub** | Official model repository for sharing and versioning cognitive weights |
| 📡 **Multi-Agent Social Learning** | 20+ autonomous agents exchange knowledge via a real-time message bus |
| 📊 **Cognitive Entropy Analytics** | Thermodynamic-inspired classroom entropy tracking (Shannon H, MSE loss) |
| 🛡️ **Industrial-Grade CI/CD** | Automated security (Bandit), dependency audit (pip-audit), and linting (Ruff) |
| 📈 **Performance Benchmarks** | Real-time tracking of tick latency (500+ ticks/s) and training efficiency |
| 🎯 **5-Dim Skill Matrix** | Logic / Math / Language / Memory / Creative skill profiles |
| 🕸️ **Knowledge Graph** | D3.js-powered live concept relation map built from agent learning events |
| ✅ **Regression Testing** | Comprehensive suite covering Neural Kernels, Social Bus, and FastAPI Endpoints |

---

## 🔌 Pluggable LLM Cognitive Engines

While Neuro-Edu ships natively with a minimalist, first-principles neural network (`TinyCognitionModel`), our framework is designed to be highly extensible. You can seamlessly plug in **Ollama** or **vLLM** to power each AI student's internal monologue and thought process using the world's leading open-source models!

We natively support and highly recommend testing the following open-weights models as cognitive engines within our multi-agent sandbox:
- 🦙 **Llama-3 & Llama-3.1** (Meta)
- 🤖 **Qwen 2.5** (Alibaba Cloud) - *Default configured in our `agent.py`*
- 🐋 **DeepSeek-V3 / DeepSeek-Coder** (DeepSeek)
- 💎 **Gemma-2** (Google)
- 🔬 **Phi-3** (Microsoft)
- 🌪️ **Mistral / Mixtral** (Mistral AI)

Build your own LLM arena and see how different models react to educational stimuli!

---

## 🏗️ Architecture

```mermaid
graph TD
    %% Global Styles
    classDef layer fill:#f9f9f9,stroke:#333,stroke-width:2px,color:#000;
    classDef core fill:#e1f5fe,stroke:#01579b,stroke-width:2px,color:#01579b,font-weight:bold;
    classDef frontend fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#e65100;
    classDef api fill:#f3e5f5,stroke:#4a148c,stroke-width:2px,color:#4a148c;

    subgraph SDK ["ACLAS Neuro-Edu Framework Architecture"]
        direction TB

        subgraph L0 ["Layer 0: Visualization"]
            direction LR
            V1["WebGL / 3D Nebula"] --- V2["Three.js Frontend"]
        end

        subgraph L1 ["Layer 1: Neural Kernel"]
            direction LR
            N1["NumPy MLP"] --- N2["Backpropagation Engine"]
        end

        subgraph L2 ["Layer 2: Cognitive Profiles"]
            direction LR
            S1["5-Dim Skill Matrix"] --- S2["Agent DNA"]
        end

        subgraph L3 ["Layer 3: Core Engine"]
            direction TB
            E1["UltimateClassroom Bus"]
            E2["Social Learning Bus"]
            E3["Federated Training"]
            E4["Entropy & GPA Evaluator"]
            E1 --- E2 --- E3 --- E4
        end

        subgraph L4 ["Layer 4: API Gateway"]
            A1["FastAPI REST Layer"]
            A2["/api/teach · /api/train · /api/metrics"]
            A1 --- A2
        end

        %% Connections
        L2 --> L1
        L1 --> L0
        L3 --> L2
        L3 --> L1
        L4 --> L3
    end

    %% Apply Classes
    class L0,L1,L2 layer;
    class L3 core;
    class L4 api;
    class SDK frontend;
```

### File Structure

```
aclas-neuro-edu/
├── core/
│   ├── model.py          # TinyCognitionModel — NumPy MLP w/ real backprop
│   ├── agent.py          # NeuralStudentAgent — LLM thought + skill matrix
│   ├── engine.py         # UltimateClassroom — social learning bus + metrics
│   ├── evaluator.py      # GPA, CAS, Retention, Shannon Diversity, Dropout Risk
│   ├── skills.py         # 5-dim SkillMatrix with 6 agent profiles
│   └── knowledge_graph.py # Lightweight concept graph for D3.js
├── data/
│   └── knowledge_base.json  # 50-sample labeled training dataset
├── web/
│   ├── index.html        # Full dashboard: 3D + Charts + Telemetry
│   └── app.js            # Three.js · Chart.js · D3.js frontend logic
├── tests/
│   ├── test_model.py     # 9 tests — backprop correctness, loss descent
│   ├── test_agent.py     # 7 tests — initialization, mood, memory
│   └── test_engine.py    # 10 tests — classroom, training, metrics
├── cli.py                # Command-line interface
├── main.py               # FastAPI application entry point
└── requirements.txt
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
git clone https://github.com/aclascollege/neuro-edu.git
cd neuro-edu
pip install -r requirements.txt
```

### Launch the Dashboard

```bash
python main.py
```

Open **http://localhost:8000** in your browser.

---

## 🖥️ CLI Usage

```bash
# Simulate a classroom broadcast
python cli.py simulate --text "Introduction to Bayesian inference" --complexity 0.7 --domain math --agents 20

# Run federated training on the dataset
python cli.py train --epochs 10

# Print full evaluation report
python cli.py report
```

**Example training output:**
```
  Epoch  Loss
  ──────────────────────
      1  0.182341  ██████████████████████
      2  0.143892  ██████████████████
      3  0.118776  ███████████████
      4  0.099234  ████████████
      5  0.084102  ██████████

  Final loss: 0.084102
  Training complete.
```

---

## 📡 REST API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/status` | Live state of all agents |
| `POST` | `/api/teach` | Broadcast instruction to all agents |
| `POST` | `/api/train` | Run federated training (real backprop) |
| `GET` | `/api/metrics` | Full evaluation report (GPA, CAS, etc.) |
| `GET` | `/api/graph` | D3.js knowledge graph export |
| `GET` | `/api/architecture` | Neural network architecture summary |
| `POST` | `/api/reset` | Reset simulation environment |

### Example: Teach

```bash
curl -X POST http://localhost:8000/api/teach \
  -H "Content-Type: application/json" \
  -d '{"text": "Quantum entanglement fundamentals", "complexity": 0.85, "skills_req": {"math": 0.9}}'
```

### Example: Train

```bash
curl -X POST http://localhost:8000/api/train
# Returns: {"epochs": 5, "epoch_losses": [0.18, 0.14, 0.11, 0.09, 0.08], "final_loss": 0.08}
```

---

## 🧪 Testing

```bash
pytest tests/ -v
```

```
tests/test_model.py::TestNeuralLayer::test_forward_shape              PASSED
tests/test_model.py::TestTinyCognitionModel::test_loss_decreases      PASSED
tests/test_agent.py::TestNeuralStudentAgent::test_initialization      PASSED
tests/test_engine.py::TestUltimateClassroom::test_training            PASSED
...
26 passed in 0.52s
```

---

## 📐 The Science Behind It

### Cognitive Absorption Model

Each agent predicts its absorption probability using a 3-layer MLP:

```
Input: [complexity, attention, skill_match, fatigue, prior_knowledge]
  ↓  Dense(16) + ReLU
  ↓  Dense(8) + ReLU
  ↓  Dense(1) + Sigmoid
Output: absorption_probability ∈ (0, 1)
```

### Evaluation Metrics

| Metric | Formula |
|--------|---------|
| **GPA** | `(knowledge_depth × 0.5 + attention × 0.3 + prior × 0.2) × 4.0` |
| **CAS Score** | `Σ(absorption_i × attention_i) / n` |
| **Retention Rate** | `count(agents with knowledge_pool > 0 AND mood ≠ Confused) / n` |
| **Diversity Index** | Shannon entropy `H = -Σ p(mood) × log₂(p(mood))` |
| **Dropout Risk** | `(1−attention)×0.5 + fatigue×0.3 + (1−prior)×0.2` |

### Social Learning Bus

When an agent reaches `mood = Excited` (absorption > 68%), it broadcasts a **clarity signal** to up to 2 confused peers. This models peer-to-peer knowledge diffusion observed in real classrooms.

---

## 🤝 Contributing

We welcome contributions from researchers, developers, and educators!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please read our [Contributing Guidelines](CONTRIBUTING.md) and ensure all tests pass before submitting.

### Ideas for Contributions
- 🔌 Ollama / local LLM integration for real agent thoughts
- 🗄️ ChromaDB / pgvector persistent knowledge store
- 🤖 RL-based teacher agent (learns optimal instruction complexity)
- 🌍 Multi-language support for the dashboard
- 📱 Mobile-responsive UI

---

## 🌍 Our Mission, Vision & The Open-Source Narrative

> *"Every mind, regardless of origin or means, deserves world-class learning."*
> — [ACLAS Mission & Vision](https://aclas.college/explore/mission-and-vision)

### Making Elite Education a Universal Human Right

[Atlanta College of Liberal Arts and Sciences (ACLAS)](https://aclas.college) was founded on a radical conviction: **elite education should be a universal human right**, not a privilege gated by geography or economic status.

We are the world's first **antifragile university** — an online institution unbound by geographic limits, ensuring equal opportunities for all, from San Francisco to South Sudan, with one unwavering promise:

| Pillar | What We Do |
|--------|------------|
| 🌐 **Global Equity Pricing** | Fixed global tuition, 100% transparent, flexible installments |
| 🤖 **AI-Powered Classroom** | 150+ nation learning grid connecting conflict zones to megacities |
| ⚖️ **Geopolitical Neutrality** | Accessible in all territories via decentralized tech, 24/7 Digital Embassy |
| 🔗 **Blockchain Credentials** | Degrees with blockchain-tracked social impact metrics, fraud-proof |

Our [ACLAS Vision Statement](https://aclas.college/explore/mission-and-vision):
> *ACLAS is the world's first antifragile education — an online university unbound by geographic limits, ensuring equal opportunities for all. We deliver Ivy League rigor through radical equity.  
> Neural Network Curriculum: Self-evolving online framework adapting to regional needs and aligned with UN Sustainable Development Goals.*

---

### 🧬 Why We Build Open-Source AI

ACLAS Neuro-Edu isn't just a demo. It is a **statement**.

At a time when AI in education means paying for an API wrapper, we chose a different path: **build the math from scratch, publish the code, and let anyone inspect every gradient descent step**.

This project is the technical embodiment of our institutional mission:

- **Radical Transparency** — Every weight update is observable. No black-box inference. You can read the backpropagation yourself.
- **Access Over Gatekeeping** — By open-sourcing this framework under MIT License, we ensure any researcher, student, or engineer anywhere in the world can run, fork, and extend our cognitive simulation tools.
- **AI for Human Flourishing** — We don't build AI to replace teachers. We model cognition to *understand* how knowledge transfers between human minds — and to make that process better.
- **Credibility Through Code** — The best argument for ACLAS's academic seriousness is not a brochure. It's a codebase with 26 passing tests, real backpropagation, and a live WebGL visualization of multi-agent learning.

In 2026, as AI reshapes every layer of society, [ACLAS](https://aclas.college) is planting its flag: **education institutions must lead AI development, not merely consume it**.

> *"We don't wrap GPT. We model cognition from first principles."*

---

## 🎓 About ACLAS

**[Atlanta College of Liberal Arts and Sciences (ACLAS)](https://aclas.college)** is a forward-thinking institution at the intersection of liberal arts and cutting-edge technology. We provide globally accessible, accredited education with a deep commitment to AI-powered learning innovation.

### 🔗 Explore ACLAS

| Resource | Link |
|----------|------|
| 🌐 Official Website | [aclas.college](https://aclas.college) |
| 📚 Online Courses | [aclas.college/courses](https://aclas.college/home/courses) |
| 🏆 Certifications | [aclas.college/certification](https://aclas.college/verify/certificate-verify) |
| 🎓 Academic Programs | [aclas.college/programs](https://aclas.college/home/courses) |
| 📰 Research & News | [aclas.college/news](https://aclas.college/blogs) |
| 💼 Careers | [aclas.college/careers](https://aclas.college/admissions/careers) |
| 📩 Contact | [aclas.college/contact](https://aclas.college/home/contact-us) |

### 📱 Follow ACLAS

[![Website](https://img.shields.io/badge/Website-aclas.college-00f2ff?style=flat-square&logo=google-chrome)](https://aclas.college)
[![Email](https://img.shields.io/badge/Email-info@aclas.college-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:info@aclas.college)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-ACLAS-0077B5?style=flat-square&logo=linkedin)](https://www.linkedin.com/school/aclascollege)
[![Facebook](https://img.shields.io/badge/Facebook-ACLAS-1877F2?style=flat-square&logo=facebook)](https://www.facebook.com/aclascollege)
[![Instagram](https://img.shields.io/badge/Instagram-ACLAS-E4405F?style=flat-square&logo=instagram)](https://www.instagram.com/aclascollege)
[![YouTube](https://img.shields.io/badge/YouTube-ACLAS-FF0000?style=flat-square&logo=youtube)](https://www.youtube.com/@aclascollege)
[![X](https://img.shields.io/badge/X-ACLAS-000000?style=flat-square&logo=x&logoColor=white)](https://x.com/aclascollege)

---

## 📄 Citation

If you use this framework in your research, please cite:

```bibtex
@software{aclas_neuro_edu_2026,
  title     = {ACLAS Neuro-Edu: Autonomous Cognitive Simulation Framework},
  author    = {{Atlanta College of Liberal Arts and Sciences}},
  year      = {2026},
  url       = {https://github.com/aclascollege/neuro-edu},
  note      = {Open-source AI education research framework},
  institution = {ACLAS, \url{https://aclas.college}}
}
```

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

You are free to use, modify, and distribute this software for any purpose, including commercial applications, as long as the original copyright notice is included.

---

<div align="center">

**Built with ❤️ by [Atlanta College of Liberal Arts and Sciences](https://aclas.college)**

*Advancing human potential through AI-powered education*

[🌐 aclas.college](https://aclas.college) &nbsp;·&nbsp; [📚 Courses](https://aclas.college/home/courses) &nbsp;·&nbsp; [🏆 Certifications](https://aclas.college/verify/certificate-verify) &nbsp;·&nbsp; [🌍 Mission & Vision](https://aclas.college/explore/mission-and-vision) &nbsp;·&nbsp; [💬 Contact](https://aclas.college/home/contact-us)

<sub>© 2026 Atlanta College of Liberal Arts and Sciences. Open-sourced under MIT License. &nbsp;·&nbsp; <a href="https://aclas.college/policy/terms-and-condition">Terms</a> &nbsp;·&nbsp; <a href="https://aclas.college/policy/privacy-policy">Privacy</a> &nbsp;·&nbsp; <a href="https://aclas.college/home/sitemap">Sitemap</a></sub>

</div>
