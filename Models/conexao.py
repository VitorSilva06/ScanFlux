import sqlite3

class Conexao:
    def __init__(self, db_name="estoque.db"):
        self.db_name = db_name

    def conectar_banco(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            return self.conn
        except Exception as erro:
            print(f"Erro ao conectar: {erro}")
            return None
