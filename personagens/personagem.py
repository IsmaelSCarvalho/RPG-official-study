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
        self.ouro = 0
        self.xp = 0
        self.nivel = 1

    def ganhar_recompensa(self, ouro,xp):
        self.ouro += ouro
        self.xp += xp
        print(f"\n💰 {self.nome} coletou {ouro} de ouro")
        print(f"✨ {self.nome} ganhou {xp} de experiência")

        # Loop para garantir que suba múltiplos níveis se ganhar muita XP de uma vez
        while self.xp >= self.nivel * 100:
            self.xp -= self.nivel * 100
            self.nivel += 1
            self.subir_de_nivel()

    def subir_de_nivel(self):
        """Executa a subida de nível, recupera a vida e melhora os atributos."""
        print("\n" + "🌟 " * 15)
        print(f"   🆙 SUBIU DE NÍVEL! {self.nome} agora é Nível {self.nivel}!   ")
        print("🌟 " * 15)

        # 1. Crescimento de Atributos baseado na classe
        if self.classe == "mago de gelo":
            # Magos ganham mais inteligência/sabedoria e mana
            self.atributos.sabedoria.base += 2
            self.atributos.hp.base += 5 # Aumenta o HP máximo
            if hasattr(self, "mana"):
                self.mana.base += 5 # Aumenta a mana máxima
            print("📈 Atributos aumentados: Sabedoria +2, HP Máximo +5, Mana Máxima +5!")

        else:
            self.atributos.forca.base += 2
            self.atributos.defesa.base += 5
            self.atributos.hp.base += 5
            print("📈 Atributos aumentados: Força +2, Defesa +5, HP Máximo +5!")

        # 2. Cura total de brinde ao subir de nível!
        # Como o HP máximo é ditado pelo .total, recuperamos a base para o valor cheio
        print(f"❤️ A vida de {self.nome} foi completamente restaurada para {self.atributos.hp.total}!")
        print("=" * 40)

    def equipar_arma(self):
        print(f"\n{self.nome} está abrindo a mochila...")
        sleep(1)
        arma_escolhida = self.inventario.escolher_arma()

        if arma_escolhida:
            self.arma = arma_escolhida
            print(f"⚔️ {self.nome} Equipou com sucesso: {arma_escolhida.nome}!")

    def equipar_armadura(self):
        armadura_escolhida = self.inventario.escolher_armadura()

        if armadura_escolhida:
            self.armadura = armadura_escolhida
            print(f"🛡️ {self.nome} equipou {armadura_escolhida.nome}!")

    def usar_pocao_cura(self):
        """Consome uma poção de cura se houver no inventário."""
        # Procuramos se há uma poção de cura no inventário
        pocao = next((item for item in self.inventario.itens if item.nome == "poção de cura"), None)

        if pocao:
            cura = 25
            self.atributos.hp.base += cura
            # Garante que não passe do máximo se você tiver um limite definido,
            # ou apenas aumenta os pontos de HP atualizados.
            self.inventario.itens.remove(pocao)
            print(f"🧪 {self.nome} bebeu uma poção de cura e recupero {cura} de HP")
        else:
            print("❌ Você não tem Poções de Cura na mochila!")

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
            print(f"⚔️ Arma equipada: {self.arma.nome} (Dano: {self.arma.dano})")
        else:
            print(f"⚔️ Arma equipada: Punhos (Dano: 1)")

        if self.armadura:
            print(f"🛡️ Armadura equipada: {self.armadura.nome} (Defesa: {self.armadura.defesa_fisica}/{self.armadura.defesa_magica})")
        else:
            print("🛡️ Armadura equipada: Nenhuma (Roupas comuns)")
        print("=" * 20)