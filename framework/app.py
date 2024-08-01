from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

LLM_ENDPOINTS = ["http://llm1:8001/generate", "http://llm2:8002/generate"]
DB_ENDPOINTS = ["http://vector_db1:8003/search", "http://vector_db2:8004/search"]

@app.post("/query")
def query_rag(query: str):
    try:
        # Vector DB에서 데이터 검색
        search_results = []
        for db_endpoint in DB_ENDPOINTS:
            response = requests.post(db_endpoint, json={"query": query})
            search_results.extend(response.json()["results"])

        # LLM에 프롬프트 전달
        contextual_data = " ".join([result["content"] for result in search_results])
        llm_responses = []
        for llm_endpoint in LLM_ENDPOINTS:
            response = requests.post(llm_endpoint, json={"prompt": contextual_data})
            llm_responses.append(response.json())

        return {"results": llm_responses}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
