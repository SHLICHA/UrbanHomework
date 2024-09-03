from threading import Thread
from time import sleep
from datetime import datetime


def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for word in range(word_count):
            file.write(f'Какое-то слово №{word + 1}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
time_end = datetime.now()
time_delta = time_end - time_start
print(f'Работа потоков {time_delta}')

time_start = datetime.now()
th_first = Thread(target=wite_words, args=(10, 'example1.txt'))
th_second = Thread(target=wite_words, args=(30, 'example2.txt'))
th_third = Thread(target=wite_words, args=(200, 'example3.txt'))
th_fourth = Thread(target=wite_words, args=(100, 'example4.txt'))
th_first.start()
th_second.start()
th_third.start()
th_fourth.start()
th_first.join()
th_second.join()
th_third.join()
th_fourth.join()
time_end = datetime.now()
time_delta = time_end - time_start
print(f'Работа потоков {time_delta}')
