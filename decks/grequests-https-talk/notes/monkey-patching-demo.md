### Monkey patching demo

```
python

import inspect
import socket

print(socket.socket)
inspect.getsourcefile(socket.ssl)

exit()

python

from gevent import monkey
monkey.patch_all()
import inspect
import socket

print(socket.socket)
inspect.getsourcefile(socket.ssl)

exit()
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
