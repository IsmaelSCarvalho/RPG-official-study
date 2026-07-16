import random
from time import sleep

from sistemas.fluxo_combate import FluxoCombate
from sistemas.loja import Loja

from personagens.inimigos.goblin import Goblin
from personagens.inimigos.esqueleto import Esqueleto
from personagens.inimigos.dragao import Dragao

class Exploracao:
    @staticmethod
    def gerar_monstros_por_nivel(heroi):
        """Retorna uma instância de monstro real adequada para o nível do herói."""
        # Geramos uma letra aleatória para o identificador (Ex: Goblin B)
        identificador_aleatorio = random.choice(["A", "B", "C", "D"])

        # 1. Tabela de Encontros Dinâmica baseada no nível do Herói
        if heroi.nivel <= 3:
            # Nível inicial: Apenas Goblins
            monstro_escolhido = Goblin(identificador=identificador_aleatorio)

        elif heroi.nivel <= 6:
            # Nível intermediário: Mistura Goblins e Esqueletos
            monstro_escolhido = random.choice([
                Goblin(identificador=identificador_aleatorio),
                Esqueleto(identificador=identificador_aleatorio),
            ])
        else:
            # Nível alto: Entram os Dragões na tabela de encontros!
            monstro_escolhido = random.choice([
                Esqueleto(identificador=identificador_aleatorio),
                Dragao(identificador=identificador_aleatorio),
            ])

        # Ouro dinâmico deixado pelo monstro (proporcional à sua força/experiência)
        # Como o seu inimigo já traz exp_recompensa da classe dele, usamos esse valor!
        monstro_escolhido.ouro_recompensa = int(monstro_escolhido.exp_recompensa * 1.5)

        # Correção interna: garantimos que o seu sistema de combate leia a XP oficial dele
        monstro_escolhido.exp_recompensa = monstro_escolhido.exp_recompensa

        return monstro_escolhido

    @staticmethod
    def explorar_passo(heroi):
        """Simula um passo de exploração na jornada, ativando tabelas dinâmicas."""
        print(f"\n🚶 {heroi.nome} avança com cautela pela região...")
        sleep(1.2)

        chance = random.randint(1, 100)
        if chance <= 50:
            # 50% de chance de acionar a tabela de monstros reais!
            monstro = Exploracao.gerar_monstros_por_nivel(heroi)
            print(f"\n⚠️ EMBOSCADA! Um {monstro.nome} surge bloqueando seu caminho!")
            sleep(1)
            FluxoCombate.iniciar_arena(heroi, monstro)

        elif chance <= 75:
            # 25% de chance de achar a loja do reino
            print("\n🏪 Um mercador viajante monta sua tenda na beira da estrada...")
            input("Pressione ENTER para olhar as mercadorias...")
            Loja.entrar(heroi)

        else:
            # 25% de chance de viagem tranquila
            print("\n🌲 O caminho segue em silêncio. Nada além do som das folhas ao vento.")
            input("\nPressione ENTER para continuar...")
    @staticmethod
    def _evento_aleatorio_beneficio(heroi):
        """Gera um evento aleatório positivo para ajudar o jogador."""
        eventos = [
            ("baú", "Você tropeçou em um velho baú de madeira escondido sob as raízes de uma árvore!"),
            ("fonte", "Você encontrou uma fonte de águas cristalinas com propriedades curativas."),
            ("santuário", "Você encontrou o santuário de uma divindade antiga. Ao rezar, sente seu corpo revigorado!")
        ]

        tipo, descricao = random.choice(eventos)
        print(f"\n✨ EVENTO {descricao}")
        sleep(1.2)

        if tipo == "baú":
            ouro_achado = random.randint(15, 35)
            heroi.ouro += ouro_achado
            print(f"Você encontrou {ouro_achado} moedas de ouro dentro do baú")
        elif tipo == "fonte":
            cura = 20
            heroi.atributos.hp.base += cura
            print(f"🧪 A água refrescante curou {cura} de HP do seu personagem!")
        elif tipo == "santuário":
            xp_ganho = 25
            # Tratamento caso o seu herói ganhe XP
            if hasattr(heroi, "ganhar_xp"):
                heroi.ganhar_xp(xp_ganho)
            else:
                print(f"✨ Você sente uma paz interior profunda! (Bônus de {xp_ganho} de XP)")

        input("\nPressione ENTER para continuar a jornada...")
