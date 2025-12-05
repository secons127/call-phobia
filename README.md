
---

# 📄 ON:AIR Mini Game (콜포비아 완화용 AI 미니게임)

## 🎮 프로젝트 개요 (Overview)

**ON:AIR Mini Game**은 전화 공포증(콜포비아)을 겪는 사용자가 부담 없이 “전화 상황에 조금씩 익숙해지도록” 돕는 **초저부담 AI 미니게임**입니다.
실제 통화처럼 음성을 사용하거나 긴 대화를 이어가는 방식이 아니라,

* **LLM이 간단한 전화 상황극을 생성하고**,
* 사용자는 **3개의 선택지만 클릭**하여 반응하며,
* LLM이 **긍정적 강화 피드백을 제공**하는 구조입니다.

이 게임은 Google Antigravity 기반의 **Vibe Coding 방식**으로 개발되며,
AI IDE가 README.md, CONTEXT.md, CURRENT_TASK.md를 자동 활용해 프로젝트 전반을 안내합니다.

---

## 🎯 목적 (Goal)

* 전화·통화에 대한 심리적 부담을 최소화한 상태에서 **가벼운 반복 노출** 제공
* 사용자가 “내가 선택한다”는 **통제감**을 얻도록 설계
* LLM이 실시간으로 *안심·격려·자기효능감 강화* 피드백 제공
* Python 기반 백엔드 + 간단한 프론트엔드로 누구나 손쉽게 실행
* Vibe Coding 명세에 따라 AI 코딩 파트너가 안정적으로 코드를 확장할 수 있는 구조 유지

---

## 🧩 미니게임 핵심 컨셉

### 📱 **Game Title: “전화 받을까 말까?” (Should I Pick Up?)**

사용자는 울리는 전화에 대해 3가지 선택 중 하나만 고르면 됩니다.

#### ▶️ 작동 방식

1. **LLM이 부담 없는 상황극 생성**
   예: “택배기사님이 전화를 걸고 있어요!”

2. **프론트엔드에 전화 애니메이션 표시**

3. **사용자 선택 (3가지)**

   * 📞 받는다
   * 🤔 잠시 후 받는다
   * 🙈 무음으로 넘긴다

4. **LLM의 상냥한 강화 피드백**

   * “지금처럼 천천히 선택해도 괜찮아요!”
   * “전화는 언제나 당신의 템포에 맞추면 돼요 :)”

#### ▶️ 게임의 특징

* 음성 입력 없음
* 긴 대화 없음
* 실패/정답 없음
* 완전한 “부담 제로 구성”

---

# 🧠 **사용 기술 스택 (Tech Stack — Python 기반 상세)**

본 프로젝트는 Python 기반으로 구현되며, 아래 기술 스택을 사용합니다.

---

## **1) Core Layer**

### 🔹 **Google Antigravity + Vibe Coding Workflow**

* AI IDE와 대화하듯 개발
* CONTEXT.md / CURRENT_TASK.md 기반으로 LLM이 코드를 정확히 생성
* 프로젝트 전체가 “AI-first 개발 구조”로 운영

### 🔹 **LLM API (Gemini 또는 OpenAI)**

사용 용도:

* 전화 라운드 시나리오 생성
* 선택지 기반 강화 피드백 생성
* 난이도 없는 심리적 안정 대사 생성

Python 예시:

```python
import openai
from google import generativeai
```

---

## **2) Backend (Python)**

### 🐍 Python Version

* **Python 3.10 ~ 3.12 권장**

### 🖥 Framework

#### ✔ **FastAPI (추천)**

* 비동기 기반, 속도 빠름
* 자동 문서화(Swagger UI)
* REST API 구축에 최적

#### ✔ Flask (대안)

* 구조 단순
* 아주 가벼운 서버에도 적합

---

## **3) Backend 주요 라이브러리**

| 라이브러리                             | 용도               |
| --------------------------------- | ---------------- |
| `fastapi`                         | 백엔드 API 서버       |
| `uvicorn`                         | FastAPI 실행 서버    |
| `openai` 또는 `google-generativeai` | LLM 시나리오/피드백 생성  |
| `python-dotenv`                   | 환경변수(API Key) 관리 |
| `pydantic`                        | 데이터 모델 검증        |
| `requests`                        | HTTP 요청 처리       |

---

## **4) Frontend**

가벼운 UI 중심:

* HTML / CSS / JavaScript
* 또는 React(선택)

필요 요소:

* 전화 울림 애니메이션
* 3개 선택 버튼
* LLM 응답 표시 영역

---

## ⚙️ 설치 방법 (Installation)

```bash
git clone https://github.com/yourname/onair-mini-game.git
cd onair-mini-game

# Python 기반 설치
pip install -r requirements.txt
```

---

## ▶️ 실행 방법 (Run)

### FastAPI 실행 시

```bash
uvicorn src.main:app --reload
```

### Flask 실행 시

```bash
python src/main.py
```

정적 웹 기반이면:

```
frontend/index.html 실행
```

---

# 📁 프로젝트 구조 (Python 기준)

```
/onair-mini-game
├── README.md
├── CONTEXT.md
├── CURRENT_TASK.md
├── .env                     # API Key 관리
├── requirements.txt
├── src/
│   ├── main.py              # FastAPI/Flask 엔트리포인트
│   ├── llm/
│   │   ├── scenario_generator.py
│   │   └── feedback_generator.py
│   ├── utils/
│   │   └── prompts.py       # LLM 프롬프트 템플릿
│   └── frontend/
│       ├── index.html
│       ├── game.js
│       └── style.css
└── tests/
    └── test_api.py
```

---

# 📌 Antigravity + LLM 활용 포인트

* README.md → AI에게 프로젝트의 목적·구조 제공
* CONTEXT.md → 파일 역할, 변수명 규칙, 아키텍처, LLM 작성 규칙 정의
* CURRENT_TASK.md → 지금 개발해야 할 구체적 작업 지시

AI IDE는 이를 “프로젝트의 성경(Bible)”처럼 참고하며 정확한 코드를 생성하게 됨.

---

# 🎨 예시 플레이 흐름

**LLM:**
“친구 민지가 전화를 걸고 있어요!
기쁜 소식이 있다는데… 어떻게 할까요?”

**사용자:**
① 받는다
② 조금만 생각
③ 이번엔 넘긴다

**LLM:**
“너무 좋아요! 지금처럼 천천히 선택하는 것도 하나의 연습이에요 😊”

---

# 🔮 향후 확장 아이디어

* “전화 피하기” 반응 속도 모드
* ‘좋은 전화만 받기’ 모드
* 배지/스탬프 보상
* 데일리 챌린지

---

