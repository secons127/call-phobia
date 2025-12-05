# 📞 ON:AIR NEXT — AI 기반 대화·콜 트레이닝 플랫폼

## 🎯 프로젝트 개요 (Overview)

ON:AIR NEXT는*LLM + Google Antigravity(바이브코딩 기반 AI IDE)를 활용하여
사용자의 **전화 공포(Call-Phobia)** 및 **대화 불안**을 완화하기 위한
**상황 시뮬레이션 + 실시간 피드백 + 멀티모달 분석 기반** AI 커뮤니케이션 트레이닝 서비스입니다.

기존 ON:AIR의 단일 LLM 피드백 구조에서 발전하여,
**AI와 공동 개발되는 차세대 방식의 대화 트레이닝 플랫폼**을 목표로 합니다.

---

## 🧠 핵심 기능 (Key Features)

### 1. 실시간 대화 시뮬레이션 (LLM Role-Play Engine)

* 다양한 상황(업무 전화, 병원 예약, CS, 인터뷰 등) 자동 시뮬레이션
* 상황 난이도·톤·캐릭터 커스터마이징
* 멀티모달 감정 기반 응답 생성

### 2. 대화 피드백 분석 (Conversation Feedback Analyzer)

* 발화 구조·명확성·속도·불안 신호 분석
* 개선점, 긍정 피드백, 추천 응답 생성
* LLM 기반 점수화 및 CBT 구조 코칭

### 3. 음성·감정 기반 멀티모달 평가

* 음성 떨림·볼륨 패턴·감정 스트레스 등 자동 분석
* STT → LLM → Summary 파이프라인

### 4. Antigravity 기반 AI 자동개발 에이전트

* AI IDE가 프로젝트 전체 코드를 이해하고 파일 단위 자동 생성·수정
* 디자인 패턴·규칙·아키텍처 일관성 자동 유지

---

## 🏗️ 시스템 아키텍처 (Architecture)

```
User → Microphone → STT Engine → LLM Role-play Engine
          ↓                        ↓
  Multimodal Analyzer ← Audio Features
          ↓
   LLM Feedback Generator
          ↓
     Result Dashboard
```

---

## 🛠️ 기술 스택 (Tech Stack)

### Frontend

* React / Next.js 또는 Flutter
* TailwindCSS / NativeWind
* WebRTC / MediaRecorder API

### Backend

* FastAPI or Node.js Express
* WebSocket 기반 실시간 대화 스트림
* Google Speech-to-Text / Whisper STT

### AI / Model

* OpenAI GPT-5.1 / Gemini 2.0 Flash / Claude 3.7
* 음성 특징 추출 모델
* LLM Role-play Engine

### AI IDE

* **Google Antigravity (Vibe Coding 기반)**

  * 자동 코드 생성 / 파일 수정 / 일관성 유지
  * README, CONTEXT, TASK 기반 협업 개발

### Infra

* Firebase Auth
* Firestore / Supabase
* Cloud Run / Vercel

---

## 📦 설치 방법 (Installation)

```bash
# 1. 레포지토리 클론
git clone https://github.com/yourname/onair-next.git
cd onair-next

# 2. 백엔드 환경 구성
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. 프론트엔드 환경 구성
cd frontend
npm install
```

---

## ▶ 실행 방법 (Run)

### Backend

```bash
python src/main.py
```

### Frontend

```bash
npm run dev
```

---

## 📂 프로젝트 구조 (Project Structure)

```
/onair-next
 ├── README.md
 ├── CONTEXT.md          # AI에게 개발 규칙·제약·구조 제공
 ├── CURRENT_TASK.md     # 현재 AI에게 수행시킬 작업 정의
 ├── backend/
 │    ├── src/
 │    │    ├── main.py
 │    │    ├── stt.py
 │    │    ├── llm_engine.py
 │    │    ├── feedback.py
 │    │    └── models/
 │    └── requirements.txt
 └── frontend/
      ├── components/
      ├── pages/
      └── package.json
```

---

## 🤝 팀 개발 규칙 (for AI IDE & Humans)

* 모든 함수에 Type Hint 필수
* 기능 기반 디렉토리 책임 분리
* LLM Prompt는 `/prompts` 폴더에서 관리
* 클래스명: PascalCase
* 함수명: snake_case
* 함수는 단일 책임 원칙 준수

---

## 🔮 ON:AIR NEXT 비전

* 개인별 커뮤니케이션 능력 지표 생성
* 멀티모달 기반 고도화된 감정 분석
* 자동화된 AI IDE 기반 개발 생산성 극대화
* 실전 대화 능력 향상을 위한 지속형 트레이닝 플랫폼 구축

---


