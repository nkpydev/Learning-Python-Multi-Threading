# Learning Python Multi-Threading

## What is Threading, or Multi Threading?

- Multithreading is the ability of CPU (Central Processing Unit) to provide multiple threads of execution concurrently.
- In layman terms, it is like: 
        - 1 worker can build a wall in 5 days.
        - 5 workers can build a wall in 1 day.
- We can visualize it like - We have to complete a work, we can divide that in granular forms of Tasks, assign those tasks to multiple workers.
- Basically many (multi) threads will start working in parallel to get 1 complete work done.

## Concepts

```python
# Python Library for multithreading
import threading

# Task1
def function1():
    #.....
    return 
# Task2
def function2():
    #.....
    return 

# Workers - t1 nad t2 | 2 threads
t1 = threading.Thread(target=function1,args=(arg_for_function1))
t2 = threading.Thread(target=function2),args=(arg_for_function2))

# If there are multiple args to be iterated thr' each thread should wait till all items are iterated, so join them.
t1.join()
t2.join()

# Start workers, or Threads
t1.start()
t2.start()

```