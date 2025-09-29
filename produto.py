from abc import ABC, abstractmethod
from categoria import Categoria

class Produto(ABC):
    
    def __init__(self, modelo: str, cor: str, preco: float, categoria: Categoria):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = categoria

    def getInformacoes(self) -> str:
        return (
            f"Modelo: {self.modelo}\n"
            f"Cor: {self.cor}\n"
            f"Preço: R$ {self.preco:.2f}\n"
            f"Categoria: {self.categoria.nome}"
        )

    @abstractmethod
    def cadastrar(self):
        pass