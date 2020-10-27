import asyncio

async def print_every_second():
    """Print seconds"""
    while True:
        for i in range(60):
            print(i, 's')
            await asyncio.sleep(1)

async def print_every_minute():
    for i in range(1, 10):
        await asyncio.sleep(60)
        print(i, 'minute')
loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(print_every_second(),
                   print_every_minute())
#把两个函数合并到一起，创建了两个协程
)
loop.close()
