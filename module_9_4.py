import random
from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

list(map(lambda x, y: x == y, first, second))

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding= 'uft-8') as file:
            file.writelines((str(data) + '\n' for data in data_set))
    return write_everything

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())