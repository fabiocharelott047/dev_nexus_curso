print()
print("|======================|")
print("|---------NEXUS--------|")
print("|======================|\n")

nickname =  input("Digite seu nickname: ")

print("Seja bem vindo,",nickname)
print("Este jogo é um combate em turnos, boa sorte!\n")

print("Escolha seu personagem:")

print("1 - Kael")
print("2 - Lyra")
print("3 - ECHO-7")

opcao = int(input("Escolha: "))

if opcao == 1:
    print("Você escolheu Kael")
    hp = 150
    dano = 25

if opcao == 2:
    print("Você escolheu Lyra")
    hp = 90
    dano = 40

if opcao == 3:
    print("Você escolheu ECHO-7")
    hp = 170
    dano = 35

print("\nUm inimigo apareceu!")

inimigo_hp = 100
inimigo_dano = 25
if opcao == 1:
    while hp > 0 and inimigo_hp > 0:
        print("vida inimigo:",inimigo_hp)

        print("\n1 - Sobrecarga Ômega")
        print("2 - Facas Múltiplas")

        acao = int(input("Escolha: "))
        print()
        if acao == 1:

            inimigo_hp = inimigo_hp - dano
            hp = hp - inimigo_dano

            print("Sua vida:",hp)
            print("Você atacou!",dano)
            print("HP do inimigo:", inimigo_hp)
if opcao == 2:
    while hp > 0 and inimigo_hp > 0:
        print("vida inimigo:",inimigo_hp)

        print("\n1 - Eco Neural")
        print("2 - Ruído Quântico")

        acao = int(input("Escolha: "))
        print()
        if acao == 1:

            inimigo_hp = inimigo_hp - dano
            hp = hp - inimigo_dano

            print("Sua vida:",hp)
            print("Você atacou!",dano)
            print("HP do inimigo:", inimigo_hp)
if opcao == 3:
    while hp > 0 and inimigo_hp > 0:
        print("vida inimigo:",inimigo_hp)

        print("\n1 - Shotgun Estrondosa")
        print("2 - Quebra de Protolo")

        acao = int(input("Escolha: "))
        print()
        if acao == 1:

            inimigo_hp = inimigo_hp - dano
            hp = hp - inimigo_dano

            print("Sua vida:",hp)
            print("Você atacou!",dano)
            print("HP do inimigo:", inimigo_hp)
#congratulations
if hp <= 0:
    print("Você morreu, sua vida chegou a zero.")
else:
    print("PARABÉS, A VITÓRIA É SUA.")