def five_discount():
    product_price = float(input('Enter the price of the product: '))

    discount = product_price * 0.05
    final_price = product_price - discount

    print(f'The original price of the product is {product_price} USD')
    print(f'The price with discount is {final_price} USD')


five_discount()
input("Press Enter to Exit ... ")
