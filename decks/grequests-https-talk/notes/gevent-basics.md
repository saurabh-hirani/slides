### gevent in-depth

- Sources:
  - [GeeksforGeeks coroutine post](https://www.geeksforgeeks.org/coroutine-in-python/)
  - [Stephen Diehl's awesome tutorial](https://sdiehl.github.io/gevent-tutorial/)
  - [gevent site](http://www.gevent.org/)
  - [Kavya Joshi's excellent Gevent talk](https://www.youtube.com/watch?v=GunMToxbE0E)
  - [learn-gevent-socketio](https://learn-gevent-socketio.readthedocs.io/en/latest/general_concepts.html)

- The bare minimum we need to know:

  - Import gevent.
  - Make gevent library calls to spawn multiple functions.
  - Yield control to something when blocked on I/O.
  - That something decides which function to wake up next.
  - Run, yield control, run, till the job is done.

- Stephen Diehl's gevent visualization:

![Stephen Diehl's gevent visualization](https://sdiehl.github.io/gevent-tutorial/flow.gif)

```
Running in foo
Explicit context to bar
Explicit context switch to foo again
Implicit context switch back to bar
```

- Citing from the sources:
  - gevent is a **coroutine**-based Python networking library that uses **greenlet** to provide a
    high-level synchronous API on top of the **libev or libuv event loop**.
  - Gevent has a **Monkey patching** utility.
  - **gevent.monkey** - The functions in this module patch parts of the standard library with compatible cooperative counterparts
    from gevent package.
  - libevent - Written in C, this library provides **asynchronous event notification**. The libevent API
    provides a mechanism to execute a **callback function** when a specific event occurs on a file descriptor
    or after a timeout has been reached.
  - Greenlet - a lightweight **coroutine** provided to Python as a C extension module. Greenlets all
    run inside of the OS process for the main program but are **scheduled cooperatively**.
  - Coroutines are generalization of subroutines. They are used for cooperative multitasking where a process
    voluntarily **yield** (give away) control periodically or when idle in order to enable multiple applications
    to be run simultaneously.
