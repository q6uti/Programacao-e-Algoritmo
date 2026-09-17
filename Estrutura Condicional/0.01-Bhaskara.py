a = float(input("Digite o coeficiente  A: "))
b = float(input("Digite o coeficiente  B: "))
c = float(input("Digite o coeficiente  C: "))

delta = ( b ** 2 ) - 4 * a * c

x1 = ( -b + delta ) / (2 * a)
x2 = ( -b - delta ) / (2 * a)

if delta > 0:
    print(f"A equação terá duas raízes reais e distintas. \n x1 = {x1} \n x2 = {x2}")

elif delta == 0: 
    print(f"A equação apresentará uma raiz real. \n x1 = {x1} \n x2 = {x2}")

else:
    print(f"A equação não possui raízes reais. \n {delta}")

input("Precione Enter para finalizar o programa...")
