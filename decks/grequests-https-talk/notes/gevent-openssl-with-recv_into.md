### gevent-openssl with recv_into

```shell
./docker-exec.sh test_grequests_python37_4 /usr/local/bin/python
```

```python
import gevent_openssl
import inspect
import json
print(json.dumps([x[0] for x in inspect.getmembers(gevent_openssl.SSL.Connection)], indent=2, default=str))
```

```python
[
  "_Connection__iowait",
  "_Connection__send",
  "__class__",
  "__delattr__",
  "__dict__",
  "__dir__",
  "__doc__",
  "__eq__",
  "__format__",
  "__ge__",
  "__getattr__",
  "__getattribute__",
  "__gt__",
  "__hash__",
  "__init__",
  "__init_subclass__",
  "__le__",
  "__lt__",
  "__module__",
  "__ne__",
  "__new__",
  "__reduce__",
  "__reduce_ex__",
  "__repr__",
  "__setattr__",
  "__sizeof__",
  "__str__",
  "__subclasshook__",
  "__weakref__",
  "_reverse_mapping",
  "accept",
  "connect",
  "do_handshake",

  "recv",
  "recv_into",

  "send",
  "sendall",
  "shutdown"
]
```
