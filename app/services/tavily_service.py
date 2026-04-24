from tavily import TavilyClient

class TavilyService:
    
    def __init__(self, api_key: str):
        self.client = TavilyClient(api_key=api_key)
       
        
    def search_news(self, my_wallet: list[str], general_topics: list[str]) -> str:
      actions_text = ", ".join(my_wallet + general_topics)
      question_ia = f"Resuma as principais notícias de hoje focadas EXCLUSIVAMENTE nos seguintes ativos: {actions_text}. Ignore o resto do mercado. Escreva o resumo OBRIGATORIAMENTE em Português do Brasil (PT-BR)."
      response = self.client.search(
            query=question_ia,
            topic="news",
            search_depth= "advanced",
            include_answer=True,
            max_results=5,
            include_domains=["infomoney.com.br", "valor.globo.com", "exame.com"]
        )
      
      return response.get("answer", "Nenhuma notícia encontrada para esses ativos.")
