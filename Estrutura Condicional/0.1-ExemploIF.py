import os
os.system("cls")

nascimento = int(input("Informe seu ano de nascimento: "))
atual = int(input("Informe o ano atual: "))

a1 = nascimento - nascimento

# SE a idade for maior ou igual a 18:
if a1 > 18:
    print("Você é maior de idade.")

# SENÃO (se ele NÃO FOR maior ou igual a 18, ou seja, se for menor):
else:
    print("Você é menor de idade.")

input("Precione Enter para finalizar o programa...")
