import time
import random

print()
print("|======================|")
print("|---------NEXUS--------|")
print("|======================|\n")

nickname = input("Digite seu nickname: ")

print(f"\nSeja bem vindo, {nickname}")
print("Este jogo é um combate em turnos, boa sorte!\n")
time.sleep(2)

# ESCOLHA DE PERSONAGEM
while True:

    print("\nEscolha seu personagem:")
    print("1 - Kael")
    print("2 - Lyra")
    print("3 - ECHO-7")

    try:
        opcao = int(input("Escolha: "))
    except ValueError:
        print("Digite apenas números.")
        continue

    if opcao == 1:
        personagem = "Kael"
        hp = random.randint(200, 300)
        dmg = random.randint(25, 50)
        break

    elif opcao == 2:
        personagem = "Lyra"
        hp = random.randint(200, 300)
        dmg = random.randint(30, 50)
        break

    elif opcao == 3:
        personagem = "ECHO-7"
        hp = random.randint(220, 350)
        dmg = random.randint(27, 70)
        break

    else:
        print("Só existem 3 opções.\n")

print(f"\nVocê escolheu {personagem}")

print("\nSeu HP é:", hp)
print("Seu dano base é:", dmg)

time.sleep(2)

print("\n|--------------------------|")
print("|-- Um inimigo apareceu! --|")
print("|--------------------------|")

# STATUS INIMIGO
inimigo_hp = random.randint(120, 300)
inimigo_dano = random.randint(10, 30)

num_turno = 1

# EFEITOS CONTÍNUOS
veneno_turnos = 0
veneno_dano = 20

espiral_turnos = 0
espiral_dano = 20

marca_turnos = 0
marca_dano = 25

