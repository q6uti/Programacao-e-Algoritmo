import os
os.system("cls")

valor_compra = float(input("Digite o valor da compra: R$ "))

print("Formas de pagamento disponíveis: \n 1 - PIX \n 2 - Dinheiro \n 3 - Cartão")
forma_pagamento = int(input("Escolha a forma de pagamento (1, 2 ou 3): "))

if forma_pagamento == 1:
    desconto = valor_compra * 0.10
elif forma_pagamento == 2:
    desconto = valor_compra * 0.05
else:
    desconto = 0

valor_final = valor_compra - desconto

print(f"Valor final da compra: R$ {valor_final:.2f}")