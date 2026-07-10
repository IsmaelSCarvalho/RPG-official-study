class Atributo:
    def __init__(self, nome: str, valor_base: int):
        self.nome = nome

        # Valor natural do personagem
        self.base = valor_base

        # Equipamento (espadas, armaduras, anéis...)
        self.bonus = 0

        # Magias, venenos, buffs, debuffs...
        self.temporario = 0

    @property
    def total(self):
        return self.base + self.bonus + self.temporario

    def adicionar_bonus(self, valor):
        self.bonus += valor

    def adicionar_temporario(self, valor):
            self.temporario += valor

    def remover_bonus(self, valor):
        self.bonus -= valor

    def remover_temporario(self, valor):
        self.temporario -= valor

    def limpar_temporario(self):
        self.temporario = 0
