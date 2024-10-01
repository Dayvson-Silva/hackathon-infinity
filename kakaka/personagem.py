import random

print(
    "\n\n   \033[1;37;37mNo ano 2000, com a virada do século, dois reinos gladiaram. \033[1;33;33mO Reino do Sol\033[m, \033[1;37;37mfoi dominado pelo \033[1;34;34mReino das Sombras\033[m. \033[1;37;37mCriaturas moradoras das regiões subcrustais organizaram investidas contra as obras da humanidade com objetivo de obter o poder do Planeta Terra. \n   \033[1;34;34mO senhor da escuridão, \033[1;37;37mjunto com o seu exército de criaturas das sombras (DOFUS) querem promover o caos social e ecológico, e em meio às guerras e à poluição,criar condições sub humanas de vida, dominando a Terra por completo com o objetivo de eliminar toda a humanidade. \n   Os guardiões do planeta: humano, mago e o elfo,têm o importante papel de reunir forças e voltar a conduzirem o destino de toda uma nação. Conhecer as artimanhas do mal e tornar-se cada vez mais forte é o único objetivo para combatê-los. Lado a lado os \033[1;33;33mguardiões do Reino do Sol, representantes da justiça divina, \033[1;37;37mtem como objetivo principal impedir o completo domínio do Reino das Sombras e garantir um planeta em condições mínimas para a sobrevivência dos humanos ainda existentes.\033[m"
)

classes = int(
    input(
        f"\n\033[1mVocê tem 3 classes para escolher, estão entre eles o\033[m \n\033[1;33;1m1 - Humano\033[m \n\033[1;36;1m2 - Mago\033[m \n\033[1;32;1m3 - Elfo \033[m\n\033[1mEscolha qual classe você deseja ser: "
    )
)
print()


# Rolar dados
def rolar_d20():
    return random.randint(1, 20)


character_information_list = []


def character_information(c, t):
    information = {"Class": c, "Weapon": t}
    character_information_list.append(information)

    # Armazena a classe e a arma do herói atual
    for character in range(len(character_information_list)):
        character_class = character_information_list[character].get("Class")
        character_weapon = character_information_list[character].get("Weapon")


match classes:
    # Humano (força, agilidade, defesa)
    case 1:
        print("\nVocê escolheu ser um humano")

        # Equipamentos
        tool = int(
            input(
                f"Você vai escolher o(s) equipamento(s) do seu humano agora, estão entre eles a \n1 - Adaga \n2 - Espada média + Escudo de madeira \n3 - Espadas duplas \nA escolha dos seus equipamentos vai afetar nos atributos do seu personagem no final: "
            )
        )

        match tool:
            case 1:
                print(
                    "\nVocê escolheu usar uma \033[1;33;35adaga\033[m \nAqui está os seus atributos iniciais \nForça: 2 \nAgilidade: 5 \nDefesa: 2"
                )
                print(character_information("Humano", "Adaga"))

            case 2:
                print(
                    "\nVocê escolheu usar uma \033[1;33;35mespada média com escudo de madeira\033[m \nAqui está os seus atributos iniciais \n1 - Força: 4 \nAgilidade: 3 \nDefesa: 5"
                )
                print(
                    character_information("Humano", "Espada média + Escudo de madeira")
                )

            case 3:
                print(
                    "\nVocê escolheu usar \033[1;33;35mespadas duplas\033[m \nAqui está os seus atributos iniciais \n1 - Força: 3 \nAgilidade: 4 \nDefesa: 3"
                )
                print(character_information("Humano", "Espadas duplas"))

    # Mago (magia, agilidade, defesa)
    case 2:
        print("\n\033[1;46;46mVocê escolheu ser um mago\033[m")

        # Equipamentos
        tool = int(
            input(
                f"Você vai escolher o(s) equipamento(s) do seu mago agora, estão entre eles o(a) \n1 - Cajado do vazio \n2 - Varinha solar \n3 - Bola da repetição \nA escolha dos seus equipamentos vai afetar nos atributos do seu personagem no final: "
            )
        )

        match tool:
            case 1:
                print(
                    "\nVocê escolheu usar um \033[1;34;33mcajado do vazio\033[m \nAqui está os seus atributos iniciais \nForça: 2 \nAgilidade: 5 \nDefesa: 2"
                )
                print(character_information("Mago", "Cajado do vazio"))

            case 2:
                print(
                    "\nVocê escolheu usar uma \033[1;35;33mvarinha solar\033[m \nAqui está os seus atributos iniciais \nForça: 4 \nAgilidade: 3 \nDefesa: 5"
                )
                print(character_information("Mago", "Varinha solar"))

            case 3:
                print(
                    "\nVocê escolheu usar a \033[1;33;35mbola da repetição\033[m \nAqui está os seus atributos iniciais \nForça: 3 \nAgilidade: 4 \nDefesa: 3"
                )
                print(character_information("Mago", "Bola da repetição"))

    # Elfo (força, agilidade, magia)
    case 3:
        print("\nVocê escolheu ser um elfo")

        # Equipamentos
        tool = int(
            input(
                f"Você vai escolher o(s) equipamento(s) do seu elfo agora, estão entre eles o(a) \n1 - Arco \n2 - X-besta \n3 - Dardos com cravos \nA escolha dos seus equipamentos vai afetar nos atributos do seu personagem no final: "
            )
        )

        match tool:
            case 1:
                print(
                    "\nVocê escolheu usar um \033[1;33;35arco\033[m \nAqui está os seus atributos iniciais \nForça: 2 \nAgilidade: 5 \nDefesa: 2"
                )
                print(character_information("Elfo", "Arco"))

            case 2:
                print(
                    "\nVocê escolheu usar uma \033[1;33;35X-besta\033[m \nAqui está os seus atributos iniciais \nForça: 4 \nAgilidade: 3 \nDefesa: 5"
                )
                print(character_information("Elfo", "X-besta"))

            case 3:
                print(
                    "\nVocê escolheu usar \033[1;33;35dardos com cravos\033[m \nAqui está os seus atributos iniciais \nForça: 3 \nAgilidade: 4 \nDefesa: 3"
                )
                print(character_information("Elfo", "Dardos com cravos"))
