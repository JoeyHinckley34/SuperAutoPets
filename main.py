import time

def main():
    print("SUPER AUTO PETS")


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print('Execution time: ' + str(round(end - start,2)))
