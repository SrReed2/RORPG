from entities.items.weapon import weapon
from entities.player import Player  # o el import que ya tengas para Player

jugador = Player()
espada = weapon("sword", 10)

espada.equip(jugador)
print(jugador.attack) 