import os
from dotenv import load_dotenv
from fastapi import FastAPI
from app.services.tavily_service import TavilyService
from app.services.telegram_services import TelegramService
from pydantic import BaseModel

load_dotenv()

app = FastAPI()

class ResumoRequest(BaseModel):
    tavily_key: str
    telegram_token: str
    chat_id: str
    carteira: list[str]
    temas: list[str]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/resumo")
def get_resume(pedido: ResumoRequest):
    TavilyService = TavilyService(api_key=os.getenv("TAVILY_API_KEY"))
    TelegramService = TelegramService(token=pedido.telegram_token, chat_id=pedido.chat_id)

    resumo = TavilyService.search_news(my_wallet=pedido.carteira, general_topics=pedido.temas)
    TelegramService.send_notification(resumo)
    return {"message": "Resumo gerado e enviado para o Telegram com sucesso!"}