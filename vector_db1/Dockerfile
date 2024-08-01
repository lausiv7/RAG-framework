FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install fastapi uvicorn
CMD ["uvicorn", "db_server:app", "--host", "0.0.0.0", "--port", "8003"]  # vector_db2에서는 포트 8004로 설정
