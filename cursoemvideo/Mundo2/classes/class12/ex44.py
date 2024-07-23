menu = """
    **************MENU**************
    |  1- A VISTA DINHEIRO/CHEQUE  |
    |  2- A VISTA CARTAO           |
    |  3- PARCELADO 2X             |
    |  4- PARCELADO 3X             |
    |  5- Sair                     |
    **************MENU**************

"""

while True: 

    product_price = float(input("Informe o preço do produto: "))
    payment_method = int(input("Digite sua opção de escolha do menu: "))
    payment_text = ""

    if payment_method == 1:
        product_price -= product_price*0.1
        payment_text = "A VISTA DINHEIRO/CHEQUE"
    elif payment_method == 2:
        product_price -= product_price*0.05
        payment_text = "A VISTA CARTAO"
    elif payment_method == 3:
        product_price = product_price / 2
        payment_text = "PARCELADO 2X COM O PRECO FORMAL"
    elif payment_method == 4:
        product_price =( product_price*1.20)/3
        payment_text = "PARCELADO 3X COM O 20% ACRESCIMO"
    elif payment_method == 5:
        break
    else:
        print("Verifique o menu e tente novamente.")

    print(f"Seu pagamento final será no valor de R${product_price} com o método {payment_text}")