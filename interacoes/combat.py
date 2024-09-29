import random
from kakaka import human

def atacar():
    ataque = human(classe, tools)
    vida = ataque["Vida"]
    dano = vida - 100
    print(dano)

    return ataque, vida, dano

print(atacar())