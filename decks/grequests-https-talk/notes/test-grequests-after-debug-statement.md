### Test grequests after debug statement

```shell
python2 ./bin/test-grequests.py https 3
python3 ./bin/test-grequests.py https 3
```


#### Sample output

```shell
python2 ./bin/test-grequests.py https 3
```

```text
2019-10-07 17:33:13,488 test-grequests.py:<module>:34 - INFO - START
2019-10-07 17:33:13,508 connectionpool.py:_new_conn:818 - DEBUG - Starting new HTTPS connection (1): localhost:8082
2019-10-07 17:33:13,509 connectionpool.py:_new_conn:818 - DEBUG - Starting new HTTPS connection (1): localhost:8082
2019-10-07 17:33:13,510 connectionpool.py:_new_conn:818 - DEBUG - Starting new HTTPS connection (1): localhost:8082
2019-10-07 17:33:13,517 connectionpool.py:_make_request:355 - DEBUG -
2019-10-07 17:33:13,517 connectionpool.py:_make_request:356 - DEBUG - sending_request
2019-10-07 17:33:13,517 connectionpool.py:_make_request:357 - DEBUG -
2019-10-07 17:33:14,518 connectionpool.py:_make_request:398 - DEBUG - https://localhost:8082 "GET /delay/1?page=0 HTTP/1.1" 200 302
2019-10-07 17:33:14,524 connectionpool.py:_make_request:355 - DEBUG -
2019-10-07 17:33:14,524 connectionpool.py:_make_request:356 - DEBUG - sending_request
2019-10-07 17:33:14,524 connectionpool.py:_make_request:357 - DEBUG -
2019-10-07 17:33:15,528 connectionpool.py:_make_request:398 - DEBUG - https://localhost:8082 "GET /delay/1?page=1 HTTP/1.1" 200 302
2019-10-07 17:33:15,537 connectionpool.py:_make_request:355 - DEBUG -
2019-10-07 17:33:15,537 connectionpool.py:_make_request:356 - DEBUG - sending_request
2019-10-07 17:33:15,537 connectionpool.py:_make_request:357 - DEBUG -
2019-10-07 17:33:16,540 connectionpool.py:_make_request:398 - DEBUG - https://localhost:8082 "GET /delay/1?page=2 HTTP/1.1" 200 302
2019-10-07 17:33:16,541 test-grequests.py:<module>:38 - INFO - END
2019-10-07 17:33:16,541 test-grequests.py:<module>:41 - INFO - total_time = 3.053 seconds
```

```shell
python3 ./bin/test-grequests.py https 3
```

```text
2019-10-07 17:35:54,857 test-grequests.py:<module>:34 - INFO - START
2019-10-07 17:35:54,876 connectionpool.py:_new_conn:820 - DEBUG - Starting new HTTPS connection (1): localhost:8082
2019-10-07 17:35:54,877 connectionpool.py:_new_conn:820 - DEBUG - Starting new HTTPS connection (1): localhost:8082
2019-10-07 17:35:54,878 connectionpool.py:_new_conn:820 - DEBUG - Starting new HTTPS connection (1): localhost:8082
2019-10-07 17:35:54,907 connectionpool.py:_make_request:357 - WARNING -
2019-10-07 17:35:54,907 connectionpool.py:_make_request:358 - WARNING - sending_request
2019-10-07 17:35:54,907 connectionpool.py:_make_request:359 - WARNING -
2019-10-07 17:35:54,909 connectionpool.py:_make_request:357 - WARNING -
2019-10-07 17:35:54,909 connectionpool.py:_make_request:358 - WARNING - sending_request
2019-10-07 17:35:54,909 connectionpool.py:_make_request:359 - WARNING -
2019-10-07 17:35:54,911 connectionpool.py:_make_request:357 - WARNING -
2019-10-07 17:35:54,911 connectionpool.py:_make_request:358 - WARNING - sending_request
2019-10-07 17:35:54,911 connectionpool.py:_make_request:359 - WARNING -
2019-10-07 17:35:55,912 connectionpool.py:_make_request:400 - DEBUG - https://localhost:8082 "GET /delay/1?page=0 HTTP/1.1" 200 302
2019-10-07 17:35:55,913 connectionpool.py:_make_request:400 - DEBUG - https://localhost:8082 "GET /delay/1?page=1 HTTP/1.1" 200 302
2019-10-07 17:35:55,914 connectionpool.py:_make_request:400 - DEBUG - https://localhost:8082 "GET /delay/1?page=2 HTTP/1.1" 200 302
2019-10-07 17:35:55,919 test-grequests.py:<module>:38 - INFO - END
2019-10-07 17:35:55,919 test-grequests.py:<module>:41 - INFO - total_time = 1.062 seconds
```
