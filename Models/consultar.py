import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from .conexao import Conexao as db

class Consulta:
    def __init__(self):
        self.conexao = db()

    def consultar_produto(self, cod_produto):
        conn = self.conexao.conectar_banco()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produto WHERE cod_produto = ?", (cod_produto,))
        resultado = cursor.fetchone()
        conn.close()
        return resultado

    def consultar_endereco(self, cod_endereco):
        conn = self.conexao.conectar_banco()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM endereco WHERE cod_endereco = ?", (cod_endereco,))
        resultado = cursor.fetchone()
        conn.close()
        return resultado

    def consultar_estoque(self, produto=None, endereco=None):

        conn = self.conexao.conectar_banco()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT produto.nome_produto, endereco.cod_endereco, quantidade
            FROM estoque
            JOIN produto ON estoque.id_produto = produto.id_produto
            JOIN endereco ON estoque.id_endereco = endereco.id_endereco
            WHERE produto.nome_produto = ? OR endereco.cod_endereco = ?
            """,
            (produto, endereco)
        )
        resultado = cursor.fetchall()
        conn.close()
        return resultado

    def atualizar_estoque(self, nome_produto, cod_endereco, quantidade):
        conn = self.conexao.conectar_banco()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE estoque
            SET quantidade = ?
            WHERE id_produto = (SELECT id_produto FROM produto WHERE cod_produto = ?)
            AND id_endereco = (SELECT id_endereco FROM endereco WHERE cod_endereco = ?)
        """, (quantidade, nome_produto, cod_endereco))

        conn.commit()
        conn.close()


        