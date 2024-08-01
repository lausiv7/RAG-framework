from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/search")
async def search(request: Request):
    data = await request.json()
    query = data["query"]
    # 여기에 벡터 DB 검색 로직 추가
    response = {"results": [{"content": f"검색 결과 for query: {query}"}]}
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8004)  # vector_db2에서는 포트 8004로 설정
