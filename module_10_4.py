import queue
from threading import Thread
from random import randint
from time import sleep
from queue import Queue


class Table:
    quest = None

    def __init__(self, number):
        self.number = number


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        waiting = randint(3, 10)
        sleep(waiting)


class Cafe:
    queue = Queue()

    def __init__(self, *tables):
        self.tables = [table for table in tables]

    def guest_arrival(self, *quests):
        for quest in quests:
            is_sit = False
            for table in self.tables:
                if table.quest is None:
                    table.quest = quest
                    table.quest.start()
                    is_sit = True
                    print(f'{quest.name} сел(-а) за стол номер {table.number}')
                    break
            if not is_sit:
                self.queue.put(quest)

    def discuss_guests(self):
        while not self.queue.empty():
            for table in self.tables:
                if not table.quest is None and not table.quest.is_alive():
                    print(f'{table.quest.name} покушал(-а) и ушел(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.quest = None
                    if not self.queue.empty():
                        next_quest = self.queue.get()
                        self.guest_arrival(next_quest)
                        print(f'{next_quest.name} вышел из очереди и сел(-а) за стол номер {table.number}')


tables = [Table(number) for number in range(1, 6)]
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
