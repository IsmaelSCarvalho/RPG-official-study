from itens.item import Item

class Arma(Item):
    def __init__(
            self,
            nome,
            peso,
            valor,
            dano,
            atributo,
            alcance="Corpo a corpo"

    ):

        super().__init__(nome, peso, valor)

        self.dano = dano
        self.atributo = atributo
        self.alcance = alcance
    def mostrar(self):

        print("=" * 40)
        print(f"Item........: {self.nome}")
        print(f"Dano........: {self.dano} ")
        print(f"Atributos...: {self.atributo} ")
        print(f"Alcance.....: {self.alcance} ")
        print(f"Peso........: {self.peso} ")
        print(f"Valor.......: {self.valor} ")
        print("=" * 40)