from threading import Thread, Lock
from random import randint
from time import sleep

class Bank:
    def __init__(self, balance):
        self.balance = int(balance)
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            amount = randint(50, 500)
            with self.lock:
                self.balance += amount
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
                print(f'Пополнение: {amount}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for j in range(100):
            amount = randint(50, 500)
            print(f'Запрос на {amount}')
            if amount <= self.balance:
                self.balance -= amount
                print(f'Снятие: {amount}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank(0)

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
