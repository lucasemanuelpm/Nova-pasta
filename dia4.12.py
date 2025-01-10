saque = int(input("digite o valor do saque"))
cedula_100 = 100
cedula_50 = 50
cedula_20 = 20
cedula_10 = 10
cedula_5 = 5
cedula_2 = 2
if saque >= 100:
    cedula_100_100 = saque // 100
    saque = saque % 100  # Atualiza o valor restante
else:
    cedula_100_100 = 0
if saque >= 50:
    cedula_50 = saque // 50
    saque = saque % 100  # Atualiza o valor restante
else:
   cedula_50 = 0
if saque >= 20:
    cedula_20 = saque // 20
    saque = saque % 100  # Atualiza o valor restante
else:
   cedula_20 = 0
if saque >= 10:
    cedula_10 = saque // 10
    saque = saque % 100  # Atualiza o valor restante
else:
   cedula_10 = 0
if saque >= 5:
    cedula_5 = saque // 5
    saque = saque % 100  # Atualiza o valor restante
else:
   cedula_5 = 0
if saque >= 2:
    cedula_2 = saque // 2
    saque = saque % 100  # Atualiza o valor restante
else:
   cedula_2 = 0
if saque != 0:
 print("Não é possível sacar o valor especificado com as cédulas disponíveis")
else:
 print("Cédulas entregues:")
if cedula_100 > 0:
 print(f"{cedula_100} x R$100")
if cedula_50 > 0:
 print(f"{cedula_50} x R$50")
if cedula_20 > 0:
 print(f"{cedula_20} x R$20")
if cedula_10 > 0:
 print(f"{cedula_10} x R$10")
if cedula_5 > 0:
 print(f"{cedula_5} x R$5")
if cedula_2 > 0:
 print(f"{cedula_2} x R$2")