class Categoria:
    
    def __init__(self, id: int, nome: str):
        self.id = id
        self.nome = nome

    def __str__(self):                              # retorna a representacao em string
        return f"({self.id}) {self.nome}"