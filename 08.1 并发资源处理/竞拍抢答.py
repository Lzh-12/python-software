import multiprocessing, random, time


def contestant(name):
    time.sleep(random.randint(1, 5))
    if random.randint(0, 1):
        print(f'{name}抢答成功！')
    else:
        print(f'{name}抢答失败！')


def main():
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=contestant, args=(f'抢答者{i + 1}',))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()


if __name__ == '__main__':
    main()
