<div align="center"><img src="https://github.com/vtiquet/holbertonschool-resources/blob/main/image/Holberton-Logo.svg" width=40% height=40%/></div>

# Resources

## Table of Contents :

  - [0. The basics of async](#subparagraph0)
  - [1. Let's execute multiple coroutines at the same time with async](#subparagraph1)
  - [2. Measure the runtime](#subparagraph2)
  - [3. Tasks](#subparagraph3)
  - [4. Tasks](#subparagraph4)

## Resources
### Read or watch:
* [Async IO in Python: A Complete Walkthrough](/rltoken/IDv2YZ5p7QHF5SxYZBMGdQ)
* [asyncio - Asynchronous I/O](/rltoken/1neoNd8gRS_mn52IQd5WTQ)
* [random.uniform](/rltoken/XTxPUx9tDxZ51zhIUrSvPw)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* asyncandawaitsyntax
* How to execute an async program withasyncio
* How to run concurrent coroutines
* How to createasynciotasks
* How to use therandommodule

## Requirements
### General
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* Allowed editors:vi,vim,emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS usingpython3(version 3.9)
* All your files should end with a new line
* All your files must be executable
* The length of your files will be tested usingwc
* The first line of all your files should be exactly#!/usr/bin/env python3
* Your code should use thepycodestylestyle (version 2.5.x)
* All your functions and coroutines must be type-annotated.
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Task
### 0. The basics of async <a name='subparagraph0'></a>

Write an asynchronous coroutine that takes in an integer argument (<code>max_delay</code>, with a default value of 10) named <code>wait_random</code> that waits for a random delay between 0 and <code>max_delay</code> (included and float value) seconds and eventually returns it.

Use the <code>random</code> module.

```
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))

bob@dylan:~$ ./0-main.py
9.034261504534394
1.6216525464615306
10.634589756751769
```

---

### 1. Let's execute multiple coroutines at the same time with async <a name='subparagraph1'></a>

Import <code>wait_random</code> from the previous python file that you’ve written and write an async routine called <code>wait_n</code> that takes in 2 int arguments (in this order): <code>n</code> and <code>max_delay</code>. You will spawn <code>wait_random</code> <code>n</code> times with the specified <code>max_delay</code>.

<code>wait_n</code> should return the list of all the delays (float values). The list of the delays should be in ascending order without using <code>sort()</code> because of concurrency.

```
bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))

bob@dylan:~$ ./1-main.py
[0.9693881173832269, 1.0264573845731002, 1.7992690129519855, 3.641373003434587, 4.500011569340617]
[0.07256214141415429, 1.518551245602588, 3.355762808432721, 3.7032593997182923, 3.7796178143655546, 4.744537840582318, 5.50781365463315, 5.758942587637626, 6.109707751654879, 6.831351588271327]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
```

The output for your answers might look a little different and that’s okay.

---

### 2. Measure the runtime <a name='subparagraph2'></a>

From the previous file, import <code>wait_n</code> into <code>2-measure_runtime.py</code>.

Create a <code>measure_time</code> function with integers <code>n</code> and <code>max_delay</code> as arguments that measures the total execution time for <code>wait_n(n, max_delay)</code>, and returns <code>total_time / n</code>.  Your function should return a float.

Use the <code>time</code> module to measure an approximate elapsed time.

```
bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))

bob@dylan:~$ ./2-main.py
1.759705400466919
```

---

### 3. Tasks <a name='subparagraph3'></a>

Import <code>wait_random</code> from <code>0-basic_async_syntax</code>.

Write a function (do not create an async function, use the regular function syntax to do this) <code>task_wait_random</code> that takes an integer <code>max_delay</code> and returns a <code>asyncio.Task</code>.

```
bob@dylan:~$ cat 3-main.py
#!/usr/bin/env python3

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))

bob@dylan:~$ ./3-main.py
<class '_asyncio.Task'>
```

---

### 4. Tasks <a name='subparagraph4'></a>

Take the code from <code>wait_n</code> and alter it into a new function <code>task_wait_n</code>.  The code is nearly identical to <code>wait_n</code> except <code>task_wait_random</code> is being called.

```
bob@dylan:~$ cat 4-main.py
#!/usr/bin/env python3

import asyncio

task_wait_n = __import__('4-tasks').task_wait_n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))

bob@dylan:~$ ./4-main.py
[0.2261658205652346, 1.1942770588220557, 1.8410422186086628, 2.1457353803430523, 4.002505454641153]
```

---


## Authors
vtiquet - [GitHub Profile](https://github.com/vtiquet)
