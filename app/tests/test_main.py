import pytest
import sys
import os

# Adiciona o diretório raiz ao sys.path para permitir importações corretas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from main import app  # Agora o pytest pode encontrar o main.py

@pytest.fixture
def client():
    """Cria um cliente de teste para a API Flask."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    """Verifica se a API está rodando e retorna 200 ou 404 para a rota raiz."""
    response = client.get('/')
    assert response.status_code in [200, 404]  # Aceita 200 caso o Swagger esteja sendo servido na raiz


def test_etl_endpoint(client, mocker):
    """Testa o endpoint /etl/run-etl."""
    mock_result = {"message": "ETL process completed", "data": []}
    
    # Simula a resposta do ETLService para evitar execuções reais
    mocker.patch("app.core.etl_service.ETLService.run", return_value=[])

    response = client.post('/etl/run-etl')
    assert response.status_code == 201
    assert response.json == mock_result
