print("*****************************")
print("**** Jogo de Adivinhação ****")
print("*****************************")

numero_secreto = 42;

chute_str = input("Digite seu numero: ")
print("Você digitou: ", chute_str);
chute = int(chute_str)

if (numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou!")

print("Fim do Jogo")
