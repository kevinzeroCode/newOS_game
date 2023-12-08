import multiprocessing

def print_numbers(args):
    start, end = args
    for i in range(start, end):
        print(i)

if __name__ == "__main__":
    # 創建 Pool 並指定執行序數量（這裡使用默認值，即 CPU 核心數）
    with multiprocessing.Pool() as pool:
        # 使用 map 函數分配任務，這裡創建兩個任務
        pool.map(print_numbers, [(1, 6), (6, 11)])

    print("All processes are done.")
