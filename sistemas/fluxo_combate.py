from time import sleep
from sistemas.combate import Combate

class FluxoCombate(Combate):

    @staticmethod
    def iniciar_arena(heroi, monstro):
        print("\n" + "⚔️ " * 20)
        print(f"        ENTRANDO NA ARENA: {heroi.nome} VS {monstro.nome}")
        print("⚔️ " * 20)

        rodada = 1

        # LOOP PRINCIPAL DA ARENA
        while heroi.atributos.hp.total > 0 and monstro.atributos.hp.total > 0:
            print(f"\n⏱️ --- RODADA {rodada} ---")
            print(f"{heroi.nome}: {heroi.atributos.hp.total} ❤️HP| {monstro.nome}: {monstro.atributos.hp.total} ❤️HP.")
            sleep(0.5)

            # ==========================================
            # 🟢 TURNO DO JOGADOR (MENU INTERATIVO)
            # ==========================================
            print(f"\nÉ a sua vez, {heroi.nome}")

            turno_ativo = True
            while turno_ativo:
                print("[1] ⚔️ Atacar")
                # Se o personagem tiver mana, mostramos a opção de magia dinamicamente!
                if hasattr(heroi, "mana"):
                    print(f"[2] 🔮 Lançar Magia (Mana: {heroi.mana.total})")
                elif hasattr(heroi, "furia"):
                    print(f"[2] 😡 Ativar a Furia (Furia: {heroi.furia.total})")
                elif hasattr(heroi, "visao"):
                    print(f"[2] 🏹 Flexcha de longo alcance (Visão: {heroi.visao.total})")
                print("[3] 🎒 Olhar Ficha/Mochila")
                print("[4] 🏃 Fugir")

                escolha = input("O que você deseja fazer? ->")

                if escolha == "1":
                    resultado_heroi = Combate.atacar(heroi, monstro)
                    resultado_heroi.mostrar()
                    turno_ativo = False
                elif escolha == "2" and (hasattr(heroi, "mana") or hasattr(heroi,"furia") or hasattr(heroi, "visao")):
                    if hasattr(heroi, "mana"):
                        # Tenta lançar a magia
                        dano_causado = heroi.lancar_seta_de_gelo(monstro)

                        # Se o dano for maior que zero, significa que ele tinha mana e a magia foi executada!
                        if dano_causado > 0:
                            turno_ativo = False

                    elif hasattr(heroi, "furia"):
                        # Tenta lançar a magia
                        dano_causado = heroi.modo_furia(monstro)

                        # Se o dano for maior que zero, significa que ele tinha mana e a magia foi executada!
                        if dano_causado > 0:
                            turno_ativo = False

                    elif hasattr(heroi, "visao"):
                        dano_causado = heroi.flechas_de_longo_alcance(monstro)

                        if dano_causado > 0:
                            turno_ativo = False

                    else:
                        # Se retornou 0 (sem mana), não gasta o turno, permitindo ele escolher outra coisa
                        input("\nPressione ENTER para voltar e escolher outra ação...")
                        print("-" * 40)
                    sleep(1)

                elif escolha == "3":
                    heroi.mostrar()
                    input("\nPressione ENTER para voltar ao menu de combate...")
                    print("-" * 40)

                elif escolha == "4":
                    print(f"\n🏃 {heroi.nome} dá meia volta e tenta escapar correndo desesperadamente!")
                    print("💨 Você conseguiu fugir do combate com segurança!")
                    return  # Sai completamente da função e encerra a arena
                else:
                    print("⚠️ Opção inválida! Escolha um número do menu.")

            if monstro.atributos.hp.total <= 0:
                print(f"🏆 {heroi.nome} VENCEU A BATALHA!")
                print("\n🎒 O monstro deixou algo para trás...")
                # Você pode instanciar um item e mandar o herói coletar:
                # heroi.inventario.adicionar_item(item_do_monstro)

                # Entrega a recompensa
                ouro = getattr(monstro, "ouro_recompensa", 10) # Padrão 10 se não tiver
                xp = getattr(monstro, "xp_recompensa", 10)
                heroi.ganhar_recompensa(ouro,xp)
                break
            sleep(1.5)

            # ==========================================
            # 🔴 TURNO DO MONSTRO
            # ==========================================
            print(f"\n🔴 Turno do {monstro.nome}: ")
            sleep(1)

            resultado_monstro = Combate.atacar(monstro, heroi)
            resultado_monstro.mostrar()

            if heroi.atributos.hp.total <= 0:
                print(f"💀 GAME OVER... {heroi.nome} foi derrotado por {monstro.nome}.")
                break

            rodada += 1
            print("-" * 40)
            sleep(1)

    print("\n🏁 O combate na arena foi encerrado!")
