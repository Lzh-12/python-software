import asyncio
import random


class ComputerFactory:
    def __init__(self):
        self.computer_count = 0

    async def produce_computer(self):
        while True:
            await asyncio.sleep(random.randint(1, 3))
            self.computer_count += 1
            print(f'【生产者】生产一台电脑，电脑数量统计：{self.computer_count}')
            await self.consumer_computer()

    async def consumer_computer(self):
        print('【消费者】搬走一台已经生成好的电脑。')
        await asyncio.sleep(random.randint(1, 3))


async def main():
    factory = ComputerFactory()
    await asyncio.gather(factory.produce_computer())


if __name__ == '__main__':
    asyncio.run(main())
