import os
os.system("cls")

temperatura = float(input("Digite a temperatura atual: "))

if temperatura >= 30:
    print("Está Quente!")
elif temperatura >= 20:
    print("Está agradável")
else:
    print("Está frio!")

input("Precione Enter para finalizar o programa...")
