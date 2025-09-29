from produto import Produto
from categoria import Categoria

class Desktop(Produto):
    def __init__(self, modelo: str, cor: str, preco: float, categoria: Categoria, potenciaDaFonte: int):
        super().__init__(modelo, cor, preco, categoria)
        self._potenciaDaFonte = potenciaDaFonte

    @property
    def potenciaDaFonte(self):
        return self._potenciaDaFonte

    @potenciaDaFonte.setter
    def potenciaDaFonte(self, valor: int):
        if valor > 0:
            self._potenciaDaFonte = valor
        else:
            print("A potência da fonte deve ser um valor positivo.")

    def getInformacoes(self) -> str:
        info_base = super().getInformacoes()
        return f"{info_base}\nPotência da Fonte: {self.potenciaDaFonte}W"

    def cadastrar(self):
        print(f"O desktop modelo '{self.modelo}' foi cadastrado com sucesso!")
        return f"Desktop '{self.modelo}' cadastrado!"