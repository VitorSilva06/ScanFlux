from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import uic
import sys
import cv2
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controller.leitor import Leitor
from controller.consultar import ControleEstoque

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("interface.ui", self)
        self.btnConsultar.clicked.connect(self.abrir_consulta)
        self.btnInventario.clicked.connect(self.abrir_inventario)
        self.btnLerEtiqueta_2.clicked.connect(self.ler_endereco)
        self.lerProduto.clicked.connect(self.ler_produto)
        self.btnExeConsulta.clicked.connect(self.resultado)
        self.btnInventariar.clicked.connect(self.fazer_inventario)

    def abrir_consulta(self):
        """Exibe o frame de consulta e oculta o de inventário"""
        self.qtdLabel.setVisible(False)
        self.numQtd.setVisible(False)
        self.qtdLabel.setVisible(False)
        self.btnInventariar.setVisible(False)
        self.btnExeConsulta.setVisible(True)

    def abrir_inventario(self):
        """Exibe o frame de inventário e oculta o de consulta"""
        self.btnExeConsulta.setVisible(False)
        self.numQtd.setVisible(True)
        self.qtdLabel.setVisible(True)
        self.btnInventariar.setVisible(True)

    def ler_endereco(self):
        leitor = Leitor()
        resultado = leitor.ler_codigo_barras_camera()
        if resultado:
            self.endereco_lido = resultado
            self.lerLabel_2.setText(f"Endereço: {resultado}")
        else:
            QMessageBox.warning(self, "Erro", "Não foi possível ler o endereço.")
        return resultado

    def ler_produto(self):
        leitor = Leitor()
        resultado = leitor.ler_codigo_barras_camera()
        if resultado:
            self.produto_lido = resultado
            self.labelProduto.setText(f"Produto: {resultado}")
        else:
            QMessageBox.warning(self, "Erro", "Não foi possível ler o produto.")
        
        return resultado


    def resultado(self):
        controle = ControleEstoque()
        dados = controle.consultar_por_etiqueta(
            produto=getattr(self, 'produto_lido', None),
            endereco=getattr(self, 'endereco_lido', None)
        )

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['Produto', 'Endereço', 'Quantidade'])

        for linha in dados:
            itens = [QStandardItem(str(campo)) for campo in linha]
            model.appendRow(itens)

        self.tableView.setModel(model)

    def fazer_inventario(self): 
        try:
            qtd = int(self.numQtd.text())  # Se for QLineEdit
        except ValueError:
            QMessageBox.warning(self, "Erro", "Quantidade inválida.")
            return

        produto = getattr(self, 'produto_lido', None)
        endereco = getattr(self, 'endereco_lido', None)

        if not produto or not endereco:
            QMessageBox.warning(self, "Erro", "Você precisa ler o produto e o endereço primeiro.")
            return

        if qtd <= 0:
            QMessageBox.warning(self, "Erro", "Quantidade deve ser maior que zero.")
            return

        controle = ControleEstoque()
        controle.insert_estoque(produto=produto, endereco=endereco, quantidade=qtd)

        QMessageBox.information(self, "Sucesso", "Inventário registrado com sucesso.")

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
