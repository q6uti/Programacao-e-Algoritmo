import os
os.system("cls")

valor_compra = float(input("Digite o valor da compra: R$ "))

if valor_compra >= 300:
    frete = 0
else:
    frete = 25

valor_final = valor_compra + frete

print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Valor do frete: R$ {frete:.2f}")
print(f"Valor final do pedido: R$ {valor_final:.2f}")