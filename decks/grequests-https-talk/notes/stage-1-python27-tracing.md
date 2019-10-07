### Stage-1 Python2.7 tracing

```
STAGE=1 PYVERSIONS=27 PROTO=https COUNT=3 TRACE=1 ./bin/run-stages.sh > stages/01/python27-trace.txt

less stages/01/python27/trace.txt

# /usr/local/lib/python2.7/site-packages/gevent/_sslgte279.py:396:send
# /usr/local/lib/python2.7/site-packages/gevent/_sslgte279.py:448:recv
```
