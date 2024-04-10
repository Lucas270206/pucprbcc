import random

jog1= 0
jog2 = 0
empate = 0
continuar = 0

print("Então você quer jogar um pedra, papel e tesoura.... \n então bora!!!")
modalidade = int(input('Para começar você deve escolher uma modalidade irmão escreva 1 para Humano x Humano; 2 para Humano x Maquina e 3 para Maquina x maquina: '))
while modalidade != 1 and modalidade != 2 and modalidade != 3:
    modalidade = int(input('Não sabe ler escolha uma modalidade VALIDA irmão escreva 1 para Humano x Humano; 2 para Humano x Maquina e 3 para Maquina x maquina: '))
while continuar != 2:
    if modalidade == 1:
        print("----" *25)
        num1 = int(input("player 1 - Escolha: 1 = pedra / 2 = papel / 3 = tesoura "))
        num2 = int(input("player 2 - Escolha: 1 = pedra / 2 = papel / 3 = tesoura "))
        while num1 != 1 and num1 != 2 and num1 != 3 and num2 != 1 and num2 != 2 and num2 != 3:
            num1 = int(input("player 1 - Escolha: 1 = pedra / 2 = papel / 3 = tesoura "))
            num2 = int(input("player 2 - Escolha: 1 = pedra / 2 = papel / 3 = tesoura "))

    elif modalidade == 2:
        print("----" *25)
        num1 = int(input("player 1 - Escolha: 1 = pedra / 2 = papel / 3 = tesoura ")) 
        num2 = random.randint(1,3)
        print("----" *25)
        while num1 != 1 and num1 != 2 and num1 != 3:
            num1 = int(input("player 1 - Escolha: 1 = pedra / 2 = papel / 3 = tesoura "))
    else:
        print("----" *25)
        num1 = random.randint(1,3)
        num2 = random.randint(1,3)
        print("----" *25)


    if num1 == 1 and num2 == 1:
        print('player 1 escolheu pedra \nPlayer 2 escolheu pedra \nDeu empate meu amores =)')
        empate += 1 
    elif num1 == 1  and num2 == 2:
        print('player 1 escolheu pedra \nPlayer 2 escolheu papel \nPlayer 2 ganhou =)')
        jog2 += 1
    elif num1 == 1  and num2 == 3:
        print('player 1 escolheu pedra \nPlayer 2 escolheu tesoura \nPlayer 1 ganhou =)')
        jog1 += 1
    elif num1 == 2  and num2 == 1:
        print('player 1 escolheu papel \nPlayer 2 escolheu pedra \nPlayer 1 ganhou =)')
        jog1 += 1
    elif num1 == 2  and num2 == 2:
        print('player 1 escolheu papel \nPlayer 2 escolheu papel \nDeu empate meu amores =)')
        empate += 1
    elif num1 == 2  and num2 == 3:
        print('player 1 escolheu papel \nPlayer 2 escolheu tesoura \nPlayer 2 ganhou =)')
        jog2 += 1
    elif num1 == 3  and num2 == 1:
        print('player 1 escolheu tesoura \nPlayer 2 escolheu pedra \nPlayer 2 ganhou =)')
        jog2 += 1
    elif num1 == 3  and num2 == 2:
        print('player 1 escolheu tesoura \nPlayer 2 escolheu papel \nPlayer 1 ganhou =)')
        jog1 += 1
    else:
        print('player 1 escolheu tesoura \nPlayer 2 escolheu tesoura \nDeu empate meu amores =)')
        empate += 1
    print(f"o placa está player 1 {jog1} x {jog2} player 2. \n Empates = {empate}")

    continuar = int(input("continuar? \n(1)Sim \n(2)Não \n"))
print(f"acabou placar final:\nPlayer 1 = {jog1} \nPlayer 2 = {jog2} \nEmpates = {empate}")
