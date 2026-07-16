from personagens.mago import Mago
from sistemas.exploracao import Exploracao


def menu_principal():
    print("🎮 BEM-VINDO AO RPG DE EXPLORAÇÃO E COMBATE 🎮")
    nome_jogador = input("Digite o nome do seu Herói: ")

    # Iniciamos o herói (no caso, um Mago)
    heroi = Mago(nome_jogador)
    heroi.ouro = 20  # Começa com um dinheirinho de bolso

    rodando = True
    while rodando:
        print("\n" + "=" * 40)
        print(
            f" 🧙‍♂️ {heroi.nome.upper()} | Nível: {heroi.nivel} | HP: {heroi.atributos.hp.base} | Ouro: {heroi.ouro} PO")
        print("=" * 40)
        print("[ 1 ] 🚶 Continuar Viagem (Explorar)")
        print("[ 2 ] 🎒 Ver Inventário / Ficha do Herói")
        print("[ 3 ] 🚪 Sair do Jogo")

        escolha = input("\nO que deseja fazer? -> ")

        if escolha == "1":
            # Dá um passo na jornada, ativando os eventos aleatórios
            Exploracao.explorar_passo(heroi)

        elif escolha == "2":
            # Mostra a ficha completa do personagem
            print("\n--- FICHA DO HERÓI ---")
            heroi.mostrar()

            # Se você tiver métodos de equipar no inventário, pode chamá-los aqui
            if hasattr(heroi, "equipar_arma") and len(heroi.inventario.itens) > 0:
                opcao = input("\nDeseja equipar alguma arma ou armadura? (s/n) -> ").lower()
                if opcao == "s":
                    heroi.equipar_arma()
                    heroi.equipar_armadura()
            input("\nPressione ENTER para voltar ao menu principal...")

        elif escolha == "3":
            print("\n💾 Salvando progresso na memória... Obrigado por jogar!")
            rodando = False
        else:
            print("⚠️ Opção inválida!")


if __name__ == "__main__":
    menu_principal()