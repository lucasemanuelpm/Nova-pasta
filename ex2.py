nome = input ("qual é o seu nome?")
altura = input ("qual é a sua altura")
idade = input ("qual é a sua idade?")
estudante = input("você é estudante?")
print("Bem vindo " , nome )
print("a sua idade é " , idade )
print( "sua altura é" , altura )
print(estudante)
ano_denascimento = int(2024 - idade)
print("seu ano de nascimento é " , ano_denascimento)
if idade < 18 :
 print("voce é maior de idade")
else: 
 print("você não é maior de idade")
