import os
os.system("cls")

nome = input("Nome do cliente: ")
nome_produto = input("Nome do produto: ")
preco_unitario = float(input("Preço unitário: R$ "))
quantidade = int(input("Quantidade: "))

subtotal = preco_unitario * quantidade

if subtotal > 1000:
    desconto = 0.15
elif subtotal > 500:
    desconto = 0.10
elif subtotal > 200:
    desconto = 0.05
else:
    desconto = 0.0

valor_desconto = subtotal * desconto
total_pagar = subtotal - valor_desconto

print(f"Cliente: {nome}")
print(f"Produto: {nome_produto}")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Desconto aplicado: {desconto * 100:.0f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Total a pagar: R$ {total_pagar:.2f}")

input("Precione Enter para finalizar o proramaga...")