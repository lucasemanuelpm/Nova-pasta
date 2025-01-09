emprestimo = float(input("digite o valor do empresitmo"))
renda_mensal = float(input("Digite sua renda mensal: ")) 
porcentagem_renda = (renda_mensal*0.30)
parcelas = 12
valor_parcela = print(emprestimo/parcelas)
if valor_parcela> porcentagem_renda:
    print("infelzimente voce nao pode fazer esse emprestimo")
else :
    print('otimo voce esta apto ao emprestimo')

