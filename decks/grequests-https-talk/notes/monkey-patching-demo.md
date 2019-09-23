### Monkey patching demo

```
python

import inspect
import socket

print(socket.socket) # should output <class 'socket._socketobject'>
inspect.getsourcefile(socket.ssl) # should output '/usr/local/Cellar/python@2/2.7.15_3/Frameworks/Python.framework/Versions/2.7/lib/python2.7/socket.py'

exit()

python

from gevent import monkey
monkey.patch_all()
import inspect
import socket

print(socket.socket) # should output <class 'gevent._socket2.socket'>
inspect.getsourcefile(socket.ssl) # should output '/usr/local/lib/python2.7/site-packages/gevent/_socket2.py'

exit()

vim '/usr/local/lib/python2.7/site-packages/gevent/_socket2.py'
# grep wait

python

import gevent._hub_primitives
gevent._hub_primitives.__file__ # should output /usr/local/lib/python2.7/site-packages/gevent/__hub_primitives.so
```

```
cd monkey_patching_demo
cat mysocket.py
cat patched_socket.py
cat call_mysocket.py
python call_mysocket.py
cat patch_and_call_mysocket.py
python patch_and_call_mysocket.py
cat patcher.py
```
