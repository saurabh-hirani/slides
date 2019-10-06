### Trace Python2.7 code

```
STAGE=0 PYVERSIONS=27 PROTO=https COUNT=3 TRACE=1 ./bin/run-stages.sh 2>&1 > stages/00/python27-trace.txt
less stages/00/python2.7-trace.txt

# /usr/local/lib/python2.7/site-packages/OpenSSL/SSL.py:1713:send
# /usr/local/lib/python2.7/site-packages/OpenSSL/SSL.py:1777:recv
# /usr/local/lib/python2.7/site-packages/urllib3/util/wait.py:136:wait_for_socket
```
