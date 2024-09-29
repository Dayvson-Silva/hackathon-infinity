def iniciar_game():
    import random

    print("No ano 2000, com a virada do século, dois reinos gladiaram. o Reino do Sol, foi dominado pelo Reino das Sombras. Criaturas moradoras das regiões subcrustais organizaram investidas contra as obras da humanidade com objetivo de obter o poder do Planeta Terra. \n   O senhor da escuridão, junto com o seu exército de criaturas das sombras (DOFUS) querem promover o caos social, ecológico e em meio às guerras e à poluição,criar condições sub humanas de vida, dominando a Terra por completo com o objetivo de eliminar toda  a humanidade. \n   Os guardiões do planeta: humanos, mago e o elfo,têm o importante papel de reunirforças e voltar a conduzirem o destino de toda uma nação. Conhecer as artimanhas do mal e tornar-se cada vez mais forte é o único objetivo para combatê-los. Lado a lado os guardiões do Reino do Sol, representantes da justiça divina, tem como objetivo principal impedir o completo domínio do Reino das Sombras e garantir um planeta em condições mínimas para a sobrevivência dos humanos ainda existentes.")

    classes = int(input(f"Você tem 3 classes para escolher, estão entre eles o \n1 - Humano \n2 - Mago \n3 - Elfo \nEscolha qual classe você deseja ser: "))
    # attributes = []

    def rolar_d20():
        return random.randint(1, 20)
    
    def human(classe, tools):
        attribute = {
            "Classe": classe,
            "Armamento(s)": tools,
            "Vida": 200
        }
        return attribute

    def atacar_inimigo():
        enemy_life = 400
        ataque = rolar_d20() * 3
        dano_causado = enemy_life - ataque
        return print(f"A vida do inimigo é {enemy_life}, o dano causado foi {ataque}, a vida do inimigo é {dano_causado}")

    def atacar_heroi():
        hero_life = 200
        ataque = rolar_d20() * 2
        dano_causado = hero_life - ataque
        return print(f"A vida do herói é {hero_life}, o dano causado foi {ataque}, a vida do herói é {dano_causado}")

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
                    atacar_inimigo()
                    atacar_heroi()
                    
                case 2:
                    print("\nVocê escolheu usar uma espada com escudo de madeira \nAqui está os seus atributos iniciais \n1 - Força: 4 \nAgilidade: 3 \nDefesa: 5")
                    print(human("Humano", "Espada média + Escudo de madeira"))
            
                case 3:
                    print("\nVocê escolheu usar espadas duplas \nAqui está os seus atributos iniciais \n1 - Força: 3 \nAgilidade: 4 \nDefesa: 3")
                    print(human("Humano", "Espadas duplas"))
                    
                    
        # Mago (magia, agilidade, defesa)
        case 2:
            print("\nVocê escolheu ser um mago")
            
            # Equipamentos
            tools = int(input(f"Você vai escolher o(s) equipamento(s) do seu mago agora, estão entre eles o \n1 - Cajado do vazio \n2 - Varinha solar \n3 - Bola da repetição \nA escolha dos seus equipamentos vai afetar nos atributos do seu personagem no final: "))
            
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
            

        # Elfo (força, agilidade, magia)
        case 3:
            print("\nVocê escolheu ser um elfo")
            
            # Equipamentos
            tools = int(input(f"Você vai escolher o(s) equipamento(s) do seu elfo agora, estão entre eles o \n1 - Arco \n2 - X-besta \n3 - Dardos com cravos \nA escolha dos seus equipamentos vai afetar nos atributos do seu personagem no final: "))
            
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