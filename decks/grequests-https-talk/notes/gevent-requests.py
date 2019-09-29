import gevent.monkey
gevent.monkey.patch_all()

import gevent
import requests
import time

def fetch(i):
    url = 'http://localhost:8081/delay/1'
    response = requests.get(url, params={'page': i}, verify=False)
    result = response.json()
    print("{}: {}".format(i, response.status_code))
    return result


def synchronous():
    for i in range(1, 6):
        fetch(i)


def asynchronous():
    threads = []
    for i in range(1, 6):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)


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
