import os
os.system("cls")

nome_cliente = input("Digite o nome do cliente: ")
total_comprado = float(input("Digite o total comprado no mês: R$ "))

if total_comprado >= 5000:
    classificacao = "Cliente Ouro"
elif total_comprado >= 2000:
    classificacao = "Cliente Prata"
else:
    classificacao = "Cliente Bronze"

print(f"Cliente: {nome_cliente}")
print(f"Total comprado: R$ {total_comprado:.2f}")
print(f"Classificação: {classificacao}")