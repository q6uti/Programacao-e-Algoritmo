import os
os.system("cls")

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade!")

    carteira = input("Possui habilitação? \n 1 - Sim \n 0 - Não \n ")

    if carteira == "1":
        print("Pode dirigir!")
    elif carteira == "0":
        print("Não pode! Vá fazer Habilitação!")
    elif carteira:
        print("Nenhuma opção disponível selecionada!")

else:
    print("Você é de menor!")

input("Precione Enter para finalizar o programa...")
