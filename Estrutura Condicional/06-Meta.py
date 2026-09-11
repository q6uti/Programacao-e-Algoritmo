import os
os.system("cls")

nome_vendedor = input("Digite o nome do vendedor: ")
total_vendido = float(input("Digite o valor total vendido no mês: R$ "))

if total_vendido >= 15000:
    desempenho = "Excelente"
elif total_vendido >= 10000:
    desempenho = "Meta atingida"
else:
    desempenho = "Meta não atingida"

print(f"Vendedor: {nome_vendedor}")
print(f"Total vendido: R$ {total_vendido:.2f}")
print(f"Desempenho: {desempenho}")