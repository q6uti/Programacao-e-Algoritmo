import os
os.system("cls")

peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc <= 24.9:
    classificacao = "Peso normal"
elif imc <= 29.9:
    classificacao = "Sobrepeso"
elif imc <= 34.9:
    classificacao = "Obesidade Grau I"
elif imc <= 39.9:
    classificacao = "Obesidade Grau II"
else:
    classificacao = "Obesidade Grau III"

print(f"IMC calculado: {imc:.2f}")
print(f"Classificação: {classificacao}")