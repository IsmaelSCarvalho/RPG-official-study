from time import sleep

# Importações dos seus sistemas
from personagens.mago import Mago
from sistemas.exploracao import Exploracao
from sistemas.missoes import guilda_global
from sistemas.interface_visual import GerenciadorVisual  # ⬅️ IMPORTANTE!


def menu_principal():
    print("🎮 " * 15)
    print("      BEM-VINDO AO RPG DE EXPLORAÇÃO E MISSÕES      ")
    print("🎮 " * 15)

    nome_jogador = input("\nDigite o nome do seu Herói: ").strip()
    if not nome_jogador:
        nome_jogador = "Aventureiro"

    heroi = Mago(nome_jogador)
    heroi.ouro = 50

    if not hasattr(heroi.inventario, "itens"):
        heroi.inventario.itens = []

    # 🐉 🔥 TESTE DA CENA DO DRAGÃO LOGO NA ENTRADA! 🔥 🐉
    print("\n⚡ [TESTE DE CENA VISUAL] Carregando encontro épico...")
    GerenciadorVisual.exibir_cena(
        "dragao",
        f"Cuidado, {heroi.nome}! As nuvens do Pico do Dragão se abrem e um fogo devastador ilumina os céus!"
    )
    input("\nPressione ENTER para fechar a imagem e entrar na Cidade Central...")

    # LOOP NORMAL DA CIDADE CENTRAL
    rodando = True
    while rodando:
        xp_atual = getattr(heroi, "experiencia", getattr(heroi, "xp", 0))
        total_itens = len(heroi.inventario.itens)

        print("\n" + "🏰 " * 15)
        print(f"       CIDADE CENTRAL | {heroi.nome.upper()} [Nível {heroi.nivel}] | XP[{xp_atual}]")
        print("🏰 " * 15)
        print(f"🪙 Ouro: {heroi.ouro} PO | 🎒 Itens na Mochila: [{total_itens}]")
        print("-" * 40)
        print("[ 1 ] 🗺️  Viajar / Explorar Regiões")
        print("[ 2 ] 🧓 Falar com o Mestre das Missões (NPC)")
        print("[ 3 ] 🎒 Ver Ficha / Inventário Detalhado")
        print("[ 4 ] 🚪 Sair do Jogo")

        escolha = input("\nPara onde deseja ir na cidade? -> ").strip()

        if escolha == "1":
            regiao_alvo = Exploracao.escolher_destino()
            if regiao_alvo:
                Exploracao.viajar_para_regiao(heroi, regiao_alvo)
        elif escolha == "2":
            guilda_global.interagir_npc(heroi)
        elif escolha == "3":
            heroi.mostrar()
            input("\nPressione ENTER para voltar...")
        elif escolha == "4":
            print("\n👋 Até a próxima jornada!")
            rodando = False


if __name__ == "__main__":
    menu_principal()