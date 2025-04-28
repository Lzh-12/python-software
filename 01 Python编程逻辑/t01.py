for cock in range(0, 21):
    for hen in range(0, 34):
        chicken = 100 - hen - cock
        if 5*cock + 3*hen + chicken/3 == 100:
            print(f"公鸡：{cock} - 母鸡：{hen} - 小鸡{chicken}")
