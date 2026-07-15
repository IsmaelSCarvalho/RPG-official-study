from personagens.mago import Mago
from personagens.personagem import Personagem
from personagens.atributosficha import AtributosFicha
from sistemas.fluxo_combate import FluxoCombate
from sistemas.loja import Loja

print("🎮 TESTE DE COMPOSIÇÃO DE ITENS REAIS 🎮\n")

# 1. Instanciamos o Merlin (ele começa zerado de itens e ouro)
heroi = Mago("Merlin")

# 2. Criamos o Goblin com ouro suficiente para as compras
atributos_goblin = AtributosFicha(forca=4, defesa=10, hp_max=20, sabedoria=1, velocidade=2)
monstro = Personagem("Goblin Tesoureiro", "Goblin", atributos_goblin)
monstro.ouro_recompensa = 100  # Ouro farto!
monstro.xp_recompensa = 120

# 3. Luta para conseguir os recursos
FluxoCombate.iniciar_arena(heroi, monstro)

# 4. Entramos na loja para gastar nosso ouro suado em itens REAIS!
Loja.entrar(heroi)

# 5. Merlin decide abrir a mochila e equipar o que comprou!
# (Aqui vai rodar o seu método interativo de escolher e equipar)
heroi.equipar_arma()
heroi.equipar_armadura()

# 6. Exibimos a ficha final atualizada
heroi.mostrar()