<div align="center"><img src="https://github.com/vtiquet/holbertonschool-resources/blob/main/image/Holberton-Logo.svg" width=40% height=40%/></div>

# Resources

## Table of Contents :

  - [0. Async Generator](#subparagraph0)
  - [1. Async Comprehensions](#subparagraph1)
  - [2. Run time for four parallel comprehensions](#subparagraph2)

## Resources
### Read or watch:
* [PEP 530 – Asynchronous Comprehensions](/rltoken/UFCR8qW3nHmEDZZaHqXL7Q)
* [What’s New in Python: Asynchronous Comprehensions / Generators](/rltoken/PAGwxZUyVGBR8EMFGGNnGg)
* [Type-hints for generators](/rltoken/fOrb8FrWbcYu8evONWj2Kw)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* How to write an asynchronous generator
* How to use async comprehensions
* How to type-annotate generators

## Requirements
### General
* Allowed editors:vi,vim,emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS usingpython3(version 3.9)
* All your files should end with a new line
* The first line of all your files should be exactly#!/usr/bin/env python3
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* Your code should use thepycodestylestyle (version 2.5.x)
* The length of your files will be tested usingwc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* All your functions and coroutines must be type-annotated.

## Task
### 0. Async Generator <a name='subparagraph0'></a>

Write a coroutine called <code>async_generator</code> that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the <code>random</code> module.

```
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())

bob@dylan:~$ ./0-main.py
[4.403136952967102, 6.9092712604587465, 6.293445466782645, 4.549663490048418, 4.1326571686139015, 9.99058525304903, 6.726734105473811, 9.84331704602206, 1.0067279479988345, 1.3783306401737838]
```

---

### 1. Async Comprehensions <a name='subparagraph1'></a>

Import <code>async_generator</code> from the previous task and then write a coroutine called <code>async_comprehension</code> that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehensing over <code>async_generator</code>, then return the 10 random numbers.

```
bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def main():
    print(await async_comprehension())

asyncio.run(main())

bob@dylan:~$ ./1-main.py
[9.861842105071727, 8.572355293354995, 1.7467182056248265, 4.0724372912858575, 0.5524750922145316, 8.084266576021555, 8.387128918690468, 1.5486451376520916, 7.713335177885325, 7.673533267041574]
```

---

### 2. Run time for four parallel comprehensions <a name='subparagraph2'></a>

Import <code>async_comprehension</code> from the previous file and write a <code>measure_runtime</code> coroutine that will execute <code>async_comprehension</code> four times in parallel using <code>asyncio.gather</code>.

<code>measure_runtime</code> should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.

```
bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

import asyncio


measure_runtime = __import__('2-measure_runtime').measure_runtime


async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)

bob@dylan:~$ ./2-main.py
10.021936893463135
```

---


## Authors
vtiquet - [GitHub Profile](https://github.com/vtiquet)
