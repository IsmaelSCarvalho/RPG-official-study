from personagens.mago import Mago
from personagens.personagem import Personagem
from personagens.arqueiro import Arqueiro
from personagens.personagem import Personagem
from personagens.atributosficha import AtributosFicha
from sistemas.fluxo_combate import FluxoCombate

print("🎮 INICIANDO O RPG COMPLETO 🎮\n")

# 1. Instanciamos os lutadores com a sua estrutura oficial
heroi = Arqueiro("Legolas")

# Damos mais HP ao Goblin para aguentar o combate por turnos
atributos_goblin = AtributosFicha(forca=4, defesa=11, hp_max=45, sabedoria=1, velocidade=1)
monstro = Personagem("Goblin Saqueador", "Goblin", atributos_goblin)

# Executa o loop da arena até alguém vencer!
FluxoCombate.iniciar_arena(heroi, monstro)