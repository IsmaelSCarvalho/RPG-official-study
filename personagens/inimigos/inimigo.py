from personagens.personagem import Personagem
from personagens.atributosficha import AtributosFicha

class Inimigo(Personagem):
    def __init__(self, nome: str, atributo: AtributosFicha, exp_recompensa: int):
        # Passa os dados obrigatórios para a classe mãe universal (Personagem)
        super().__init__(nome=nome, classe="Monstro", atributo=atributo)

        # Atributos específicos que só inimigos têm (recompensas)
        self.exp_recompensa = exp_recompensa
        self.tipo = "Monstro"