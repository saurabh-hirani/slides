### Monkey patching demo


#### Socket module without monkey patching

```text
$ python

import inspect
import socket

print(socket.socket)

inspect.getsourcefile(socket.ssl)

exit()
```

#### Socket module with monkey patching

```text
$ python

from gevent import monkey
monkey.patch_all()
import inspect
import socket

print(socket.socket)

inspect.getsourcefile(socket.ssl)

exit()
```

#### Bring your own monkey

```text
cd monkey_patching_demo
```

```text
cat blocking_socket.py
```

```python

def socket():
  print("I will block")

```

```text
cat non_blocking_socket.py
```

```python

def socket():
  print("I will not block")

```

```text
cat call_blocking_socket.py
```

```python

import blocking_socket
blocking_socket.socket()

```

```text
python call_blocking_socket.py
```

```text
I will block
```

```text
cat patch_and_call_blocking_socket.py
```

```python

import patcher
patcher.patch_all()

import blocking_socket
blocking_socket.socket()

```

```text
python patch_and_call_blocking_socket.py
```

```text
I will not block
```

```text
cat patcher.py
```

```python

def patch_all():
  import blocking_socket
  import non_blocking_socket
  blocking_socket.socket = non_blocking_socket.socket

```
