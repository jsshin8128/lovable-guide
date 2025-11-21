from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 학습 데이터
texts = [
    "프로젝트 발표 자료 만들기",
    "보고서 작성",
    "세탁하기",
    "방 청소하기",
    "유튜브 보기",
    "넷플릭스 보기"
]
labels = ["high", "high", "medium", "medium", "low", "low"]

# 1) 텍스트 → 벡터
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# 2) Naive Bayes 훈련
model = MultinomialNB()
model.fit(X, labels)

# 3) 예측 함수
def predict_priority(text):
    X_test = vectorizer.transform([text])
    return model.predict(X_test)[0]

