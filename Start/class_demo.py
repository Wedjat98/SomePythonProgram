class BenzCar:
    brand = '奔驰'
    country = '德国'

    @staticmethod
    def pressHorn():
        print('嘟嘟~~~~~~')

    def __init__(self, color, engineSN):
        self.color = color  # 颜色
        self.engineSN = engineSN  # 发动机编号

    def changeColor(self, newColor):
        self.color = newColor


car1 = BenzCar('白色', '24503425527866')
car1.changeColor('黑色')

print(car1.color)
