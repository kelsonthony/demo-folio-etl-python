import pandas as pd
from app.ports.excel_port import ExcelPort
from app.config.settings import EXCEL_FILE_PATH

class ExcelReader(ExcelPort):
    def read_users(self):
        df = pd.read_excel(EXCEL_FILE_PATH)
        return df.to_dict(orient="records")
