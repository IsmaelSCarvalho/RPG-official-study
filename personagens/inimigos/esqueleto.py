from personagens.inimigos.inimigo import Inimigo
from personagens.atributosficha import AtributosFicha

class Esqueleto(Inimigo):
    def __init__(self, identificador: str):

        atributos_esqueleto = AtributosFicha(
            forca=6,
            defesa=9,
            hp_max=100,
            sabedoria=3,
            velocidade=4
        )

        nome_completo = f"Esqueleto {identificador}".strip()

        super().__init__(
            nome=nome_completo,
            atributo=atributos_esqueleto,
            exp_recompensa=35
        )
