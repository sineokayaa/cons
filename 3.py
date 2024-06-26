class Robot:
    pass


r = Robot()

'''
print(type(r))  # <class '__main__.Robot'>
a = 5
print(type(a))  # <class 'int'>
print(isinstance(a, int))  # True

print(isinstance(a, Robot))  # False

print(dir(Robot))  # список магических методов, к-рые уже присутствуют в этом классе


d = []
for i in range(5):
    d.append(Robot())
print(d)  # список из 5 ссылок на экзмепляры класса. это все из-за того, что метод представления не переопределен
'''


class Robot:
    elem = []  # атрибут! класса, относится ко всему классу. напр, ускорение свободного падения для мяча.

    # тогда его форма, цвет и тп-атрибуты экзампляров класса
    def __new__(cls, *args, **kwargs):  # конструктор класса-метод(например в СИ), к-рый создает экземпляр класса.
        # __init__ не создает экземпляр класса. создает __new__
        obj = super().__new__(cls)  # создает экземпляр
        return obj

    def __init__(self, number):  # селф-экзмепляр
        self.__number = number  # атрибут экземпляра! класса. del на него также работает. _number-не трогать за пределеами класса.
        # __number-недоступен за пределеами класса
        # new срабатывает раньше, чем init. сначала создает объект, а init
        # устанавливает атрибуты. инит-инициализация,нью-конструктор. на питоне методы инициализации пишут.
        Robot.elem.append(self)
        Robot.say()  # не метод класса, с классом она не работает.
        self.__power = 100

    power = property()

    @power.setter
    def power(self, value):
        self.__power = value

    @power.getter
    def power(self):
        return self.__power

    @power.deletter
    def power(self):
        del self.__power

    # описывая класс, переопределяем магич.методы,к-рые там есть(инициализация(в классич.программировании-контруктор))
    # есть атрибуты и методы экземпляров класса(с параметром селф).
    # есть атрибуты и методы класса!
    # есть методы-статики.
    # есть свой-ства, связанные с защищенными атрибутами. чтобы их описать, нужно переопределить сеттеры и геттеры
    # метод хорошего тона: переопределение стр и репр, документ-строки(!) как у класса, так и у всех методов(!)
    def __repr__(self):  # если бы был стр, то список выводился бы ссылками, а робот Робот №2.
        return f'Робот №{self.number}'  # переопределен метод репр

    @classmethod  # метод класса. метод для экзмепляра, а инит и нью-методы экзепляров
    def double(cls):
        n = len(cls.elem)  # длина атрибута класса
        for i in range(n):
            cls.elem[i].number *= 2  # умножили на 2 номер каждого робота

    @staticmethod  # к классу не имеют никакого отношения. вспомогательный метод, не привязанный к экземпляру.
    # просто описан внутри класса
    def say():  # ничей метод. не имеет ссылки на экземпляр. он сам по себе.
        print('Ррр-р-р-р-р!!')


d = []
for i in range(5):
    d.append(Robot(i))

print(Robot.elem)  # атрибут класса, который хранит все экземпляры класса. атрибут доступен внутри класса
# [Робот №0, Робот №1, Робот №2, Робот №3, Робот №4]
Robot.double()  # применяем метод для класса!!
print(Robot.elem)  # [Робот №0, Робот №2, Робот №4, Робот №6, Робот №8]

'''
print(d)  # [Робот №0, Робот №1, Робот №2, Робот №3, Робот №4]
print(d[2])  # Робот №2. хоть и без стр, но благодаря репр распечатать получается

print(d[3].number)  # 3-номер робота
# print(d[3].num) 'Robot' object has no attribute 'num'

d[3].num = d[3].number * 2
print(d[3].num)  # 6
del d[3].num # удаление атрибута у экзамепляра из класса
# print(d[2].num) # атрибут существует только для одного экзамепляра(3)
print(d[3].num) # 'Robot' object has no attribute 'num'
'''
