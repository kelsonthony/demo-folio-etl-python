from app.adapters.excel_reader import ExcelReader
from app.adapters.api_client import ApiClient
from app.core.user_model import User

class ETLService:
    def __init__(self):
        self.excel_reader = ExcelReader()
        self.api_client = ApiClient()

    def run(self):
        users_data = self.excel_reader.read_users()
        results = []
        
        for row in users_data:
            user = User(row)  # Converte a linha do Excel para objeto User
            user_json = user.to_json()  # Transforma em JSON
            
            # Enviar UM usuário por vez
            status, response = self.api_client.send_user(user_json)

            # Armazena o resultado
            results.append({
                "username": user.username,
                "status": status,
                "response": response
            })

        return results  # Retorna o resultado de todas as requisições
