from personagens.arqueiro import Arqueiro
from personagens.guerreiro import Guerreiro
from personagens.mago import Mago

class CadastroPersonagens:

    def __init__(self):
        self.personagem = None

    def cadastro_personagens(self):

        print("=" * 40)
        print("--- Cadastro de personagens ---")
        print("=" * 40)

        nome = input("Nome: ").title().strip()

        print("\nEscolha uma classe")
        print("[1] Guerreiro Maculado")
        print("[2] Mago Clériga das Cinzas")
        print("[3] Danger Pária das Sombras")

        while True:

            escolha = input("\nOpção: ")
            if escolha == "1":
                self.personagem = Guerreiro(nome)
                break
            elif escolha == "2":
                self.personagem = Mago(nome)
                break
            elif escolha == "3":
                self.personagem = Arqueiro(nome)
                break
            else:
                print("Opção INVALIDA")

        print("\n--- Personagem criado com sucesso! ---")
        return self.personagem

