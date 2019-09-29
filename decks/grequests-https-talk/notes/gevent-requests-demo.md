### gevent-requests-demo


1. Import and **monkey patch**.

```python
import gevent.monkey
gevent.monkey.patch_all()
```

2. Write ```fetch``` function which will be called synchronously and asynchronously.

```python
import gevent
import requests

def fetch(i):
    url = 'http://localhost:8081/delay/1'
    response = requests.get(url, params={'page': i}, verify=False)
    result = response.json()
    print("{}: {}".format(i, response.status_code))
    return result
```

3. Write synchronous version

```python
def synchronous():
    for i in range(1, 6):
        fetch(i)
```

4. Write asynchronous version - **greenlet and event loop**

```python
def asynchronous():
    threads = []
    for i in range(1, 6):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)
```

5. Call both to verify

```python
print("synchronous: start")
start_time = int(time.time())
synchronous()
print("synchronous: end")
end_time = int(time.time())
print("synchronous: time = {} seconds".format(end_time - start_time))

print("==============")
print("asynchronous: start")
start_time = int(time.time())
asynchronous()
end_time = int(time.time())
print("asynchronous: end")
print("asynchronous: time = {} seconds".format(end_time - start_time))
```

6. Run the program.

```
python3 gevent-requests.py

synchronous: start
1: 200
2: 200
3: 200
4: 200
5: 200
synchronous: end
synchronous: time = 5 seconds
==============
asynchronous: start
1: 200
4: 200
3: 200
2: 200
5: 200
asynchronous: end
asynchronous: time = 1 seconds
```
