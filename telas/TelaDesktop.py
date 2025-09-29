from PyQt5.QtWidgets import *

class TelaDesktop(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QFormLayout()

        self.modelo_input = QLineEdit()
        self.cor_input = QLineEdit()
        self.preco_input = QLineEdit()
        self.categoria_input = QLineEdit()
        self.potencia_input = QLineEdit()
        self.botao_cadastrar = QPushButton("Cadastrar Desktop")

        layout.addRow(QLabel("Modelo:"), self.modelo_input)
        layout.addRow(QLabel("Preço (R$):"), self.preco_input)
        layout.addRow(QLabel("Cor:"), self.cor_input)
        layout.addRow(QLabel("Categoria:"), self.categoria_input)
        layout.addRow(QLabel("Potência da Fonte (W):"), self.potencia_input)
        layout.addRow(self.botao_cadastrar)

        self.setLayout(layout)