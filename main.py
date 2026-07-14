from personagens.mago import Mago
from personagens.personagem import Personagem
from personagens.atributosficha import AtributosFicha
from sistemas.fluxo_combate import FluxoCombate

print("🎮 INICIANDO O RPG COMPLETO 🎮\n")

# 1. Instanciamos o Merlin (ele começa no nível 1)
heroi = Mago("Merlin")

# 2. Criamos um Goblin de teste
atributos_goblin = AtributosFicha(forca=4, defesa=11, hp_max=15, sabedoria=1, velocidade=1)
monstro = Personagem("Goblin Saqueador", "Goblin", atributos_goblin)

# Definimos que esse goblin dá muita XP para garantir o Level Up!
monstro.ouro_recompensa = 50
monstro.xp_recompensa = 120  # Merlin precisa de 100 XP para o Nível 2

# 3. Entramos na arena!
FluxoCombate.iniciar_arena(heroi, monstro)