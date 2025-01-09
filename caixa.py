emprestimo = float(input("digite o valor do emprestimo"))
renda_mensal = float(input("Digite sua renda mensal: ")) 
parcelas = int(input("deseja pagar em quantas parcelas?"))
porcentagem_renda = renda_mensal*0.30
valor_parcela = emprestimo/parcelas
print(valor_parcela)
print(porcentagem_renda)
if valor_parcela >= porcentagem_renda :
    print("voce nao é digno da parcela")


