## README.md: Introduction to Asynchronous Programming in Python

### Class Objective
The goal of this class is to introduce students to the fundamentals of asynchronous programming in Python, highlighting the differences and advantages over traditional synchronous programming. Practical examples will be provided to demonstrate how to implement asynchronous code and the concepts of `asyncio`, a Python library for writing concurrent code using the `async`/`await` syntax.

### What is Asynchronous Programming?
Asynchronous programming is a programming model that allows long-running operations (such as I/O) to run in the "background", allowing the main program to continue its execution without being blocked. This is achieved through the use of coroutines, which are functions that can pause their execution and resume at a later point.

### Advantages of Asynchronous Programming
* **Better resource utilization:** By not blocking the main thread, multiple I/O operations can be performed simultaneously, improving efficiency and performance.
* **Improved user experience:** In graphical user interface (GUI) applications or web services, it keeps the application responsive, even during long-running operations.
* **Scalability:** Facilitates handling large volumes of connections or network requests.

### Key Differences from Synchronous Programming
* **Flow of execution:** In synchronous programming, code executes sequentially. In contrast, in asynchronous programming, the flow can be paused and resumed, allowing other operations to execute.
* **I/O handling:** Asynchronous programming is especially useful for I/O operations, where the wait time to complete the operation is significant.

### Synchronous vs. Asynchronous Code Example
Now, let's move on to code examples to illustrate these concepts.

#### Synchronous Example: File Download
First, let's see how a script would look like to download files synchronously, which means each download must complete before starting the next one.

```python
import requests
import time

def descargar_archivo(url):
  respuesta = requests.get(url)
  nombre_archivo = url.split('/')[-1]
  with open(nombre_archivo, 'wb') as f:
    f.write(respuesta.content)
  print(f'Descargado {nombre_archivo}')

def main():
  urls = [
    'http://example.com/archivo1',
    'http://example.com/archivo2',
    'http://example.com/archivo3',
  ]
   
  inicio = time.time()
  for url in urls:
    descargar_archivo(url)
  duracion = time.time() - inicio
  print(f'Tiempo total de descarga: {duracion} segundos')

if __name__ == '__main__':
  main()
```

#### Asynchronous Example: File Download
Now, we refactor the code to use `asyncio`, which allows downloads to be performed concurrently.

```python
import asyncio
import aiohttp
import time

async def descargar_archivo(session, url):
  async with session.get(url) as respuesta:
    nombre_archivo = url.split('/')[-1]
    with open(nombre_archivo, 'wb') as f:
      while True:
        chunk = await respuesta.content.read(1024)
        if not chunk:
          break
        f.write(chunk)
    print(f'Descargado {nombre_archivo}')

async def main():
  urls = [
    'http://example.com/archivo1',
    'http://example.com/archivo2',
    'http://example.com/archivo3',
  ]
   
  async with aiohttp.ClientSession() as session:
    tareas = [descargar_archivo(session, url) for url in urls]
    inicio = time.time()
    await asyncio.gather(*tareas)
    duracion = time.time() - inicio
    print(f'Tiempo total de descarga: {duracion} segundos')

if __name__ == '__main__':
  asyncio.run(main())
```

### Conclusion
These examples demonstrate how the asynchronous programming model can significantly improve efficiency by performing multiple I/O operations simultaneously, compared to the traditional synchronous approach. In the next class, we will explore coroutines, task scheduling, and exception handling in an asynchronous environment in more depth.

---

This README provides an overview and basic code examples to introduce asynchronous programming. The code examples are simplified for ease of understanding and should be adapted for more complex and practical uses.