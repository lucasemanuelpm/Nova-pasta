numero = int(input("qual o numero voce deseja"))
pares = 0
impares = 0 
for i in range( 1, 21) :
    if i %2 == 0 :
        print("o numero é par")
        pares =+ 1
    elif i%3 == 0 :
        print("o numero é impar")
        impares +1