# LOOP PRINCIPAL
while hp > 0 and inimigo_hp > 0:

    print(f"\n|=== TURNO {num_turno} ===|\n")

    # EFEITOS POR TURNO

    if veneno_turnos > 0:
        inimigo_hp = max(0, inimigo_hp - veneno_dano)
        veneno_turnos -= 1

        print(f"Veneno causou {veneno_dano} dano!")
        print(f"Turnos restantes: {veneno_turnos}\n")

    if espiral_turnos > 0:
        inimigo_hp = max(0, inimigo_hp - espiral_dano)
        espiral_turnos -= 1

        print(f"Espiral Fantasma causou {espiral_dano} dano!")
        print(f"Turnos restantes: {espiral_turnos}\n")

    if marca_turnos > 0:
        inimigo_hp = max(0, inimigo_hp - marca_dano)
        marca_turnos -= 1

        print(f" Marca da Execução causou {marca_dano} dano!")
        print(f"Turnos restantes: {marca_turnos}\n")

    print("HP do inimigo:", inimigo_hp)
    print("Dano do inimigo:", inimigo_dano)
    time.sleep(1)

    # KAEL
    if opcao == 1:

        print("\n1 - Sobrecarga Ômega")
        print("2 - Facas Múltiplas")
        print("3 - Veneno")

        try:
            acao = int(input("\nEscolha um ataque: "))
        except ValueError:
            print("Digite apenas números.")
            continue

        if acao == 1:
            dano = dmg

            inimigo_hp = max(0, inimigo_hp - dano)
            hp = max(0, hp - inimigo_dano)

            print(f"\n Sobrecarga Ômega causou {dano} dano!")

        elif acao == 2:
            hp = max(0, hp - inimigo_dano)

            dmg_one = random.randint(5, 15)
            dmg_two = random.randint(5, 15)
            dmg_three = random.randint(5, 15)
            dmg_four = random.randint(5, 15)
            dano_total = dmg_one + dmg_two + dmg_three + dmg_four

            inimigo_hp = max(0, inimigo_hp - dano_total)

            print("\n Facas Múltiplas!")
            print(f"...hit {dmg_one}")
            time.sleep(0.5)
            print(f"...hit {dmg_two}")
            time.sleep(0.5)
            print(f"...hit {dmg_three}")
            time.sleep(0.5)
            print(f"...hit {dmg_four}")
            time.sleep(0.5)
            print(f"\nDano total: {dano_total}")

        elif acao == 3:

            veneno_turnos = 3

            hp = max(0, hp - inimigo_dano)

            print("\n O inimigo foi envenenado!")
        else:
            print("Ataque inválido.")
            continue

    # LYRA
    elif opcao == 2:

        print("\n1 - Eco Neural")
        print("2 - Ruído Quântico")
        print("3 - Espiral Fantasma")

        try:
            acao = int(input("\nEscolha um ataque: "))
        except ValueError:
            print("Digite apenas números.")
            continue

        if acao == 1:

            dano = dmg
            inimigo_hp = max(0, inimigo_hp - dano)
            hp = max(0, hp - inimigo_dano)

            print(f"\n Eco Neural causou {dano} dano!")

        elif acao == 2:
            hp = max(0, hp - inimigo_dano)

            dmg_one = random.randint(8, 18)
            dmg_two = random.randint(8, 18)
            dmg_three = random.randint(8, 18)
            dmg_four = random.randint(8, 18)
            dano_total = dmg_one + dmg_two + dmg_three + dmg_four
            
            inimigo_hp = max(0, inimigo_hp - dano_total)

            print("\n Ruído Quântico!")
            print(f"...hit {dmg_one}")
            time.sleep(0.5)
            print(f"...hit {dmg_two}")
            time.sleep(0.5)
            print(f"...hit {dmg_three}")
            time.sleep(0.5)
            print(f"...hit {dmg_four}")
            time.sleep(0.5)
            print(f"\nDano total: {dano_total}")

        elif acao == 3:

            espiral_turnos = 3

            hp = max(0, hp - inimigo_dano)

            print("\n Espiral Fantasma ativada!")

        else:
            print("Ataque inválido.")
            continue

    # ECHO-7
    elif opcao == 3:

        print("\n1 - Shotgun Estrondosa")
        print("2 - Quebra de Protocolo")
        print("3 - Marca da Execução")

        try:
            acao = int(input("\nEscolha um ataque: "))
        except ValueError:
            print("Digite apenas números.")
            continue

        if acao == 1:
            dano = dmg + 10
            inimigo_hp = max(0, inimigo_hp - dano)
            hp = max(0, hp - inimigo_dano)

            print(f"\n Shotgun Estrondosa causou {dano} dano!")

        elif acao == 2:
            hp = max(0, hp - inimigo_dano)

            dmg_one = random.randint(10, 20)
            dmg_two = random.randint(10, 20)
            dmg_three = random.randint(10, 20)
            dmg_four = random.randint(10, 20)
            dano_total = dmg_one + dmg_two + dmg_three + dmg_four
            inimigo_hp = max(0, inimigo_hp - dano_total)

            print("\n Quebra de Protocolo!")
            print(f"...hit {dmg_one}")
            time.sleep(0.5)
            print(f"...hit {dmg_two}")
            time.sleep(0.5)
            print(f"...hit {dmg_three}")
            time.sleep(0.5)
            print(f"...hit {dmg_four}")
            time.sleep(0.5)

            print(f"\nDano total: {dano_total}")

        elif acao == 3:
            marca_turnos = 3
            hp = max(0, hp - inimigo_dano)

            print("\n Marca da Execução ativada!")
        else:
            print("Ataque inválido.")
            continue

    # STATUS
    print("\nSua vida:", hp)
    print("Vida do inimigo:", inimigo_hp)
    num_turno += 1
    time.sleep(2)
    
# FINAL
if hp <= 0:

    print("\nVocê morreu.")
    print("Sua vida chegou a zero.")

else:

    print("\n|=============================|")
    print("|- PARABÉNS, A VITÓRIA É SUA -|")
    print("|=============================|")

    print("\nStatus Final")
    print("HP:", hp)
    print("Dano Base:", dmg)
    