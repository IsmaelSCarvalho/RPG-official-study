from personagens.atributosficha import AtributosFicha
from sistemas.inventario import Inventario
from time import sleep

class Personagem:
    def __init__(self, nome: str, classe: str, atributo: AtributosFicha):
        self.nome = nome
        self.classe = classe
        self.atributos = atributo  # Isso é COMPOSIÇÃO
        self.inventario = Inventario()
        self.atributo_desarmado = "forca"
        self.dano_desarmado = "1d4"
        self.arma = None
        self.armadura = None

    def equipar_arma(self):
        print(f"\n{self.nome} está abrindo a mochila...")
        sleep(1)
        arma_escolhida = self.inventario.escolher_arma()

        if arma_escolhida:
            self.arma = arma_escolhida
            print(f" ⚔️ {self.nome} Equipou com sucesso: {arma_escolhida.nome}!")

    def equipar_armadura(self):
        armadura_escolhida = self.inventario.escolher_armadura()

        if armadura_escolhida:
            self.armadura = armadura_escolhida
            print(f" 🛡️ {self.nome} equipou {armadura_escolhida.nome}!")

    def receber_dano(self, quantidade_dano: int) -> int:
        self.atributos.hp.base -= quantidade_dano

        if self.atributos.hp.base <=0:
            self.atributos.hp.base = 0

        return quantidade_dano


    def mostrar(self):

        print("=" * 20)
        print(f"Nome: {self.nome}")
        print(f"Classe: {self.classe}")
        # Acessamos o .total que criamos usando o @property!
        print(f"Força: {self.atributos.forca.total}")
        print(f"Defesa: {self.atributos.defesa.total}")
        print(f"Vida: {self.atributos.hp.total}")
        if self.arma:
            print(f" ⚔️ Arma equipada: {self.arma.nome} (Dano: {self.arma.dano})")
        else:
            print(f" ⚔️ Arma equipada: Punhos (Dano: 1)")

        if self.armadura:
            print(f" 🛡️ Armadura equipada: {self.armadura.nome} (Defesa: {self.armadura.defesa_fisica}/{self.armadura.defesa_magica})")
        else:
            print(" 🛡️ Armadura equipada: Nenhuma (Roupas comuns)")
        print("=" * 20)