from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break

files = [f'./file {number}.txt' for number in range(1, 5)]
#start = datetime.now()
#for file in files:
#    read_info(file)
#end = datetime.now()
#time_delta = end - start
#print(f'Время линейного выполнения: {time_delta}') #0:00:04.341656

if __name__ == '__main__':
    start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)
    end = datetime.now()
    time_delta = end - start
    print(f'Время многопроцессорного выполнения: {time_delta}') #0:00:02.187855