import sys
from PyQt5.QtWidgets import *
from categoria import Categoria
from desktop import Desktop
from notebook import Notebook
from .TelaDesktop import TelaDesktop
from .TelaNotebook import TelaNotebook


class TelaPrincipal(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sisteminha de Cadastro de Computadores")
        self.setGeometry(150, 150, 550, 450)

        self.abas = QTabWidget()
        self.setCentralWidget(self.abas)

        self.tela_desktop = TelaDesktop()
        self.tela_notebook = TelaNotebook()

        self.abas.addTab(self.tela_desktop, "Cadastrar Desktop")
        self.abas.addTab(self.tela_notebook, "Cadastrar Notebook")
        
        self.tela_desktop.botao_cadastrar.clicked.connect(self.cadastrar_desktop)
        self.tela_notebook.botao_cadastrar.clicked.connect(self.cadastrar_notebook)

    def cadastrar_desktop(self):
        try:
            modelo = self.tela_desktop.modelo_input.text()
            cor = self.tela_desktop.cor_input.text()
            preco = float(self.tela_desktop.preco_input.text())
            categoria_nome = self.tela_desktop.categoria_input.text()
            potencia = int(self.tela_desktop.potencia_input.text())

            if not all([modelo, cor, categoria_nome]):
                raise ValueError("Todos os campos de texto devem ser preenchidos.")

            categoria_obj = Categoria(id=1, nome=categoria_nome)
            desktop = Desktop(modelo, cor, preco, categoria_obj, potencia)
            status = desktop.cadastrar()
            info = desktop.getInformacoes()

            QMessageBox.information(self, "Cadastro Realizado", f"{status}\n\n---\n{info}")      # truquezinho pro espaçamento no popup quando cria o produto

            for campo in [self.tela_desktop.modelo_input, self.tela_desktop.cor_input, 
                          self.tela_desktop.preco_input, self.tela_desktop.categoria_input, 
                          self.tela_desktop.potencia_input]:
                campo.clear()

        except ValueError:
            QMessageBox.warning(self, "ERRO", "Verifica ai se o preço e a potência são números e se todos os campos estão preenchidos.")
        except Exception as e:
            QMessageBox.critical(self, "ERRO", f"Ocorreu algum erro esquisito ai: {e}")

    def cadastrar_notebook(self):
        try:
            modelo = self.tela_notebook.modelo_input.text()
            cor = self.tela_notebook.cor_input.text()
            preco = float(self.tela_notebook.preco_input.text())
            categoria_nome = self.tela_notebook.categoria_input.text()
            bateria = self.tela_notebook.bateria_input.text()

            if not all([modelo, cor, categoria_nome, bateria]):
                raise ValueError("Preencha todos os campos.")

            categoria_obj = Categoria(id=2, nome=categoria_nome)
            notebook = Notebook(modelo, cor, preco, categoria_obj, bateria)
            status = notebook.cadastrar()
            info = notebook.getInformacoes()

            QMessageBox.information(self, "Cadastro Realizado", f"{status}\n\n---\n{info}")

            for attr_name in dir(self.tela_notebook):
                attr = getattr(self.tela_notebook, attr_name)       # outra maneira do clear dos campos (mais recomendavel)
                if isinstance(attr, QLineEdit):
                    attr.clear()

        except ValueError:
            QMessageBox.warning(self, "ERRO", "Verifica ai se o preço é um número e se todos os campos estão preenchidos.")
        except Exception as e:
            QMessageBox.critical(self, "ERRO", f"Ocorreu algum erro esquisito ai: {e}")