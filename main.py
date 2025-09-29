import sys
from PyQt5.QtWidgets import QApplication
from telas.TelaPrincipal import TelaPrincipal


app = QApplication(sys.argv)
janela = TelaPrincipal()
janela.show()
sys.exit(app.exec_())