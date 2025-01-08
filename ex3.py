pão = 3.50
leite = 4.20
café = 2.80
total_dacompra = (pão + leite + café)
print(total_dacompra)
total_pago = 20
troco = (total_pago - total_dacompra )
print(troco)

nota_media = 85
frequencia = "80%"

nota_minima = (nota_media>= 60)
frequencia_minima = (frequencia>= "80%")
print("parabens voce passou em notas com :" ,  nota_media)
print("parabens voce apsssou com uma frequencia de :" , frequencia)

#ofertaespecial
itens = 8
valor_total = 120
desconto = (valor_total>= 100) or (itens>=10)
print(desconto ,  "aprovado")

