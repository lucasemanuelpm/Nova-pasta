pares = 0
impares = 0
for numero in range(1, 21):
 if numero % 2 == 0:
  pares += 1
else:
 impares += 1
print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)