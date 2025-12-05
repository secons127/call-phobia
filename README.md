
**ON:AIR Mini Game (콜포비아 완화용 AI 미니게임)**

## 🎮 프로젝트 개요 (Overview)

**ON:AIR Mini Game**은 전화 공포증(콜포비아)을 겪는 사용자가 부담 없이 “전화 상황에 익숙해지도록” 돕기 위한 *초저부담·재미형 미니게임*입니다.
대화 스트레스 없이, **Google Antigravity(바이브코딩 환경)** + **LLM**을 활용하여,
사용자가 “전화받기” 상황을 간접적으로 체험하며 재미있게 연습할 수 있도록 설계되었습니다.

본 미니게임은 실제 통화처럼 말해야 하는 것이 아니라,
**LLM이 제시하는 선택지 / 간단 상호작용 / 타이핑 없는 반응 게임**으로 구성되어
전화를 두려워하는 사용자도 부담 없이 즐길 수 있습니다.

---

## 🎯 목적 (Goal)

* 전화 상황의 압박 없이 **작게, 가볍게, 반복적으로 노출**하여 콜포비아 완화를 돕는다.
* LLM이 사용자 행동을 실시간으로 해석해 **칭찬·강화 피드백**을 제공한다.
* Google Antigravity 환경에서 AI 코딩 파트너와 함께 빠르게 기능을 확장할 수 있는 구조 제공.
  (바이브코딩 명세가 요구하는 “프로젝트 맥락 제공 문서화” 방식 준수)

---

## 🧩 미니게임 핵심 컨셉

### **📱 Game Title: “전화 받을까 말까?” (Should I Pick Up?)**

사용자의 목표는 **전화 벨이 울릴 때 적절한 타이밍에 반응하는 것**이다.
그러나 게임은 단순 클릭이 아니라 LLM이 상황을 연출한다.

#### ▶️ 작동 방식

1. LLM이 가벼운 상황극을 생성

   * 예: “택배기사님이 전화를 걸었어요! 받으면 좋은 일이 생길지도…?”
2. 화면에 전화가 울리는 애니메이션 등장
3. 사용자는 **3가지 부담 없는 선택지** 중 하나를 클릭

   * 📞 받는다
   * 🤔 잠시 후 받는다
   * 🙈 무음으로 넘긴다
4. LLM이 선택에 대해 **긍정적·기분 좋은 피드백**을 제공

   * “지금처럼 천천히 선택하는 것도 좋아요!”
   * “받지 않아도 괜찮아요. 중요한 건 ‘내가 선택했다’는 점이에요!”

#### ▶️ 게임의 특징

* **사용자 음성 입력 없음**
* **전화 공포를 자극하는 실제 대화 없음**
* 부담을 극도로 낮춘 형태

---

## 🧠 사용 기술 스택 (Tech Stack)

PDF 명세에 따라 기술 스택을 README의 필수 요소로 정리함.


### **Core**

* **Google Antigravity + Vibe Coding Workflow**

  * AI IDE와 대화하듯 개발
  * CONTEXT.md / CURRENT_TASK.md 기반 반복 개발 구조
* **LLM API (Gemini or OpenAI)**

  * 시나리오 생성
  * 피드백 생성

### **Frontend**

* HTML/CSS/JS 또는 React (선택 가능)

### **Backend**

* 간단한 Node.js 또는 Python(Flask/FastAPI)

  * 단, 미니게임은 로컬에서도 충분히 동작 가능하도록 설계

---

## ⚙️ 설치 방법 (Installation)

```bash
git clone https://github.com/yourname/onair-mini-game.git
cd onair-mini-game

# 필요 시
pip install -r requirements.txt   # Python 기반일 경우
npm install                      # Node 기반일 경우
```

---

## ▶️ 실행 방법 (Run)

### Python 서버 실행 시

```bash
python src/main.py
```

### Node 서버 실행 시

```bash
npm start
```

또는 웹 정적 파일 기반이면

```text
index.html 열기
```

---

## 📁 프로젝트 구조 (예시)

README는 구조 개요만 포함하도록 PDF에서 설명한 규칙을 따름.
세부 규칙은 CONTEXT.md에서 관리.


```
/onair-mini-game
├── README.md
├── CONTEXT.md
├── CURRENT_TASK.md
├── src/
│   ├── main.py or app.js
│   ├── llm/
│   │   └── scenario_generator.py
│   ├── frontend/
│   │   ├── index.html
│   │   ├── game.js
│   │   └── style.css
└── requirements.txt
```

---

## 📌 Antigravity + LLM 활용 포인트

* **LLM이 게임 상황을 자동 생성**
* **사용자 선택에 따라 맞춤형 강화 피드백 생성**
* **Antigravity에서 CONTEXT.md 기반으로 안정적 코드 생산 가능**
* AI 코드 파트너(LLM)가 *프로젝트의 Bible*로 README와 CONTEXT를 항상 참고하도록 설계
  (PDF의 “AI IDE 활용 목적” 요구사항을 충실히 반영)


---

## 🎨 예시 플레이 흐름 (Example Flow)

**LLM:**
“지금 당신에게 ‘친구 민지가’ 전화를 걸고 있어요!
민지는 좋은 소식을 들려주고 싶대요😊 어떻게 할까요?”

**사용자 선택:**
① 받는다
② 3초만 생각해본다
③ 이번엔 넘긴다

**LLM 반응:**
“좋아요! 지금처럼 ‘내가 선택한 템포’를 유지하는 것이 가장 중요해요.
전화는 언제나 당신의 리듬에 맞춰도 됩니다 :)”

---

## 🔮 향후 확장 아이디어

* “전화 피하기” 모드 → 스트레스 없는 반응 속도 게임
* “좋은 전화만 골라 받기” 미션
* 미니 보상 시스템(스티커/배지)
* 하루 1회 짧은 전화 노출 “데일리 챌린지”

---
