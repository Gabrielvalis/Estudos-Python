
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Criamos uma matriz 3x3 para analisar.
matriz = [
    [8, 2, 5],
    [4, 6, 1],
    [3, 7, 9]
]

# NumPy: calcula a soma de todos os elementos.
array = np.array(matriz)
soma_total = np.sum(array)

# Pandas: organiza os dados em uma tabela.
tabela = pd.DataFrame(
    matriz,
    columns=["Coluna 0", "Coluna 1", "Coluna 2"]
)

print("Matriz:")
print(tabela)

print("\nSoma total:", soma_total)
print("\nMédia de cada coluna:")
print(tabela.mean())

# Matplotlib: cria um gráfico dos valores da matriz.
plt.imshow(array, cmap="viridis")
plt.colorbar(label="Valor")
plt.title("Visualização da matriz 3x3")
plt.xlabel("Colunas")
plt.ylabel("Linhas")
plt.savefig("matriz_grafico.png")
plt.show()

