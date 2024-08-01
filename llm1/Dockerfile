FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install fastapi uvicorn
CMD ["uvicorn", "model_server:app", "--host", "0.0.0.0", "--port", "8001"]  # llm2에서는 포트 8002로 설정
