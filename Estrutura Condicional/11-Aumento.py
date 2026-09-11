import os
os.system("cls")

nome_funcionario = input("Digite o nome do funcionário: ")
salario_atual = float(input("Digite o salário atual: R$ "))

if salario_atual <= 2000:
    percentual = 0.10
elif salario_atual <= 5000:
    percentual = 0.07
else:
    percentual = 0.05

valor_aumento = salario_atual * percentual
novo_salario = salario_atual + valor_aumento

print(f"Funcionário: {nome_funcionario}")
print(f"Salário atual: R$ {salario_atual:.2f}")
print(f"Percentual de aumento: {percentual * 100:.0f}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")