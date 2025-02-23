from flask import Flask
from flask_restx import Api
from app.controllers.etl_controller import etl_ns

app = Flask(__name__)


# Configuração do Swagger
api = Api(app, version="1.0", title="ETL API",
          description="API para execução do processo ETL")

# Registrando o namespace do ETL
api.add_namespace(etl_ns, path='/etl')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)
