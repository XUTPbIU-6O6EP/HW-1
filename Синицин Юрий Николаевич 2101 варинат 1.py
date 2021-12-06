import math
from time import time

def vremya(func):
    def vremyaVipolnenia(*args):
        start = time()
        func(*args)
        print('Время работы функции:', time() - start)
    return vremyaVipolnenia

def decorat(func):
    def name(*args):
        print('Была вызвана функция', func.__name__)
        func(*args)
    return name


@vremya
@decorat
def ploshad(length, width):
    print ('Площадь садового участка в акрах =', (length*width)/43560)

@vremya
@decorat
def padenie(d):
    speed = math.sqrt(0 ** 2 + 2 * 9.8 * d)
    print('Финальная скорость при падении =', speed, 'м/с')



length, width = float(input('Введите длину садового участка в футах: ')), float(input('Введите ширину садового участка в футах: '))
ploshad(length, width)
d = float(input('Введите начальную высоту падения шара в метрах: '))
padenie(d)
