
import time
import random

#mudar a vida dos personagens com objetivo de ter mais rodadas
#colocar quanto de vida o inimigo tirou "o imimigo causou x vida"
#

print()
print("|======================|")
print("|---------NEXUS--------|")
print("|======================|\n")
time.sleep(1)
nickname =  input("Digite seu nickname: ")

print("\nSeja bem vindo,",nickname)
print("Este jogo é um combate em turnos, boa sorte!\n")
#colocar mais texto
time.sleep(3)

while True:
   
    print("\nEscolha seu personagem:")
    print("1 - Kael")
    print("2 - Lyra")
    print("3 - ECHO-7")
    
    opcao = int(input("Escolha: "))
    if opcao == 1:
        print("Você escolheu Kael")
        hp = random.randint (200, 300)
        dmg = random.randint (25, 50)
        time.sleep(1)
        break
    elif opcao == 2:
        print("Você escolheu Lyra")
        hp = random.randint (200, 300)
        dmg = random.randint (30, 50)
        time.sleep(1)
        break
    elif opcao == 3:
        print("Você escolheu ECHO-7")
        hp = random.randint (220, 350)
        dmg = random.randint(27,70)
        time.sleep(1)
        break
    elif opcao != (1, 2, 3):
        print("Só existe 3 opções por aqui\n")
        

print("\nSeu HP é:",hp)
print("Seu dano base é:",dmg)
time.sleep(2)
print("\nUm inimigo apareceu!")

inimigo_hp = random.randint(75, 250)
inimigo_dano = random.randint(10, 30)

num_turno = 1

if opcao == 1:
    while hp > 0 and inimigo_hp > 0:
        time.sleep(2)

        print(f"\n|=== TURNO {num_turno} ===|\n")
        
        sobrecarga_omega = dmg
        facas_multiplas = dmg + random.randint (20,45)

        print("vida inimigo:",inimigo_hp)
        print("Dano do inimigo", inimigo_dano)
        
        time.sleep(1)

        print("\n1 - Sobrecarga Ômega (normal)")
        print("2 - Facas Múltiplas (combo)")
        print("3 - Veneno (dura por 3 turnos)")
        
        acao = int(input("\nEscolha um ataque: "))
        print()

        if acao == 1:

            inimigo_hp = max(0, inimigo_hp - sobrecarga_omega)
            hp = max(0, hp - inimigo_dano)

            print("Você atacou!",)
            print("Sua vida:",hp)
            time.sleep(2)
            print("\nHP do inimigo:", inimigo_hp)
        
        elif acao == 2:

            inimigo_hp = max(0, inimigo_hp - facas_multiplas)
            hp = max(0, hp - inimigo_dano)

            print("Você atacou multiplas facas!")
            print(f"...hit {dmg/random.choice([2,5,6])} dmg")
            time.sleep(1)
            print(f"...hit {dmg/random.choice([2,5,6])} dmg")
            time.sleep(1)
            print(f"...hit {dmg/random.choice([2,5,6])} dmg")
            time.sleep(1)
            print(f"...hit {dmg/random.choice([2,4,6])} dmg")
            time.sleep(1)
            #definir as variaveis antes da escrita para mostrar o dano total
            print("dano total foi",)

            print("Sua vida:", hp)
            time.sleep(2)
            print("\nVida do inimigo:", inimigo_hp)

        num_turno += 1

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
    print("\nVocê morreu, sua vida chegou a zero.")
else:
    print("\n|=============================|")
    print("|- PARABÉNS, A VITÓRIA É SUA -|")
    print("|=============================|")
    print("Status|HP:",hp)
    print("|Dano:",dmg) 