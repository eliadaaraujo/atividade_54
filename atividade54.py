# Leia 10 números inteiros e armazene-os em uma lista.
# Mostre a soma dos pares e a soma dos ímpares separadamente.
# Exemplo: [2, 3, 4, 5] → pares = 6, ímpares = 8.

numeros = []
somapares = 0
somaimpares = 0
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

    if numero % 2 == 0:
        somapares += numero
    else:
        somaimpares += numero

print(f'Números: {numeros} soma dos pares: {somapares} soma dos impares: {somaimpares}')