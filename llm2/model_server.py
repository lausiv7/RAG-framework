from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    prompt = data["prompt"]
    # 여기에 LLM 모델 로직 추가
    response = {"generated_text": f"응답 for prompt: {prompt}"}
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)  # llm2에서는 포트 8002로 설정
