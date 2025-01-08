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

#senha
senha_inserida = "12345"
senha_correta = "12345"
usuario_bloqueado = False
acesso_permitido = (senha_inserida == senha_correta) and   (usuario_bloqueado == False)
print("parabens acesso permitido" ,  acesso_permitido) 

#divisão de tarefas
conta = 150.00
pessoas = 3
valorpor_pessoas = (conta/pessoas)
divisão_exata = conta%pessoas == 0 
print(valorpor_pessoas)
print(divisão_exata)
