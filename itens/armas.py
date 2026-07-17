from itens.arma import Arma

class EspadaMadeira(Arma):
    def __init__(self):
        super().__init__(
            nome="Espada de Madeira",
            peso=2,
            valor=50,
            dano="1d6",
            atributo="forca"
        )

class EspadaLonga(Arma):
    def __init__(self):
        super().__init__(
            nome="Espada Longa",
            peso=3,
            valor=70,
            dano="1d8",
            atributo="forca"

        )

class Cajado(Arma):
    def __init__(self):
        super().__init__(
            nome="Cajado do Infinito",
            peso=2,
            valor=45,
            dano="1d6",
            atributo="sabedoria"
        )

class Adaga(Arma):
    def __init__(self):
        super().__init__(
            nome="Adaga Fina",
            peso=0.5,
            valor=50,
            dano="1d4",
            atributo="agilidade"
        )

class ArcoCurto(Arma):
    def __init__(self):
        super().__init__(
            nome="ArcoCurto",
            peso=1,
            valor=60,
            dano="1d6",
            atributo="agilidade",
            alcance="A distancia (15 metros)"
        )