from flask import Flask, jsonify
from app.core.etl_service import ETLService

app = Flask(__name__)

@app.route('/run-etl', methods=['POST'])
def run_etl():
    """
    Endpoint para executar o processo ETL.
    Retorna o status de cada usuário processado.
    """
    etl = ETLService()
    result = etl.run()
    return jsonify({"message": "ETL process completed", "data": result}), 201

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)
