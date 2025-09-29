from produto import Produto
from categoria import Categoria

class Notebook(Produto):
    
    def __init__(self, modelo: str, cor: str, preco: float, categoria: Categoria, tempoDeBateria: str):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempoDeBateria = tempoDeBateria

    @property
    def tempoDeBateria(self):
        return self.__tempoDeBateria

    @tempoDeBateria.setter
    def tempoDeBateria(self, tempo: str):
        self.__tempoDeBateria = tempo

    def getInformacoes(self) -> str:
        info_base = super().getInformacoes()
        return f"{info_base}\nTempo de Bateria: {self.tempoDeBateria}"

    def cadastrar(self):
        print(f"O notebook modelo '{self.modelo}' foi cadastrado com sucesso!")
        return f"Notebook '{self.modelo}' cadastrado!"