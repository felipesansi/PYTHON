# Definindo uma lista de nomes
lista_nomes = ["Felipe", "Mariana", "Ronaldo"]

# Usando um loop for para iterar sobre a lista de nomes e imprimir cada nome
for nome in lista_nomes:
    print(nome)


# Usando a função range para criar listas de números

# Cria uma lista de números de 0 a 4
n = list(range(5))
print(n)  # Saída: [0, 1, 2, 3, 4]

# Cria uma lista de números de 10 a 19
n = list(range(10, 20))
print(n)  # Saída: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# Cria uma lista de números de 20 a 28, pulando de 2 em 2
n = list(range(20, 30, 2))
print(n)  # Saída: [20, 22, 24, 26, 28]


# Separando números pares e ímpares

# Inicializa listas vazias para armazenar números pares e ímpares
par = []
impar = []

# Usando um loop for para iterar sobre o intervalo de 10 a 19
for i in range(10, 20):
    if i % 2 == 0:  # Verifica se o número é par
        par.append(i)  # Adiciona o número à lista de pares
    else:
        impar.append(i)  # Adiciona o número à lista de ímpares

# Imprime os números pares e ímpares
print("Os números pares:", par)
print("Os números ímpares:", impar)


# Usando a função enumerate para obter índices e valores da lista

# Imprime a lista de tuplas (índice, nome)
print(list(enumerate(lista_nomes)))

# Usando um loop for para iterar sobre a lista com índices
for a, b in enumerate(lista_nomes):
    if a == 2:  # Verifica se o índice é 2
        print("O nome de b é", b)  # Imprime o nome quando o índice é 2


# Usando um loop while para iterar sobre a lista de nomes

i = 0
# O loop continua enquanto i for menor que o comprimento da lista
while i < len(lista_nomes):
    print(i)  # Imprime o valor atual de i
    i += 1  # Incrementa i em 1


# Usando um loop while com break

n = 0
# O loop continua enquanto n for menor que o comprimento da lista
while n < len(lista_nomes):
    print("lista antes do if:", lista_nomes[n])  # Imprime o nome atual
    if lista_nomes[n] == "Felipe":  # Verifica se o nome é "Felipe"
        break  # Interrompe o loop se o nome for "Felipe"
    n += 1  # Incrementa n em 1

# Imprime o nome após o loop
print("depois do if:", lista_nomes[n])


# Usando um loop while com continue

n = 0
# O loop continua enquanto n for menor ou igual a 5
while n <= 5:
    n += 1  # Incrementa n em 1
    if n == 4:  # Verifica se n é igual a 4
        print("\n")  # Imprime uma linha em branco
        continue  # Continua para a próxima iteração, ignorando o que vem depois
print("depois do if", n)  # Imprime o valor final de n

# Corrigindo um erro de atribuição
n = 0  # Inicializa n com 0 novamente
n += 1  # Incrementa n em 1
