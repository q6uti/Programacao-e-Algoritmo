import os
os.system("cls")

salario = float(input("Digite o salário do cliente: R$ "))
valor_parcela = float(input("Digite o valor da parcela desejada: R$ "))

limite_parcela = salario * 0.30

if valor_parcela <= limite_parcela:
    print("Empréstimo aprovado")
else:
    print("Empréstimo não aprovado")