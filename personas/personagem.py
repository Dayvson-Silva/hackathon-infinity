classes = int(input(f"Você tem 3 classes para escolher, estão entre eles o \n1 - Humano \n2 - Mago \n3 - Elfo \nEscolha qual classe você deseja ser: "))
attributes = []

def human(classe, tools):
    attribute = {
        "Classe": classe,
        "Armamento(s)": tools,
    }
    return attribute

match classes:
    # Humano (força, agilidade, defesa)
    case 1:
        print("\nVocê escolheu ser um humano")
        
        # Equipamentos
        tools = int(input(f"Você vai escolher o(s) equipamento(s) do seu humano agora, estão entre eles o \n1 - Adaga \n2 - Espada média + Escudo de madeira \n3 - Espadas duplas \nA escolha dos seus equipamentos vai afetar nos atributos do seu personagem no final: "))
        
        match tools:
            case 1:
                adaga = print("\nVocê escolheu usar uma adaga \nAqui está os seus atributos iniciais \nForça: 2 \nAgilidade: 5 \nDefesa: 2")
                print(human("Humano", "Adaga"))
                
            case 2:
                print("\nVocê escolheu usar uma espada com escudo de madeira \nAqui está os seus atributos iniciais \n1 - Força: 4 \nAgilidade: 3 \nDefesa: 5")
                print(human("Humano", "Espada média + Escudo de madeira"))
        
            case 3:
                print("\nVocê escolheu usar espadas duplas \nAqui está os seus atributos iniciais \n1 - Força: 3 \nAgilidade: 4 \nDefesa: 3")
                print(human("Humano", "Espadas duplas"))
                
                
                
                
    # Mago (magia, agilidade, defesa)
    case 2:
        print("\nVocê escolheu ser um mago")

    # Elfo (força, agilidade, magia)
    case 3:
        print("\nVocê escolheu ser um elfo")
    