### Stage-1 socket class without pyopenssl

```text
STAGE=1 PYVERSIONS=37 PROTO=https COUNT=3 SOCKET_CLASS=1 ./bin/run-stages.sh | grep socket_class
```

#### Sample output

```text
STAGE=1 PYVERSIONS=37 PROTO=https COUNT=3 SOCKET_CLASS=1 ./bin/run-stages.sh | grep socket_class
```

```text
2019-10-07 10:26:12,522  - python37_1 - test_grequests_v1.py:main:168 - WARNING - socket_class = <class 'gevent._ssl3.SSLSocket'>
```
