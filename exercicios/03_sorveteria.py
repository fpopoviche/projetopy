#Faca um programa de uma sorveteria, onde o usuario pode escolher:
# a. Tipo de sorvete, casquinha 1,00 cascao 2,50 cestinha 4,00
# b. Sabor do sorvete, morango, creme, chocolate
# c. Cobertura, caramelo 1,50 morango 1,50 chocolate 1,50 sem cobertura 0,00
# apresente o valor a ser pago

#definindo valores
preco_casquinha = 1.0
preco_cascao = 2.50
preco_cestinha = 4.0
preco_cobertura = 1.50
valor_total = 0.0 
pedido_valido = True

#recebendo escolha do usuario
print("Escolha seu sorvete: ")
print("""
(1) Casquinha (R$1,00)
(2) Cascao (R$2,50)
(3) Cestinha (R$4,00)
      """)
escolha_sorvete = input("Digite a opcao que voce deseja")

#verificando escolhas e somando valores
if escolha_sorvete == "1": 
    valor_total += preco_casquinha
elif escolha_sorvete == "2":
    valor_total += preco_cascao
elif escolha_sorvete == "3":
    valor_total += preco_cestinha
else: 
    print('ERRO: escolha uma opcao valida (1, 2 ou 3)')
    pedido_valido = False #define que o pedido nao pode prosseguir.

if pedido_valido == True:

    #registrando escolha de sabor
    escolha_sabor = input("""
    Escolha o sabor:
    (1) Morango
    (2) Creme
    (3) Chocolate """)

    #verificando escolhas e somando valores
    validacao = input("""
    Voce deseja adicionar cobertura por R$1,50?
    (1) SIM
    (2) NAO
    """)

    if validacao == "1":
        escolha_cobertura = input("""
    Digite a opcao que voce deseja:                             
    (1) Caramelo
    (2) Morango
    (3) Chocolate
    """)
        valor_total += preco_cobertura #soma 1,50
    elif validacao == "2":
        print("Que pena!")

    else: print("Escolha uma opcao valida (1 ou 2)")

    print("O valor total do seu pedido eh R$: ", valor_total)