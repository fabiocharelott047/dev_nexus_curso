import time
import random

#mudar a vida dos personagens com objetivo de ter mais rodadas

print()
print("|======================|")
print("|---------NEXUS--------|")
print("|======================|\n")
time.sleep(1)
nickname =  input("Digite seu nickname: ")

print("\nSeja bem vindo,",nickname)
print("Este jogo é um combate em turnos, boa sorte!\n")
#colocar mais texto
time.sleep(2)

print("Escolha seu personagem:")

print("1 - Kael")
print("2 - Lyra")
print("3 - ECHO-7")

opcao = int(input("Escolha: "))

if opcao == 1:
    print("Você escolheu Kael")
    hp = 200
    dmg = 25

if opcao == 2:
    print("Você escolheu Lyra")
    hp = 170
    dmg = 25

if opcao == 3:
    print("Você escolheu ECHO-7")
    hp = 220
    dmg = random.randint(10,35)

print("\nSeu HP é:",hp)
print("Seu dano base é:",dmg)
print("\nUm inimigo apareceu!")

inimigo_hp = random.randint(75, 250)
inimigo_dano = random.randint(10, 30)

if opcao == 1:
    while hp > 0 and inimigo_hp > 0:
        sobrecarga_omega = dmg
        facas_multiplas = dmg + 10

        print("vida inimigo:",inimigo_hp)

        print("\n1 - Sobrecarga Ômega")
        print("2 - Facas Múltiplas")

        acao = int(input("\nEscolha um ataque: "))
        print()
        if acao == 1:

            inimigo_hp = max(0, inimigo_hp - dmg)
            hp = max(0, hp - inimigo_dano)

            print("Você atacou!",)
            print("Sua vida:",hp)
            print("\nHP do inimigo:", inimigo_hp)
if opcao == 2:
    while hp > 0 and inimigo_hp > 0:
        
        eco_neural = dmg
        ruido_quantico = dmg + 10


        print("vida inimigo:",inimigo_hp)

        print("\n1 - Eco Neural")
        print("2 - Ruído Quântico")

        acao = int(input("Escolha seu ataque: "))
        print()
        if acao == 1:

            inimigo_hp = max(0, inimigo_hp - eco_neural)
            hp = max(0, hp - inimigo_dano)

            print("Você atacou!", eco_neural)
            print("Sua vida:",hp)
            print("\nVida do inimigo:", inimigo_hp)
        
        else: acao = 2

        inimigo_hp = max(0, inimigo_hp - ruido_quantico)
        hp = max(0, hp - inimigo_dano)

        print("Você atacou!", ruido_quantico)
        print("Sua vida:", hp)
        print("\nVida do inimigo:", inimigo_hp)

if opcao == 3:
    while hp > 0 and inimigo_hp > 0:
        
        shotgun_estrondosa = dmg
        quebra_de_protocolo = dmg + 10

        print("\n1 - Shotgun Estrondosa")
        print("2 - Quebra de Protocolo")

        acao = int(input("Escolha: "))
        print()
        if acao == 1:

            inimigo_hp = max(0, inimigo_hp - shotgun_estrondosa)
            hp = max(0, hp - inimigo_dano)
            
            print("Você atacou!", shotgun_estrondosa)
            print("Sua vida:",hp)
            print("\nHP do inimigo:", inimigo_hp)
        else: acao = 2

        inimigo_hp = max(0, inimigo_hp - quebra_de_protocolo)
        hp = max(0, hp - inimigo_dano)

        print("Você atacou!", quebra_de_protocolo)
        print("Sua vida:", hp)
        print("\nVida do inimigo:", inimigo_hp)

#congratulations
if hp <= 0:
    print("Você morreu, sua vida chegou a zero.")
else:
    print("PARABÉS, A VITÓRIA É SUA.")
