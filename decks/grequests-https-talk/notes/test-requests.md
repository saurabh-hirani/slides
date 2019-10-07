### Test requests

#### Commands

```shell
cat test-requests.py
python2 ./bin/test-requests.py https 3
python3 ./bin/test-requests.py https 3
```



#### Sample output

```shell
python2 ./bin/test-requests.py https 3
```

```text
2019-10-07 17:03:57,671 test-requests.py:<module>:32 - INFO - START
2019-10-07 17:03:57,679 connectionpool.py:_new_conn:818 - DEBUG - Starting new HTTPS connection (1): localhost:8082
2019-10-07 17:03:58,692 connectionpool.py:_make_request:398 - DEBUG - https://localhost:8082 "GET /delay/1?page=0 HTTP/1.1" 200 302
2019-10-07 17:03:58,695 connectionpool.py:_new_conn:818 - DEBUG - Starting new HTTPS connection (1): localhost:8082
2019-10-07 17:03:59,707 connectionpool.py:_make_request:398 - DEBUG - https://localhost:8082 "GET /delay/1?page=1 HTTP/1.1" 200 302
2019-10-07 17:03:59,710 connectionpool.py:_new_conn:818 - DEBUG - Starting new HTTPS connection (1): localhost:8082
2019-10-07 17:04:00,720 connectionpool.py:_make_request:398 - DEBUG - https://localhost:8082 "GET /delay/1?page=2 HTTP/1.1" 200 302
2019-10-07 17:04:00,721 test-requests.py:<module>:36 - INFO - END
2019-10-07 17:04:00,721 test-requests.py:<module>:39 - INFO - total_time = 3.05 seconds
```

```shell
python3 ./bin/test-requests.py https 3
```

```text
2019-10-07 17:06:15,275 test-requests.py:<module>:32 - INFO - START
2019-10-07 17:06:15,294 connectionpool.py:_new_conn:820 - DEBUG - Starting new HTTPS connection (1): localhost:8082
2019-10-07 17:06:16,326 connectionpool.py:_make_request:400 - DEBUG - https://localhost:8082 "GET /delay/1?page=0 HTTP/1.1" 200 302
2019-10-07 17:06:16,334 connectionpool.py:_new_conn:820 - DEBUG - Starting new HTTPS connection (1): localhost:8082
2019-10-07 17:06:17,356 connectionpool.py:_make_request:400 - DEBUG - https://localhost:8082 "GET /delay/1?page=1 HTTP/1.1" 200 302
2019-10-07 17:06:17,361 connectionpool.py:_new_conn:820 - DEBUG - Starting new HTTPS connection (1): localhost:8082
2019-10-07 17:06:18,378 connectionpool.py:_make_request:400 - DEBUG - https://localhost:8082 "GET /delay/1?page=2 HTTP/1.1" 200 302
2019-10-07 17:06:18,382 test-requests.py:<module>:36 - INFO - END
2019-10-07 17:06:18,382 test-requests.py:<module>:39 - INFO - total_time = 3.105 seconds
```
