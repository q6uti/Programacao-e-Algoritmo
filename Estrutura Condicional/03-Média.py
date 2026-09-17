import os
os.system("cls")

nota1 = float(input("Insira sua nota do primeiro semestre: "))
nota2 = float(input("Insira sua nota do sengundo semestre: "))
nota3 = float(input("Insira sua nora do terceiro semestre: "))

resultado = (nota1 + nota2 + nota3) / 3

if resultado >= 7:
    print("Você foi aprovado!")
elif resultado > 4:
    print("Você esta de recuperação.")
else:
    print("Reprovado!")

print(f"Sua méida atual é {resultado:.2f}")

input("Precione Enter para finalizar o programa...")
