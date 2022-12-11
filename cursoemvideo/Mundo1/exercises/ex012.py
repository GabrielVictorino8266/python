# Crie um programa que calcule descontos de produtos.

productPrice = float(input("What's the price of the product? "))
discountPercentage = float(input("Discount (%): "))

newproductPrice = (productPrice - (productPrice / 100) * discountPercentage)

answer = 'The price after the discount is U$ {} .'
print(answer.format(round(newproductPrice, 2)))