from personagens.personagem import Personagem
from personagens.atributosficha import AtributosFicha
from personagens.atributo import Atributo


class Mago(Personagem):
    def __init__(self, nome: str):
        # Criamos o pacote de atributos básicos do Mago
        atributos_mago = AtributosFicha(forca=5, defesa=10, hp_max=100, sabedoria=15, velocidade=0)

        # Passamos para a classe mãe
        super().__init__(nome=nome, classe="Mago de Gelo", atributo=atributos_mago)

        self.atributo_desarmado = "sabedoria"
        self.dano_desarmado = "1d6"

        # Adicionamos a mana exclusiva do Mago
        self.mana = Atributo("Mana", 80)

    def mostrar(self):

        # Chamamos o mostrar da classe mãe para exibir Nome, Força, Defesa e vida
        super().mostrar()

        # Adicionamos o print exclusivo da mana do Mago
        print(f"Mana: {self.mana.total} ")
        print("=" * 20)