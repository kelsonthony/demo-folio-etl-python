import requests
from app.ports.api_port import ApiPort
from app.config.settings import API_URL, HEADERS
import json

class ApiClient(ApiPort):
    def send_user(self, user_json):
        try:
            # Convertendo JSON para string formatada corretamente
            payload = json.dumps(user_json)

            # Enviando a requisição POST para a API
            response = requests.post(API_URL, data=payload, headers=HEADERS)

            # Log para depuração
            print(f"\n[LOG] Enviando usuário: {user_json['username']}")
            print(f"[LOG] Payload Enviado: {payload}")
            print(f"[LOG] Status Code: {response.status_code}")
            print(f"[LOG] Resposta da API: {response.text}\n")

            return response.status_code, response.json() if response.status_code == 201 else response.text
        except Exception as e:
            print(f"[ERRO] Falha ao enviar usuário {user_json['username']}: {e}")
            return 500, str(e)
