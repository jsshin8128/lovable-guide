# 할 일 우선순위 자동 분류 API

FastAPI 기반의 할 일 우선순위 자동 분류 API입니다. Naive Bayes 머신러닝 모델을 사용하여 할 일 텍스트를 분석하고 우선순위를 자동으로 분류합니다.

## 로컬 실행 방법

### 1. uv 설치 (최초 1회만)

**Linux/Mac:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

설치 후 터미널을 재시작하거나 `source ~/.bashrc` (Linux)를 실행하세요.

### 2. 의존성 설치 및 서버 실행

**uv로 실행**

```bash
uv pip install -r requirements.txt
uv run uvicorn main:app --reload
```

서버가 실행되면 `http://localhost:8000`에서 API를 사용할 수 있습니다.

API 문서는 `http://localhost:8000/docs`에서 확인할 수 있습니다.

## Render 배포 방법

### 1. GitHub 저장소에 코드 푸시

프로젝트를 GitHub 저장소에 푸시합니다.

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-github-repo-url>
git push -u origin main
```

### 2. Render에서 새 Web Service 생성

1. [Render 대시보드](https://dashboard.render.com)에서 "New +" → "Web Service" 선택
2. GitHub 저장소 연결
3. 다음 설정 적용:

**Environment:** `Python 3`

**Build Command:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh && source $HOME/.local/bin/env && rm -rf .venv && uv venv && source .venv/bin/activate && uv pip install -r requirements.txt
```

**Start Command:**
```bash
source .venv/bin/activate && uvicorn main:app --host 0.0.0.0 --port $PORT
```

**또는 더 간단한 방법 (--system 플래그 사용):**

**Build Command:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh && export PATH="$HOME/.local/bin:$PATH" && uv pip install --system -r requirements.txt
```

**Start Command:**
```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

### 3. 환경 변수

기본적으로 환경 변수 설정이 필요하지 않습니다.

### 4. 배포 완료

배포가 완료되면 Render에서 제공하는 URL로 API에 접근할 수 있습니다.

예: `https://your-app-name.onrender.com/priority`

## 📡 API 사용법

### 엔드포인트

**POST** `/priority`

할 일 텍스트를 받아 우선순위를 분류합니다.

### 요청 예시

```json
{
  "text": "회의 준비하기"
}
```

### 응답 예시

```json
{
  "priority": "high"
}
```

### cURL 예시

```bash
curl -X POST "https://your-app.onrender.com/priority" \
  -H "Content-Type: application/json" \
  -d '{"text": "회의 준비하기"}'
```

### Python 예시

```python
import requests

url = "https://your-app.onrender.com/priority"
data = {"text": "회의 준비하기"}
response = requests.post(url, json=data)
print(response.json())  # {"priority": "high"}
```

## 🧠 우선순위 분류

API는 Naive Bayes 머신러닝 모델을 사용하여 할 일 텍스트를 다음 세 가지 우선순위로 분류합니다:

- **high**: 높은 우선순위 (예: 프로젝트 발표, 보고서 작성)
- **medium**: 중간 우선순위 (예: 세탁, 방 청소)
- **low**: 낮은 우선순위 (예: 유튜브 보기, 넷플릭스 보기)

## 📁 프로젝트 구조

```
.
├── main.py              # FastAPI 애플리케이션
├── priority_model.py    # Naive Bayes ML 모델
├── requirements.txt     # Python 의존성
└── README.md           # 프로젝트 문서
```

## 🔧 기술 스택

- **FastAPI**: 고성능 웹 프레임워크
- **scikit-learn**: 머신러닝 라이브러리
- **uvicorn**: ASGI 서버
- **uv**: 초고속 Python 패키지 매니저 (Rust 기반)

