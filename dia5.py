#estrutura de repetição
#Repetir N vezes onde quem define é o usuario ou o programador
#ou n é uma condição
#For item_individual in lista
# bloco repeitdo N vezes
frutas = ["maça", "laranja", "banana"]
for fruta in frutas :
 print("Fruta:", fruta)
 for i in range (5) :
  print("Num" , i )
  print(frutas [0])
 print(frutas [1])
 #while 
 contador = 0 
 while contador < 5 :
   print("Num while " , contador)
   contador  +=  1
   # um loop com uma condição mal definida = loop infinito = bug
   for i in range(10):
    if i == 8 :
     break
    print("num for " , i)
 #break para o loop
 #continue pula a execução
for i in range(10):
    if i == 8 :
     continue
    print("num for " , i)