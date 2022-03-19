import asyncio

async def f1():
    task= asyncio.create_task(f2())
    
    print("Mr.")
    r_value=await task
    print("ji")
    
   
    print(f"Return Value is {r_value}")
    
async def f2():
    print("Himanshu")
    # await asyncio.sleep(1)
    print("Rajore")
    return 10
    
asyncio.run(f1())