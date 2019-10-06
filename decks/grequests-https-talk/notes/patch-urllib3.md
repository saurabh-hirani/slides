### Patch urllib3

```shell
2019-10-06 20:09:04,530 ./bin/test-gevent_requests.py:<module>:92 - INFO - START
2019-10-06 20:09:04,558 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:_new_conn:816 - DEBUG - Starting new HTTPS connection (1): localhost:8082
2019-10-06 20:09:04,559 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:_new_conn:816 - DEBUG - Starting new HTTPS connection (1): localhost:8082
2019-10-06 20:09:04,560 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:_new_conn:816 - DEBUG - Starting new HTTPS connection (1): localhost:8082
2019-10-06 20:09:05,575 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:_make_request:396 - DEBUG - https://localhost:8082 "GET /delay/1?page=0 HTTP/1.1" 200 302
2019-10-06 20:09:05,577 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:_make_request:396 - DEBUG - https://localhost:8082 "GET /delay/1?page=1 HTTP/1.1" 200 302
2019-10-06 20:09:05,579 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:_make_request:396 - DEBUG - https://localhost:8082 "GET /delay/1?page=2 HTTP/1.1" 200 302
2019-10-06 20:09:05,580 ./bin/test-gevent_requests.py:<module>:97 - INFO - END
```

```shell
vim /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py
# Find where request is being sent
# Add debugging statement
```
