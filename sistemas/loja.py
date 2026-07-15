from time import sleep

from itens.armas import EspadaMadeira, EspadaLonga, Cajado, Adaga, ArcoCurto
from itens.armaduras import ArmaduraCouro, ArmaduraFerro, ArmaduraMithril, ArmaduraDiamante

class Loja:
    @staticmethod
    def entrar(heroi):
        """Menu principal da loja que categoriza as mercadorias de forma dinâmica."""
        # Criamos o estoque instanciando os itens reais
        estoque_armas = [EspadaMadeira(), EspadaLonga(), Cajado(), Adaga(), ArcoCurto()]
        estoque_armaduras = [ArmaduraCouro(), ArmaduraFerro(), ArmaduraMithril(), ArmaduraDiamante()]

        print("\n" + "🏪 " * 15)
        print(f"        BEM-VINDO À LOJA DE ITENS, {heroi.nome.upper()}!")
        print("🏪 " * 15)

        visita_ativa = True
        while visita_ativa:
            print(f"\nSeu Ouro {heroi.ouro} PO")
            print("-" * 40)
            print("[ 1 ] 🧪 Comprar Consumíveis (Mecânica futura de poções)")
            print("[ 2 ] ⚔️ Ver Armas à venda")
            print("[ 3 ] 🛡️ Ver Armaduras à venda")
            print("[ 4 ] 🚪 Sair da Loja")

            escolha = input("\nO que você deseja comprar? -> ")


            if escolha == "1":
                print("\n🧪 O lojista resmunga: 'Ainda estou aguardando a entrega do alquimista...'")
                sleep(1)

            elif escolha == "2":
                Loja._mostrar_categoria(heroi, "ARMAS", estoque_armas)

            elif escolha == "3":
                Loja._mostrar_categoria(heroi, "ARMADURAS", estoque_armaduras)

            elif escolha == "4":
                print("\n👋 O lojista acena: 'Volte sempre, aventureiro!'")
                visita_ativa = False
                sleep(1)
            else:
                print("⚠️ Opção inválida!")

    @staticmethod
    def _mostrar_catagoria(heroi, nome_categoria, itens_estoque):
        """Gerencia de forma 100% dinâmica a exibição, escolha e compra de qualquer item."""
        exibindo = True
        while exibindo:
            print(f"\n🪙 Seu Ouro: {heroi.ouro} PO")
            print(f"--- ESTOQUE DE {nome_categoria} ---")

            for indice, item in enumerate(itens_estoque, start=1):
                detalhe = f"Dano: {item.dano}" if hasattr(item, "dano") else f"Def/Mag: {item.defesa_fisica}/{item.defesa_magica}"
                print(f"[{indice}] {item.nome} ({detalhe}) | Curto: {item.valor} PO")

            print(f"[ {len(itens_estoque) + 1} ] ⬅️ Voltar ao menu Principal")

            try:
                opcao = int(input("\nDigite o número do item que deseja comprar: "))

                if opcao == len(itens_estoque) + 1:
                    exibindo = False

                elif 1 <= opcao <= len(itens_estoque):
                    item_escolhido = itens_estoque[opcao - 1]

                    if heroi.ouro >= item_escolhido.valor:
                        heroi.ouro -= item_escolhido.valor
                        heroi.iventario.adicionar_item(item_escolhido)
                        print(f"\n✅ Compra realizada! {item_escolhido.nome} adicionada à sua mochila!")
                        sleep(1)
                    else:
                        print("\n❌ Ouro insuficiente para este item!")
                        sleep(1)

                else:
                    print("\n⚠️ Opção inválida!")
                    sleep(1)
            except ValueError:
                print("\n⚠️ Por favor, digite um número válido.")
                sleep(1)