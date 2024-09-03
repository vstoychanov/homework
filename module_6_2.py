class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f'Модель:{self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя:{self.__engine_power}'

    def get_color(self):
        return f'Цвет:{self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        found_color = False
        for color in self.__COLOR_VARIANTS:
            if color.lower() == new_color.lower():
                self.__color = new_color
                found_color = True
                break
        if not found_color:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSANGER_LIMIT = 5
    def __init__(self, owner, model, color, engine_power):
        Vehicle.__init__(self, owner, model, color, engine_power)

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
