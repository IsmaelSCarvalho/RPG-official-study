from personagens.personagem import Personagem
from personagens.atributosficha import AtributosFicha
from personagens.atributo import Atributo

class Guerreiro(Personagem):
    def __init__(self, nome: str):

        atributos_guerreiro = AtributosFicha(forca=10, defesa=15, hp_max=100, sabedoria=0)

        super().__init__(nome=nome, classe="Guerreiro Alado", atributo=atributos_guerreiro)

        self.furia = Atributo("Furia", 13)

    def mostrar(self):

        super().mostrar()

        print(f"Furia: {self.furia.total} ")
        print("=" * 20)


