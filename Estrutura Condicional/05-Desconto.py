import os
os.system("cls")

valor_compra = float(input("Digite o valor da compra: R$ "))

if valor_compra >= 500:
    desconto = valor_compra * 0.10
else:
    desconto = 0

valor_final = valor_compra - desconto

print(f"Valor original: R$ {valor_compra:.2f}")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor final da compra: R$ {valor_final:.2f}")