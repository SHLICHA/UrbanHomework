from random import randint
from threading import  Thread, Lock
from time import sleep


class Bank:
    lock = Lock()

    def __init__(self):
        self.balance: int = 0

    def deposit(self):
        for i in range(100):
            entrance = randint(50, 500)
            self.balance += entrance
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {entrance}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            cut = randint(50, 500)
            print(f'Запрос на {cut}')
            if cut <= self.balance:
                self.balance -= cut
                print(f'Снятие: {cut}, Баланс: {self.balance}')
            else:
                print('Запрос отклонен. Недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')