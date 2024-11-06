from datetime import datetime
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8')as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)
    return all_data

if __name__ == "__main__":
    files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

    start_1 = datetime.now()
    for file in files:
        read_info(file)

    end_1 = datetime.now()
    time_res_1 = end_1 - start_1
    print(time_res_1)

    start_2 = datetime.now()
    with multiprocessing.Pool(processes=2) as pool:
        pool.map(read_info, files)
    end_2 = datetime.now()
    time_res_2 = end_2 - start_2
    print(time_res_2)

