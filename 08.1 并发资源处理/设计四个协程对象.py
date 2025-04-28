import asyncio


async def subtract(x, y):
    result = x - y
    print(f'减法计算结果：{result}')


async def add(x, y):
    result = x + y
    print(f'加法计算结果：{result}')


async def main():
    coroutines = [
        subtract(10, 5), # 减法协程
        subtract(7, 3), # 减法协程
        add(2, 3), # 加法协程
        add(8, 2) # 加法协程
    ]
    await asyncio.gather(*coroutines)


if __name__ == '__main__':
    asyncio.run(main())
