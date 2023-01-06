import math
resposta = "S"

input("Seja bem vindo, vamos começar? ")

#Variaveis
while resposta == "S":
    a = int(input('\nDigite o valor de A: '))
    b = int(input('\nDigite o valor de B: '))
    c = int(input('\nDigite o valor de C: '))

    #Formulas

    delta = b**2 -4*a*c
    raizdelta = math.sqrt(delta)
    x1 = (-b + raizdelta)/2*a
    x2 = (-b - raizdelta)/2*a

    print(f'O valor de x1 é igual a {x1} e o valor de x2 é igual a {x2}')

    resposta = input('Deseja continuar realizando operações? ').upper()

    if resposta != "S":
        print("Até a proxima!")