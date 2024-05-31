import asyncio
import time
import datetime

# async def main():
#     print('hello')
    
#     # wait for one second then print worls
#     await asyncio.sleep(1)
#     print('world')
    

# asyncio.run(main())

async def play(delay,what):
    await asyncio.sleep(delay)
    print(what)

# Tasks are used to shedule coroutines


# async def main():
#     print(f'started at {time.strftime('%X')}')
#     task1 = asyncio.create_task(play(1,'hello'))
#     task2 = asyncio.create_task(play(2,'world'))
    
    
    
#     await task1
#     await task2
    
#     print(f"finished at {time.strftime('%X')}")

# either use the create task alone or use a tash grup
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(play(1,"hello"))
        task2 = tg.create_task(play(2,"world"))
        
        try:   
            task1.cancel
        except asyncio.CancelledError as e:
            print(e.add_note('kamaa cancelled'))
        
        
        print(f'started at {time.strftime('%X')}')
    print(f'finished at {time.strftime('%X')}')
    
    
    
async def getTime():
    loop = asyncio.get_running_loop()
    end_time = loop.time()+10.0
    
    while True:
        print(datetime.datetime.now())
        if(loop.time()+1.0)>=end_time:
            break
        await asyncio.sleep(1.0)
    
asyncio.run(getTime())


async def futures(fut,delay,value):
    await asyncio.sleep(delay)
    fut.set_result(value)
   
async def main2(): 
    loop = asyncio.get_running_loop()
    ft = loop.create_future()
    loop.create_task(
        futures(ft,1,42)
    )
    print('hello....')
    print(await ft)

asyncio.run(main2())