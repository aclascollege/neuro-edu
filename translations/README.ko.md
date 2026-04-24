<div align="center">

<img src="https://aclas.college/uploads/system/8b0b26b6b391297deb6e9b56768404f5.png" width="80" alt="ACLAS Logo" />

# ACLAS Neuro-Edu SDK (한국어)

### *AI 기반 교육을 위한 자율 인지 시뮬레이션 프레임워크*

**[애틀랜타 인문과학 대학 (ACLAS)](https://aclas.college) 제작**

---

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.19743807-blue.svg)](https://doi.org/10.5281/zenodo.19743807)

**[🚀 온라인 데모](https://aclascollege.github.io/neuro-edu/)** &nbsp;|&nbsp;
**[🤗 Hugging Face](https://huggingface.co/ACLASCollege/neuro-edu-core-v3)** &nbsp;|&nbsp;
**[🌐 공식 홈페이지](https://aclas.college)** &nbsp;|&nbsp;
**[🎓 MCS 프로그램](https://aclas.college/programs/mcs)** &nbsp;|&nbsp;
**[📚 온라인 강의](https://aclas.college/home/courses)** &nbsp;|&nbsp;
**[🎓 전문 자격증](https://aclas.college/verify/certificate-verify)** &nbsp;|&nbsp;
**[💬 커뮤니티](https://aclas.college/admissions/alumni-network)**

</div>

---

**[English](../README.md)** | **[Français](README.fr.md)** | **[Español](README.es.md)** | **[Русский](README.ru.md)** | **[Deutsch](README.de.md)** | **[繁體中文](README.zh-TW.md)** | **[日本語](README.ja.md)** | **[한국어](README.ko.md)**

---

## 🌌 ACLAS Neuro-Edu란 무엇인가요?

**ACLAS Neuro-Edu**는 연구 등급의 오픈 소스 다중 에이전트 인지 시뮬레이션 프레임워크입니다. 외부 AI API에 의존하지 않고 **온디바이스 신경망**, **벡터 공간 의미론**, **열역학적 엔트로피 분석**을 사용하여 지식 습득 과정을 모델링합니다.

> *"우리는 GPT를 래핑하지 않습니다. 제1원칙부터 인지 모델을 구축합니다."*

### 🌟 핵심 기능

- 🧠 **온디바이스 신경 커널**: 순수 NumPy로 구현된 MLP (실제 역전파 지원).
- 🤗 **Hugging Face 통합**：공동 연구를 위해 인지 모델 가중치 내보내기 지원。
- 📡 **사회적 학습**: 20개 이상의 자율 에이전트가 실시간 메시지 버스를 통해 지식 교환.
- 🛡️ **산업용 등급 CI/CD**：자동화된 보안 감사, 종속성 체크 및 성능 벤치마크。
- 📈 **고급 스코어링**: GPA, CAS 점수, 지식 보유율 및 중도 탈락 위험 분석.

## 🔌 플러그형 LLM 인지 엔진

Neuro-Edu는 제1원칙 기반의 미니멀리스트 신경망(`TinyCognitionModel`)과 함께 기본 제공되지만, 우리 프레임워크는 확장성이 매우 뛰어나도록 설계되었습니다. **Ollama** 또는 **vLLM**을 원활하게 연결하여 세계 최고의 오픈 소스 모델을 사용하여 각 AI 학생의 내부 독백과 사고 과정을 구동할 수 있습니다!

우리는 멀티 에이전트 샌드박스 내에서 인지 엔진으로 다음 오픈 웨이트 모델을 테스트하는 것을 강력히 권장합니다:
- 🦙 **Llama-3 & Llama-3.1** (Meta)
- 🤖 **Qwen 2.5** (Alibaba Cloud) - *우리의 `agent.py`에 기본 구성됨*
- 🐋 **DeepSeek-V3 / DeepSeek-Coder** (DeepSeek)
- 💎 **Gemma-2** (Google)
- 🔬 **Phi-3** (Microsoft)
- 🌪️ **Mistral / Mixtral** (Mistral AI)

자신만의 대규모 모델 경기장을 구축하고 다양한 모델이 교육 자극에 어떻게 반응하는지 확인해보세요!

---

## 🏗️ 미션 및 비전

> *"출신이나 수단에 관계없이 모든 지성은 세계 수준의 교육을 받을 자격이 있다."*
> — [ACLAS 미션 및 비전](https://aclas.college/explore/mission-and-vision)

---

## 🚀 빠른 시작

```bash
git clone https://github.com/aclascollege/neuro-edu.git
cd neuro-edu
pip install -r requirements.txt
python main.py
```

브라우저에서 **http://localhost:8000**을 여세요.

---

## 📜 라이선스

이 프로젝트는 **MIT 라이선스**를 따릅니다.

<div align="center">

**[애틀랜타 인문과학 대학](https://aclas.college)에서 ❤️으로 제작되었습니다**

<sub>© 2026 Atlanta College of Liberal Arts and Sciences.</sub>

</div>

---

### 📱 Follow ACLAS

[![Website](https://img.shields.io/badge/Website-aclas.college-00f2ff?style=flat-square&logo=google-chrome)](https://aclas.college)
[![Email](https://img.shields.io/badge/Email-info@aclas.college-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:info@aclas.college)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-ACLAS-0077B5?style=flat-square&logo=linkedin)](https://www.linkedin.com/school/aclascollege)
[![Facebook](https://img.shields.io/badge/Facebook-ACLAS-1877F2?style=flat-square&logo=facebook)](https://www.facebook.com/aclascollege)
[![Instagram](https://img.shields.io/badge/Instagram-ACLAS-E4405F?style=flat-square&logo=instagram)](https://www.instagram.com/aclascollege)
[![YouTube](https://img.shields.io/badge/YouTube-ACLAS-FF0000?style=flat-square&logo=youtube)](https://www.youtube.com/@aclascollege)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-ACLAS-yellow?style=flat-square)](https://huggingface.co/ACLASCollege)
[![X](https://img.shields.io/badge/X-ACLAS-000000?style=flat-square&logo=x&logoColor=white)](https://x.com/aclascollege)
