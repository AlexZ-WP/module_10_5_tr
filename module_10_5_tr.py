
import multiprocessing
import time
import threading
from multiprocessing import Pool

def read_info(name):
    all_data =[]
    for i in name:
        with open(i, 'r', encoding='utf-8') as f: #Открывать файл name для чтения.
            lines = f.readline()# Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
            for line in lines:
                if line.strip():
                    all_data.append(f.readline())  # Во время считывания добавлять каждую строку в список all_data.
                else:
                    return
        


start_time = time.time()

filenames = [f'./file {number}.txt' for number in range(1, 5)]
name = filenames
thread1 = threading.Thread(target=read_info(name))
thread1.start()
end_time = time.time()
elapsed_time = start_time - end_time
print(elapsed_time)

if __name__ == '__main__':
    start_time = time.time()
    # filenames = [f'./file {number}.txt' for number in range(1, 5)]
    # name = filenames
    process1 = multiprocessing.Process(target=read_info(name))
    process1.start()

    with Pool(name) as p:
        p.map(read_info(name))
    end_time = time.time()
    elapsed_time = start_time - end_time


    print(elapsed_time)
