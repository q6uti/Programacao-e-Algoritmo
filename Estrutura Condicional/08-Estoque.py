import os
os.system("cls")

produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade disponível em estoque: "))

if quantidade < 10:
    situacao = "Estoque crítico"
elif quantidade <= 30:
    situacao = "Estoque baixo"
else:
    situacao = "Estoque adequado"

print(f"Produto: {produto}")
print(f"Quantidade: {quantidade}")
print(f"Situação: {situacao}")