from tavily import TavilyClient

class TavilyService:
    
    def __init__(self, api_key: str):
        self._client = TavilyClient(api_key=api_key)
       
        
    def search_news(self, my_wallet: list[str], general_topics: list[str]) -> str:
      question_ia = self._build_prompt(my_wallet, general_topics)
      response = self._client.search(
            query=question_ia,
            topic="news",
            search_depth= "advanced",
            include_answer=True,
            max_results=5,
            include_domains=["infomoney.com.br", "valor.globo.com", "exame.com"]
        )
      return response.get("answer", "Nenhuma notícia encontrada para esses ativos.")
    
    def _build_prompt(self, my_wallet: list[str], general_topics: list[str]) -> str:
        actions_text = ", ".join(my_wallet + general_topics)
        question_ia = f"Faça um briefing executivo sobre hoje. Dê destaque especial aos ativos: {', '.join(my_wallet)}. Além disso, resuma as movimentações mais importantes em {', '.join(general_topics)}. Escreva em Português (PT-BR) de forma direta e em tópicos."
        return question_ia
      
