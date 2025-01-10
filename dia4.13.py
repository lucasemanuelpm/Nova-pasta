valor_saque = int(input("Digite o valor do saque: R$"))
if valor_saque <= 0:
 print("Valor inválido.")
else:
 cedulas_100 = valor_saque // 100
valor_saque %= 100
cedulas_50 = valor_saque // 50
valor_saque %= 50
cedulas_20 = valor_saque // 20
valor_saque %= 20
cedulas_10 = valor_saque // 10
valor_saque %= 10
cedulas_5 = valor_saque // 5
valor_saque %= 5
cedulas_2 = valor_saque // 2
valor_saque %= 2
if valor_saque != 0:
 print("Não é possível sacar o valor especificado com as cédulas disponíveis")
else:
 print("Cédulas entregues:")
if cedulas_100 > 0:
 print(f"{cedulas_100} x R$100")
if cedulas_50 > 0:
 print(f"{cedulas_50} x R$50")
if cedulas_20 > 0:
 print(f"{cedulas_20} x R$20")
if cedulas_10 > 0:
 print(f"{cedulas_10} x R$10")
if cedulas_5 > 0:
 print(f"{cedulas_5} x R$5")
if cedulas_2 > 0:
 print(f"{cedulas_2} x R$2")