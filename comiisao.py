comissao_1000 = 5/1000
comissao_500 = 1/500
comissao_0500 = 2/750
comissao = int(input("qual foi o valor da sua venda"))
if comissao == 1000 :
    print( "entao voce ganhou " , 0.05*1000 , "de comissao" )
elif comissao == 500 :
    print("entao voce ganhou" , 0.01*500 , "de comissao")
elif comissao == 750 :
    print("entao voce ganhou" , 00.2*750 , "de comissao")
