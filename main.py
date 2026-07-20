from personagens.mago import Mago
from sistemas.exploracao import Exploracao
from sistemas.missoes import guilda_global


def menu_principal():
    print("🎮 BEM-VINDO AO RPG EXPANDIDO 🎮")
    nome_jogador = input("Digite o nome do seu Herói: ")

    heroi = Mago(nome_jogador)
    heroi.ouro = 50
    # Caso seu inventário seja uma classe, garantimos que tenha a lista de itens acessível
    if not hasattr(heroi.inventario, "itens"):
        heroi.inventario.itens = []

    rodando = True
    while rodando:
        # Puxa a experiência atual do herói (ajuste o nome da variável se no seu for .xp ou .exp)
        xp_atual = heroi.experiencia if hasattr(heroi, "experiencia") else getattr(heroi, "xp", 0)

        # Conta quantos itens totais existem dentro da lista da mochila
        total_itens = len(heroi.inventario.itens)

        print("\n" + "🏰 " * 15)
        # 1ª Melhoria: Adicionado o indicador de XP ao lado do nível
        print(f"       CIDADE CENTRAL | {heroi.nome.upper()} [Nível {heroi.nivel}] | XP[{xp_atual}]")
        print("🏰 " * 15)
        # 2ª Melhoria: Agora mostra apenas o total numérico de itens acumulados
        print(f"🪙 Ouro: {heroi.ouro} PO | 🎒 Itens na Mochila: [{total_itens}]")
        print("-" * 40)
        print("[ 1 ] 🗺️  Viajar / Explorar Regiões")
        print("[ 2 ] 🧓 Falar com o Mestre das Missões (NPC)")
        print(
            "[ 3 ] 🎒 Ver Ficha / Inventário Detalhado")  # Boa prática para o jogador ainda ver o NOME dos itens se quiser
        print("[ 4 ] 🚪 Sair do Jogo")

        escolha = input("\nPara onde deseja ir na cidade? -> ")
        # ... resto do seu código de escolhas (1, 2, 3, 4) igual ...

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
            print("\n👋 Até a próxima jornada, herói!")
            rodando = False


if __name__ == "__main__":
    menu_principal()