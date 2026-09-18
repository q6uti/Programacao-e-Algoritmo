import os
os.system("cls")

# 1. Define o número base da tabuada
numero = 5

# 2. Cria o contador começando em 1
i = 1

# 3. Repete o bloco enquanto o contador 'i' for menor ou igual a 10
while i <= 10:

    # 4. Multiplica o 'i' pelo 'numero' e mostra o resultado
    print(f" {i} x {numero} = {i * numero}")
    
    # 5. Soma +1 no contador 'i' para avançar e evitar um loop infinito
    i += 1