### Monkey patching demo

```
$ python

import inspect
import socket

print(socket.socket)

inspect.getsourcefile(socket.ssl)

exit()
```

```
$ python

from gevent import monkey
monkey.patch_all()
import inspect
import socket

print(socket.socket)

inspect.getsourcefile(socket.ssl)

exit()
```

```
$ cd monkey_patching_demo

$ cat blocking_socket.py

$ cat non_blocking_socket.py

$ cat call_blocking_socket.py

$ python call_blocking_socket.py

I will block

$ cat patch_and_call_blocking_socket.py

$ python patch_and_call_blocking_socket.py

I won't block

$ cat patcher.py
```
