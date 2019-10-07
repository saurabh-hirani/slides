### Test grequests

```shell
python2 ./bin/test-grequests.py https 3
python3 ./bin/test-grequests.py https 3
```



#### Sample output

```shell
python2 ./bin/test-grequests.py https 3
```

```text
2019-10-07 17:26:26,047 test-grequests.py:<module>:34 - INFO - START
2019-10-07 17:26:26,070 connectionpool.py:_new_conn:818 - DEBUG - Starting new HTTPS connection (1): localhost:8082
2019-10-07 17:26:26,071 connectionpool.py:_new_conn:818 - DEBUG - Starting new HTTPS connection (1): localhost:8082
2019-10-07 17:26:26,072 connectionpool.py:_new_conn:818 - DEBUG - Starting new HTTPS connection (1): localhost:8082
2019-10-07 17:26:27,079 connectionpool.py:_make_request:398 - DEBUG - https://localhost:8082 "GET /delay/1?page=1 HTTP/1.1" 200 302
2019-10-07 17:26:28,087 connectionpool.py:_make_request:398 - DEBUG - https://localhost:8082 "GET /delay/1?page=0 HTTP/1.1" 200 302
2019-10-07 17:26:29,100 connectionpool.py:_make_request:398 - DEBUG - https://localhost:8082 "GET /delay/1?page=2 HTTP/1.1" 200 302
2019-10-07 17:26:29,101 test-grequests.py:<module>:38 - INFO - END
2019-10-07 17:26:29,101 test-grequests.py:<module>:41 - INFO - total_time = 3.053 seconds
```

```shell
python3 ./bin/test-grequests.py https 3
```

```text
2019-10-07 17:27:25,407 test-grequests.py:<module>:34 - INFO - START
2019-10-07 17:27:25,425 connectionpool.py:_new_conn:820 - DEBUG - Starting new HTTPS connection (1): localhost:8082
2019-10-07 17:27:25,426 connectionpool.py:_new_conn:820 - DEBUG - Starting new HTTPS connection (1): localhost:8082
2019-10-07 17:27:25,427 connectionpool.py:_new_conn:820 - DEBUG - Starting new HTTPS connection (1): localhost:8082
2019-10-07 17:27:26,459 connectionpool.py:_make_request:400 - DEBUG - https://localhost:8082 "GET /delay/1?page=0 HTTP/1.1" 200 302
2019-10-07 17:27:26,464 connectionpool.py:_make_request:400 - DEBUG - https://localhost:8082 "GET /delay/1?page=2 HTTP/1.1" 200 302
2019-10-07 17:27:26,465 connectionpool.py:_make_request:400 - DEBUG - https://localhost:8082 "GET /delay/1?page=1 HTTP/1.1" 200 302
2019-10-07 17:27:26,470 test-grequests.py:<module>:38 - INFO - END
2019-10-07 17:27:26,470 test-grequests.py:<module>:41 - INFO - total_time = 1.063 seconds
```


