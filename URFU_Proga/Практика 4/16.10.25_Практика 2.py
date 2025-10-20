class Transport:
    def get_description(self):
        return "Транспортное средство"

class Car(Transport):
    def get_description(self):
        return "Автомобиль - ездит по дорогам"

class Bicycle(Transport):
    def get_description(self):
        return "Велосипед - приводится в движение педалями"

class Airplane(Transport):
    def get_description(self):
        return "Самолет - летает по воздуху"

# Демонстрация
def trans(name):
    return name.get_description()

print(trans(Car()))
print(trans(Bicycle()))
print(trans(Airplane()))
