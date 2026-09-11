import os
os.system("cls")

fornecedor1 = input("Digite o nome do fornecedor 1: ")
valor1 = float(input(f"Digite o valor da proposta de {fornecedor1}: R$ "))

fornecedor2 = input("Digite o nome do fornecedor 2: ")
valor2 = float(input(f"Digite o valor da proposta de {fornecedor2}: R$ "))

if valor1 < valor2:
    print(f"{fornecedor1} apresentou o menor preço.")
elif valor2 < valor1:
    print(f"{fornecedor2} apresentou o menor preço.")
else:
    print("As propostas possuem o mesmo valor.")