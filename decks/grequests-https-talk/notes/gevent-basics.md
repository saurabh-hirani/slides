### gevent basics

- requests code:

    ```python
    for i in range(url_count):
        requests.get(url, params={'page': i}, verify=False)
    ```

- grequests code:

    ```python
    pending_requests = []
    for i in range(url_count):
        pending_requests.append(grequests.get(
            url, params={'page': i}, verify=False))

    all_responses = grequests.map(pending_requests)
    ```

- [gevent + requests](https://github.com/gevent/gevent/blob/master/examples/concurrent_download.py):

    ```python
    import gevent
    from gevent import monkey

    # patches stdlib (including socket and ssl modules) to cooperate with other greenlets
    monkey.patch_all()

    import requests

    # Note that we're using HTTPS, so
    # this demonstrates that SSL works.
    urls = [
        'https://www.google.com/',
        'https://www.apple.com/',
        'https://www.python.org/'
    ]

    def print_head(url):
        print('Starting %s' % url)
        data = requests.get(url).text
        print('%s: %s bytes: %r' % (url, len(data), data[:50]))

    jobs = [gevent.spawn(print_head, _url) for _url in urls]

    gevent.wait(jobs)
    ```

- Stephen Diehl's gevent visualization:

<p align="center">
    <img src="https://sdiehl.github.io/gevent-tutorial/flow.gif"></img>
    <pre>
    Running in foo
    Explicit context to bar
    Explicit context switch to foo again
    Implicit context switch back to bar
    </pre>
</p>


- The bare minimum we need to know:

  - Import gevent.
  - Make gevent library calls to spawn multiple functions.
  - Yield control to something when blocked on I/O.
  - That something decides which function to wake up next.
  - Run, yield control, run, till the job is done.

- Sources:
  - [GeeksforGeeks coroutine post](https://www.geeksforgeeks.org/coroutine-in-python/)
  - [Stephen Diehl's awesome tutorial](https://sdiehl.github.io/gevent-tutorial/)
  - [gevent site](http://www.gevent.org/)
  - [Kavya Joshi's excellent Gevent talk](https://www.youtube.com/watch?v=GunMToxbE0E)
  - [learn-gevent-socketio](https://learn-gevent-socketio.readthedocs.io/en/latest/general_concepts.html)

- Citing from the sources:
  - gevent is a **coroutine**-based Python networking library that uses **greenlet** to provide a
    high-level synchronous API on top of the **libev or libuv event loop**.
  - As per [gevent api](http://www.gevent.org/api/gevent.html) **spawn** creates a new **greenlet** object and schedule it
     to run ```function(*args, **kwargs)```. This can be used as gevent.spawn or Greenlet.spawn.
  - libevent - Written in C, this library provides **asynchronous event notification**. The libevent API
    provides a mechanism to execute a **callback function** when a specific event occurs on a file descriptor
    or after a timeout has been reached.
  - Greenlet - a lightweight **coroutine** provided to Python as a C extension module. Greenlets all
    run inside of the OS process for the main program but are **scheduled cooperatively**.
  - Coroutines are generalization of subroutines. They are used for cooperative multitasking where a process
    voluntarily **yield** (give away) control periodically or when idle in order to enable multiple applications
    to be run simultaneously.
  - Gevent has a **Monkey patching** utility.
  - **gevent.monkey** - The functions in this module **patch** parts of the standard library with compatible cooperative counterparts
    from gevent package.
