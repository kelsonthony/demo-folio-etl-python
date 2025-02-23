from flask import jsonify
from flask_restx import Namespace, Resource
from app.core.etl_service import ETLService

# Criando um namespace para agrupar os endpoints
etl_ns = Namespace("ETL", description="Operações relacionadas ao processo ETL")

@etl_ns.route('/run-etl')
class RunETL(Resource):
    def post(self):
        """
        Executa o processo ETL.
        ---
        tags:
          - ETL
        responses:
          201:
            description: ETL processado com sucesso
            schema:
              properties:
                message:
                  type: string
                  example: "ETL process completed"
                data:
                  type: array
                  items:
                    type: object
        """
        etl = ETLService()
        result = etl.run()
        return jsonify({"message": "ETL process completed", "data": result}), 201
