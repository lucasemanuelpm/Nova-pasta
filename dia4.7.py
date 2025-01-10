num1 = float(input("qual o primeiro número quee voce deseja?"))
num2 = float(input("qual o segundo número quee voce deseja?"))
operação  = str(input("qual operação você deseja ?soma, subtração, multiplicação ou divisão"))
if operação == "soma" :
    print(num1+num2)
elif operação == "subtração" :
    print(num1-num2)
elif operação == "multiplicação" :
    print(num1 * num2)
elif operação == "divisão":
    print(num1/num2)
else: 
    print("por favor digite um número valido")

