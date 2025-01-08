#operadores aritmeticos
a = 4
b = 6
print( a + b)
print(a - b)
print(a * b)
print(a/b)
# ** - exponenciação
# // divisão inteira
 
print(a//b)
print(a%b)

#operadores de comparação
x = 5
y = 4
print(x<y)
print(x>y)
print(x!=y)
print(5>=4)
print(5<=4)
#operadores lógicos
#AND OR E NOT
#unircomparações
idade = 19
possui_carteira = True
pode_digirir = (idade>=18) and possui_carteira
print(pode_digirir)
#AND só é verdadeiro quando ambos os resultados resultam em true
#OR é verdadeiro quando uma operação resulta em true
eh_estudante = False
idade = 60

meia_entrada = eh_estudante == True or idade>=60
print(meia_entrada)
#NOT INVERTER UM BOOL
chovendo = True
nao_chovendo = False
print( "chovendo", chovendo)
print("nao chovendo", nao_chovendo)