### Monkey patching demo

```
$ python

>>> import inspect
>>> import socket

>>> print(socket.socket)
<class 'socket._socketobject'>

>>> inspect.getsourcefile(socket.ssl)
'/usr/local/Cellar/python@2/2.7.15_3/Frameworks/Python.framework/Versions/2.7/lib/python2.7/socket.py'

>>> exit()
```

```
$ python

>>> from gevent import monkey
>>> monkey.patch_all()
>>> import inspect
>>> import socket

>>> print(socket.socket)
<class 'gevent._socket2.socket'>

>>> inspect.getsourcefile(socket.ssl)
'/usr/local/lib/python2.7/site-packages/gevent/_socket2.py'

>>> exit()
```

```
$ cd monkey_patching_demo

$ cat mysocket.py

def f1():
  print("f1")

$ cat patched_socket.py

def f1():
  print("patched f1")

$ cat call_mysocket.py

import mysocket
mysocket.f1()

$ python call_mysocket.py

f1

$ cat patch_and_call_mysocket.py

import patcher
patcher.patch_all()

import mysocket
mysocket.f1()

$ python patch_and_call_mysocket.py

patched f1

$ cat patcher.py

def patch_all():
  import mysocket
  import patched_socket
  mysocket.f1 = patched_socket.f1
```
