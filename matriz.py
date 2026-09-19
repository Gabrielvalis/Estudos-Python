# Programa para trabalhar com uma matriz 3x3

matriz = []

print("Digite os valores da matriz 3x3:")

for i in range(3):
    linha = []

    for j in range(3):
        valor = int(input(f"Digite o valor [{i}][{j}]: "))
        linha.append(valor)

    matriz.append(linha)

print("\nMatriz digitada:")

for linha in matriz:
    print(linha)

soma = 0

for linha in matriz:
    for valor in linha:
        soma += valor

diagonal = []

for i in range(3):
    diagonal.append(matriz[i][i])

print("\nSoma dos elementos:", soma)
print("Diagonal principal:", diagonal)
