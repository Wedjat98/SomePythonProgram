prices = input('please input some number\n').split()
for price in prices:
    afterTax = int(price)*1.1
    print(f'before tex is {price},and after tex is {afterTax}')

