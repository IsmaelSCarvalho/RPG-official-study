from time import sleep
class Inventario:
    def __init__(self):
        # O inventário guarda a sua própria lista de itens
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)
        print(f"{item.nome} adicionado")

    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
            print(f"{item.nome} removido")
        else:
            print("Item não encontrado.")

    def listar_itens(self):
        print("\n=======  IVENTARIO  =======")
        if len(self.itens) ==0:
            print("O iventário está vazio")
            return

        for indice, item in enumerate(self.itens, start=1):
            print(f"[{indice}] {item.nome} {item.peso}kg")

    def listar_itens_detalhado(self):
        print("\n=======  MEU INVENTARIO  =======")
        if len(self.itens) == 0:
            print("O inventário está vazio.")
            return

        for indice, item in enumerate(self.itens, start=1):
            print(f"Item da mochila número [{indice}]")

            item.mostrar()
            print()

    def escolher_arma(self):
        from itens.arma import Arma
        armas_disponiveis = [item for item in self.itens if isinstance(item, Arma)]

        if not armas_disponiveis:
            print("Você não tem nenhuma arma disponível para equipar!")
            return None

        print("\n=======  SELECIONE UMA ARMA  =======")
        for indice, arma in enumerate(armas_disponiveis, start=1):
            print(f"Opção:[{indice}] {arma.nome}")

        while True:
            try:
                escolha = int(input("\nDigite o número da arma que deseja equipar (ou 0 para voltar): "))
                if escolha == 0:
                    return None

                if 1 <= escolha <= len(armas_disponiveis):
                    arma_escolhida = armas_disponiveis[escolha-1]

                    print(f"\n--- Status: {arma_escolhida.nome} ---")
                    arma_escolhida.mostrar()
                    while True:
                        decisao = input(f"\nDeseja equipar {arma_escolhida.nome}? [S/N]: ").strip().upper()[0]
                        if decisao and decisao[0] == 'S':
                            return arma_escolhida
                        if decisao and decisao[0] == 'N':
                            print("\nVoltando ao menu de seleção...")
                            sleep(0.5)
                            break
                        else:
                            print("Opção inválida! Digite S para sim e N para não. ")
                else:
                    print("Número inválido! Escolha uma das opções da tela.")
            except ValueError:
                print("Por favor, digite um número válido!")

    def escolher_armadura(self):
        from itens.armadura import Armadura
        armaduras_disponiveis = [item for item in self.itens if isinstance(item, Armadura)]

        if not armaduras_disponiveis:
            print("Você não tem armadura para equipar!")
            return None
        print("\n=======  SELECIONE UMA ARMADURA  =======")
        for indice, armadura in enumerate(armaduras_disponiveis, start=1):
            print(f"Opção:[{indice}] {armadura.nome}")
            sleep(1)


        while True:
            try:
                escolha = int(input("\nDigite o número da arma que deseja equipar (ou 0 para voltar): "))
                sleep(0.5)

                if escolha == 0:
                    return None

                if 1 <= escolha <= len(armaduras_disponiveis):
                    armaduras_escolhida = armaduras_disponiveis[escolha-1]
                    print(f"\n--- Status {armaduras_escolhida.nome} ---")
                    armaduras_escolhida.mostrar()

                    while True:
                        decisao = input(f"\nDeseja equipa {armaduras_escolhida.nome}? [S/N]: ").strip().upper()[0]
                        if decisao and decisao[0] == "S":
                            return armaduras_escolhida
                        elif decisao and decisao[0] == "N":
                            print("\nVoltando ao menu de seleção...")
                            sleep(0.5)
                            break
                        else:
                            print("Opção inválida! Digite S para Sim ou N para Não.")
                else:
                    print("Número inválido! Escolha uma das opções da tela.")

            except ValueError:
                print("Por favor, digite um número válido!")