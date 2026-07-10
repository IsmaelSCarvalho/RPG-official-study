from personagens.personagem import Personagem
from personagens.atributosficha import AtributosFicha

class Esqueleto(Personagem):
    def __init__(self):

        atributos_esqueleto = AtributosFicha(
            forca=6,
            defesa=9,
            hp_max=100
        )
        super().__init__(
            nome="Esqueleto",
            classe="Monstro",
            atributo=atributos_esqueleto
        )
