#dz6

#1
from time import sleep

class TrafficLight:
    color = ('красный', 'желтый', 'зеленый')

    def running(self):
        for i in TrafficLight.color:
            if i == TrafficLight.color[0]:
                print(i)
                sleep(7)
            elif i == TrafficLight.color[1]:
                print(i)
                sleep(2)
            elif i == TrafficLight.color[2]:
                print(i)
                sleep(3)

TrafficLight().running()

#2
class Road:
    def set_road(self, _length, _width):
        print(_length * _width * 25 * 5)

a = Road()
a.set_road(20, 5000)


#3

class Worker:
    name = ('Иван')
    surname = ('Сидоров')
    position = ('Строитель')
    _income = {"wage": 12500, "bonus": 4000}

class Position(Worker):
    def get_full_name(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        print(f'Имя: {self.name}, Фамилия: {self.surname}, Должность: {self.position}')
        print(f'Имя: {Worker.name}, Фамилия: {Worker.surname}, Должность: {Worker.position}')
    # def get_total_income(self):
    #     print('Сумма дохода:', sum(Worker._income.values()))

    def get_total_income(self):
        print(list(self._income.values()))
        print('Сумма дохода:', sum(self._income.values()))


Position().get_full_name('Сергей', 'Петров', 'Повар')
Position().get_total_income()


#4
class Car:
    name = 'Mazda'
    color = 'Red'
    speed = 140
    is_police = 1

    def go(self):
        return f'Авто: едет'

    def stop(self):
        return f'Авто: стоит'

    def turn_left(self):
        return f'Авто: едет на лево'

    def turn_right(self):
        return f'Авто: едет на право'

    def show_speed(self):
        print(f'Скорость авто {self.name}, {self.speed} км/ч')

class TownCar(Car):
    def set_info(self):
        print(f'TownCar: name: {self.name}, color: {self.color},', self.go())

    def show_speed(self, speed):
        self.speed = speed
        print(f'Скорость авто {self.name}, {self.speed} км/ч')
        if self.speed >= 60:
            print(f'Скорость {self.name} привышена')
        else:
            print(f'Скрость {self.name} является разрешенной')

class SportCar(Car):
    def set_info(self, name, color):
        self.name = name
        self.color = color
        print(f'SportCar: name: {self.name}, color: {self.color}, speed: {self.speed},', self.stop())

class WorkCar(Car):
    def set_info(self, name, color):
        self.name = name
        self.color = color
        print(f'WorkCar: name: {self.name}, color: {self.color},', self.turn_left())

    def show_speed(self, name, speed):
        self.name = name
        self.speed = speed
        print(f'Скорость авто {self.name}, {self.speed} км/ч,')
        if self.speed >= 40:
            print(f'Скорость {self.name} привышена')
        else:
            print(f'Скрость {self.name} является разрешенной')


class PoliceCar(Car):
    def set_info(self, name, color):
        self.name = name
        self.color = color
        print(f'PoliceCar: name: {self.name}, color: {self.color}, speed: {self.speed},', self.turn_right())

        if Car().is_police == 1:
            print(f'{self.name} Полицейская машина')
        else:
            print(f'{self.name} Не Полицейская машина')

car1 = Car()
TownCar().set_info()
TownCar().show_speed(50)
SportCar().set_info('McLaren', 'green')
WorkCar().set_info('Ford', 'blue')
WorkCar().show_speed('Ford', 60)
PoliceCar().set_info('Chevrolet', 'black')

#5
class Stationery:
    title = ('Ручка', 'Карандаш', 'Маркер')

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки', Stationery.title[0])

class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки', Stationery.title[1])

class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки', Stationery.title[2])

s = Stationery()
s.draw()
Pen().draw()
Pencil().draw()
Handle().draw()