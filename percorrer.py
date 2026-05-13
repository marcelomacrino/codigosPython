numeros = [10,20,30,40,50]

for numero in numeros:
    print(numero)

for i in range(len(numeros)):
    print(f"posicao:  {i+1}: {numeros[i]}")

numeros.append(89)

print(numeros)

numeros.insert(3,67)

print(numeros)

numeros.remove(10)

print(numeros)

numeros.pop(4)

print(numeros)

len(numeros)

print(len(numeros))

numeros.sort()

print(numeros)

numeros.sort(reverse=True)

print(numeros)