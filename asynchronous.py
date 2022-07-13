import asyncio
import time
import threading

async def async_help_func():
    loop = asyncio.get_running_loop()
    print(loop)
    for i in range(5):

        # this will create a new coroutine and REGISTER ON EVENT LOOP
        await asyncio.sleep(2)

        # each coroutine works after sleeping for 2 seconds
        print(threading.active_count(), " thread alive ")  # actual user threads at this particular time
        print(str(threading.get_native_id()) + " thread: " + str(i+1))


async def mainfunc():
    # this is the evnet loop
    loop = asyncio.get_running_loop()
    start_time = time.time()

    # this is for registering coroutines to eventloop
    # we have registered same functions as 2 different COROUTINES
    # now these two coroutines will work in cooperative manner
    # eg: it will get preempted on asyncio.sleep
    await asyncio.gather(async_help_func(), async_help_func())

    end_time = time.time()
    result = end_time - start_time
    print("time taken in seconds ", result)
asyncio.run(mainfunc())
