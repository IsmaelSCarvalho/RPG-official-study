from itens.item import Item

class Armadura(Item):
    def __init__(self, nome, peso, valor, defesa_fisica, defesa_magica):


        super().__init__(nome, peso, valor)

        self.defesa_fisica = defesa_fisica
        self.defesa_magica = defesa_magica

    def mostrar(self):

        print("=" * 40)
        print(f"Item...........: {self.nome}")
        print(f"peso...........: {self.peso}")
        print(f"valor..........: {self.valor}")
        print(f"defesa_fisica..: {self.defesa_fisica}")
        print(f"defesa_magica..: {self.defesa_magica}")
        print("=" * 40)