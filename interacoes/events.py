import random

def event_1():
    evento_incial = [
        "Os dofus(Criaturas das sombras) surgiu do solo para te impedir",
        "Os nífes(Criaturas do centro da terra) surgiram do solo para te impedir" 
    ]
    return random.choice(evento_incial)
    
def evento_2():
    evento_secundario = [
        "Os bugs possuidos apareceram, lute com eles",
        "As bestas das profundezas surgiram, tome cuidado"
    ]
    return random.choice(evento_secundario)
    
def mestre():
    chefao = [
        "Você deu de cara com o Lord of shadows, o combate final"
    ]
    return random.choice(chefao)
    