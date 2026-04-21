import os
import requests
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

# Agora ele puxa as chaves de forma invisível e segura
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def enviar_mensagem_telegram(texto):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    
    pack = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": texto,
        "parse_mode": "Markdown"
    }
    
    response = requests.post(url, json=pack)
    
    if response.status_code == 200:
        print("📱 Notificação enviada para o Telegram com sucesso!")
    else:
        print(f"❌ Erro ao enviar para o Telegram: {response.text}")

def buscar_noticias_com_ia():
    tavily = TavilyClient(api_key=TAVILY_API_KEY)
    
    minha_carteira = ["PETR4", "NUBANK", "NVIDIA", "bitcoin", "ethereum"]
    acoes_texto = ", ".join(minha_carteira)
    
    print(f"🤖 Acionando a IA do Tavily para ler sobre: {acoes_texto}...")

    pergunta_ia = f"Resuma as principais notícias de hoje focadas EXCLUSIVAMENTE nos seguintes ativos: {acoes_texto}. Ignore o resto do mercado. Escreva o resumo OBRIGATORIAMENTE em Português do Brasil (PT-BR)."

    resposta = tavily.search(
        query=pergunta_ia,
        topic="news",
        search_depth="advanced",
        include_answer=True,
        max_results=4,
        include_domains=["infomoney.com.br", "valor.globo.com", "exame.com"]
    )

    resumo = resposta['answer']
    print("\n📰 Resumo da carteira gerado. Disparando para o Telegram...")
    
    mensagem_final = f"📊 *InvesNote - Radar da Sua Carteira*\n🎯 Ativos: {acoes_texto}\n\n{resumo}"
    
    enviar_mensagem_telegram(mensagem_final)

if __name__ == "__main__":
    buscar_noticias_com_ia()