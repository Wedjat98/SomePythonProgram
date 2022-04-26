prices = input('please input some number\n').split()


def calcTax(price):
    afterTax = int(price) * 1.1
    print(f'before tex is {price},and after tex is {afterTax}')
    return afterTax


for p in prices:
    calcTax(p)
