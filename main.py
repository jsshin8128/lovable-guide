from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from priority_model import predict_priority

app = FastAPI()

# CORS 설정 (* 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 요청 모델
class TodoRequest(BaseModel):
    text: str

# 응답 모델
class PriorityResponse(BaseModel):
    priority: str

@app.post("/priority", response_model=PriorityResponse)
async def classify_priority(request: TodoRequest):
    """
    할 일 텍스트를 받아 우선순위를 분류합니다.
    
    - **text**: 할 일 내용
    
    반환값:
    - **priority**: "high", "medium", "low" 중 하나
    """
    priority = predict_priority(request.text)
    return PriorityResponse(priority=priority)

@app.get("/")
async def root():
    return {"message": "할 일 우선순위 자동 분류 API"}

