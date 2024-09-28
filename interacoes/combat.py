import random

def atacar(atacante, defensor):
    dano = max(0, atacante.forca + random.radint(-2, 5) - defensor.destreza)
    defensor.vida -= dano
    return dano

