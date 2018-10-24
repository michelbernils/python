
'''
numero_secreto = 42
chute_str = input("Chute um numero: ")
chute = int(chute_str)

if (numero_secreto == chute):
    print("Você Acertou o numero")
else:
    if (chute > numero_secreto):
        print("Você errou! O seu chute foi maior que o número secreto.")
    if (chute < numero_secreto):
        print("Você errou! O seu chute foi menor que o número secreto.")
'''


numero_secreto = 10
chute_str = input("Chute um numero: ")
chute = int(chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    print("Você acertou!")
else:
    if (maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
        print("Você errou! O seu chute foi menor que o número secreto.")
