# описываем класс человека. от него наследуется студент

class Pet:  # class Pet(object)-значит, что класс не наследуется ни от кого. не обязательная вещь, но так в явном
    # виде показываем, что класс ни от кого не наследуется.
    def __init__(self, name=None):  # инициализация экзмепляра класса
        self.name = name


class Dog(Pet):  # собаки наследуется от класса питомцев
    def __init__(self, name, breed=None):
        super().__init__(name)  # обращаемся к классу, от к-го мы наследуемся(Пет) с помощью супер()
        self.breed = breed

    def say(self):
        return f'{self.name}: Гав!'


dog = Dog('Шарик', 'Доберман')  # экземпляр класса Дог
print(dog.name, dog.breed)
print(dog.say())
