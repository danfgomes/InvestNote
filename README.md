# InvesNote - AI Financial Assistant

O **InvesNote** é um assistente financeiro automatizado projetado para monitorar ativos específicos (Ações e Criptomoedas) e entregar resumos inteligentes diretamente no Telegram do usuário. 

Este projeto faz parte de uma arquitetura de microserviços que integra Inteligência Artificial para filtragem de notícias e automação de mensageria.

## Funcionalidades
- **Monitoramento Personalizado:** Busca notícias apenas dos ativos presentes na sua carteira (ex: PETR4, Bitcoin, Ethereum).
- **Inteligência Artificial:** Utiliza a API do Tavily para ler, filtrar e resumir as notícias mais relevantes do mercado brasileiro (B3) e cripto.
- **Notificações Real-time:** Envio de alertas formatados via Telegram Bot.


## Tecnologias Utilizadas
- **Linguagem:** Python 3.12
- **IA/Busca:** Tavily AI
- **Mensageria:** Telegram Bot API
- **Gestão de Dependências:** Poetry

