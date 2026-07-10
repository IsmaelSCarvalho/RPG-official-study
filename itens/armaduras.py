from itens.armadura import Armadura

class ArmaduraCouro(Armadura):
    def __init__(self):
        super().__init__(
            nome="Armadura de Couro",
            valor=35,
            peso=2,
            defesa_fisica=15,
            defesa_magica=2
        )

class ArmaduraFerro(Armadura):
    def __init__(self):
        super().__init__(
            nome="Armadura de Ferro",
            valor=60,
            peso=6,
            defesa_fisica=18,
            defesa_magica=4
        )

class ArmaduraMithril(Armadura):
    def __init__(self):
        super().__init__(
            nome="Armadura de Mithril",
            valor=35,
            peso=2,
            defesa_fisica=2,
            defesa_magica=15
        )

class ArmaduraDiamante(Armadura):
    def __init__(self):
        super().__init__(
            nome="Armadura de Diamante",
            valor=60,
            peso=6,
            defesa_fisica=4,
            defesa_magica=18

        )
