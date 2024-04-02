# ООП. класс-описание сущности с атрибутами(св-вами:фамилия, цвет глаз и тд). действия-методы.
# наследование-атрибуты и методы одного класса наследуются другим классом

class Robot:  # описываем класс робот, а не отдельного какого-то. должен создавать экземпляр.
    '''
    Class of robots.
    '''

    def __init__(self,
                 name):  # метод или атрибут с __ -магический метод, т.е. он уже существует. обязательно дб ссылка на экземпляр класса
        self.name = name  # self-ссылка на экземпляр класса, нейм-имя. создали атрбут нейм, в к-рый передил имя робота
        self.__power = 100  # начальный заряд робота 100(__power-защищенный атрибут)
        self.__mood = 100

    @property  # декоратор позволяет написанному методу стать свойством
    def mood(self):
        return self.__mood  # свойство отличается тем, что мы сможем задавать муд по своим правилам!!

    @mood.setter
    def mood(self, value):
        if isinstance(value, int) or isinstance(value, float):  # только если заряд инт или вещественн
            if 0 <= value <= 100:
                self.__mood = value

    @mood.getter
    def mood(self):
        if self.__mood > 80:
            return 'отличное'
        elif self.__mood > 60:
            return 'хорошее'
        elif self.__mood > 40:
            return 'не очень'
        return 'плохое'

    def say_hello(self):
        print('Привет!')
        self.__power -=1
        if self.__mood <= 99:
            self.__mood +=1


    def __eq__(self, other):
        return self.__power == other.__power  # сравнение по их энергии


    def get_power(self):
        return self.__power  # возвращает заряд


    def set_power(self, power):
        if isinstance(power, int) or isinstance(power, float):  # только если заряд инт или вещественн
            if 0 <= power <= 100:
                self.__power = power


    # переопределяем еще один метод(метод строкового представления)
    def __str__(self):  # метод стр чтобы печатать классы?
        return f'Робот: {self.name}'


    def __repr__(self):  # метод представления
        # return f'P.:{self.name}' == ретерну 22 строки
        return self.__str__(self)
