import os
os.system("cls")

nome_vendedor = input("Digite o nome do vendedor: ")
valor_vendas = float(input("Digite o valor das vendas: R$ "))

if valor_vendas > 20000:
    percentual = 0.10
elif valor_vendas > 10000:
    percentual = 0.07
else:
    percentual = 0.05

comissao = valor_vendas * percentual

print(f"Vendedor: {nome_vendedor}")
print(f"Valor vendido: R$ {valor_vendas:.2f}")
print(f"Percentual de comissão: {percentual * 100:.0f}%")
print(f"Valor da comissão: R$ {comissao:.2f}")