# controller/controle_estoque.py
from controller.leitor import Leitor
from Models.consultar import Consulta

class ControleEstoque:
    def __init__(self):
        self.model = Consulta()
        self.leitor = Leitor()

    def consultar_por_etiqueta(self, produto=None, endereco=None):
        return self.model.consultar_estoque(produto=produto, endereco=endereco)
    
    def insert_estoque(self, produto, endereco, quantidade):
        return self.model.atualizar_estoque(
            nome_produto=produto,
            cod_endereco=endereco,
            quantidade=quantidade
        )

