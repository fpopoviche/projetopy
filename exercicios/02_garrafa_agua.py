#FACA UM PROGRAMA QUE VENDE UMA GARRAFA DE AGUA
# SE O CLIENTE ESCOLHER AGUA MINERAL NATURAL, SERA COBRADO 1,50
# SE O CLIENTE ESCOLHER AGUA MINERAL COM GAS, SERA COBRADO 2,50

texto = """"
Escolha a sua agua para comprar
(1) Agua mineral natural
(2) Agua mineral com gas
"""

opcao = input(texto)

conta = 0
if opcao == "1":
    conta = 1.5
    print("O valor a ser pago eh: 1,50")

elif opcao == "2":
    conta = 2.5
    print('O valor a ser pago eh: 2,50 ')

if conta == 0:
    print('Escolha uma opcao valida')
else:
    print('Sua conta eh: R$', conta)