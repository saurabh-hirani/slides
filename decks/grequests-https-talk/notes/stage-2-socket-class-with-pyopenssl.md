### Stage-2 socket class with pyopenssl

```text
STAGE=2 PYVERSIONS=37 PROTO=https COUNT=3 SOCKET_CLASS=1 ./bin/run-stages.sh | grep socket_class
```

#### Sample output

```text
STAGE=2 PYVERSIONS=37 PROTO=https COUNT=3 SOCKET_CLASS=1 ./bin/run-stages.sh | grep socket_class
```

```text
2019-10-07 10:24:39,027  - python37_2 - test_grequests_v1.py:main:168 - WARNING - socket_class = <class 'urllib3.contrib.pyopenssl.WrappedSocket'>
```
