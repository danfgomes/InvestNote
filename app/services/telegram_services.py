import requests

class TelegramService:

  def __init__(self, token: str, chat_id: str):
      self._token = token
      self._chat_id = chat_id

  def send_notification(self, text: str):
     message = self._format_message(text)

     message_format = {
        "chat_id": self._chat_id,
        "text": message,
        "parse_mode": "Markdown"
     }
     url = f"https://api.telegram.org/bot{self._token}/sendMessage"

     requests.post(url, json=message_format)
     
    

  def _format_message(self, text: str) -> str:
     return f"*InvesNote - Radar da Sua Carteira*\n\n{text}"