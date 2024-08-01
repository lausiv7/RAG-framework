RAG Architecture Model은 다음과 같이 사용자의 질문을 받아서, 
Framework가 Vector DB에서 Semantic Search로 Contextual Data를 받고, 
이를 LLM에 Prompt로 질문하여 그 처리 결과를 받아서 최종 사용자에게 전달하게 됩니다. 
이 Famework는 여러 LLM과 Vector DB로 부터도 처리할 수 있게 확장할 것 입니다.
Docker Composer로 1대의 Framwork, 멀티 LLM, 멀티 DB로 각각 생성하고 Framework를 중심으로 Link하는 예제 코드와 실행 방법

rag-architecture/
├── docker-compose.yml
├── framework/
│   ├── Dockerfile
│   ├── app.py
├── llm1/
│   ├── Dockerfile
│   ├── model_server.py
├── llm2/
│   ├── Dockerfile
│   ├── model_server.py
├── vector_db1/
│   ├── Dockerfile
│   ├── db_server.py
├── vector_db2/
│   ├── Dockerfile
│   ├── db_server.py


![image](https://github.com/user-attachments/assets/0b2d6d09-3131-440d-8c8f-456dd90f7d5b)



https://aws.amazon.com/ko/blogs/tech/multi-rag-and-multi-region-llm-for-chatbot/
https://medium.com/@bijit211987/advanced-rag-for-llms-slms-5bcc6fbba411
