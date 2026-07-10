from personagens.atributo import Atributo

class AtributosFicha:
    def __init__(self, forca: int, defesa: int, hp_max: int, sabedoria: int, velocidade: int):
        # Usamos a classe Atributo que você criou no primeiro dia!
        self.forca = Atributo("Força", forca)
        self.defesa = Atributo("Defesa", defesa)
        self.hp = Atributo("Vida", hp_max)
        self.sabedoria = Atributo("Sabedoria", sabedoria)
        self.velocidade = Atributo("Velocidade", velocidade)
