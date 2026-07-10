from personagens.personagem import Personagem
from personagens.atributosficha import AtributosFicha
from personagens.atributo import Atributo

class Arqueiro(Personagem):
    def __init__(self, nome: str):

        atributos_arqueiro = AtributosFicha(forca=7, defesa=12, hp_max=100, sabedoria=2, velocidade=13)

        super().__init__(nome=nome, classe="Flecha das Sobras", atributo=atributos_arqueiro)

        self.atributo_desarmado = "velocidade"
        self.dano_desarmado = "1d5"

        self.velocidade = Atributo("visao", 25)

    def mostrar(self):

        # Chamamos o mostrar da classe mãe para exibir Nome, Força, Defesa e vida
        super().mostrar()

        # Adicionamos o print exclusivo da mana do Mago
        print(f"Velocidade: {self.velocidade.total} ")
        print("=" * 20)