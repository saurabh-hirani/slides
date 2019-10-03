### Stage-1 Python2.7 tracing

```shell
./docker-exec.sh test_grequests_python27_1 \
 /usr/local/bin/python /app/test_grequests_v1.py \
--log-level DEBUG \
 --url https://https_server:8081/delay/1 --url-count 5 \
 --trace

less stages/01/python27/trace.txt

# /usr/local/lib/python2.7/site-packages/gevent/_sslgte279.py:396:send
# /usr/local/lib/python2.7/site-packages/gevent/_sslgte279.py:448:recv
```
