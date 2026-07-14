from personagens.personagem import Personagem
from personagens.atributosficha import AtributosFicha
from personagens.atributo import Atributo

class Guerreiro(Personagem):
    def __init__(self, nome: str):

        self.furia_total = None
        atributos_guerreiro = AtributosFicha(forca=10, defesa=15, hp_max=100, sabedoria=0, velocidade=1)

        super().__init__(nome=nome, classe="Guerreiro Alado", atributo=atributos_guerreiro)

        self.atributo_desarmado = "forca"
        self.dano_desarmado = "1d5"

        self.furia = Atributo("Furia", 13)

    def modo_furia(self, alvo):
        custo_furia = 5

        if self.furia.total < custo_furia:
            print(f"❌ {self.nome} Guerreiro sem inspiração! (Restante: {self.furia.total})")
            return 0  # Retorna 0 indicando que a magia falhou

        self.furia.base -= custo_furia

        modificador_forca = self.atributos.forca.total
        dano_fisico = 13 + modificador_forca

        print(f"\n👊 {self.nome} salta em direção ao mostro no seu [Modo Furia] como uma bola de fogo cai sobre o monstro!")
        print(f"✨ Gastou {custo_furia} de Furia! Furia restante: {self.furia.base}")

        dano_sofrido = alvo.receber_dano(dano_fisico)

        print(f"💥 O soco esmaga {alvo.nome} causando {dano_sofrido} de dano fisico instantâneo!")

        return dano_sofrido

    def mostrar(self):

        super().mostrar()

        print(f"Furia: {self.furia.total} ")
        print("=" * 20)


