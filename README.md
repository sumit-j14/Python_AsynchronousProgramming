# Python_AsynchronousProgramming
concepts of eventloop,coroutines,etc
# asynchronous vs multiprocessing  
in multiprocessing, we have different processes running in preemptive manner as per kernel algorithms  
and it takes lot of overheads of context switching upon process preemption  
and furthermore these preemptions can occus at a any random time  
So to overcome these issues we use CoRoutines  
# coRoutines basics  
basically coroutines can be understood as two Threads which run in a "COOPERATIVE multi-tasking manner"  
for example if one corroutine has to wait for I/O then that coroutine will be paused for some time  
and other coroutines Registered on the eventloop will get chance of execution  
# eventloop  
in very simple words eventloop is a DataStructure to manage all coroutines  
# output  
![Screenshot from 2022-07-14 02-55-21](https://user-images.githubusercontent.com/72104547/178840803-47b67747-a19a-4f7a-9026-4a8a25eeb7ec.png)  
Point to notice is that ONLY ONE KERNEL LEVEL thread gets created  
# async/await  
the asynchronous functions (Coroutines) need to be declared "async"  
and the program exection resumes at the code written after the keyword "await"
