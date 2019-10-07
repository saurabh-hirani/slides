### Python3.7 uses recv_into

```text
STAGE=3 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```

#### Sample output

```text
STAGE=3 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```

```text
=============
test_grequests_python37_3: installed_modules: urllib3==1.24.1 requests==2.21.0 gevent==1.4.0 grequests==0.3.0 pyopenssl==19.0.0 gevent-openssl==1.2
2019-10-07 18:12:52,019  - python37_3 - test_grequests_v2.py:main:165 - INFO - START
2019-10-07 18:12:52,071  - python37_3 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 18:12:52,152  - python37_3 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 18:12:52,181  - python37_3 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 18:12:53,239  - python37_3 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 308
2019-10-07 18:12:54,261  - python37_3 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 308
2019-10-07 18:12:55,283  - python37_3 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 308
2019-10-07 18:12:55,293  - python37_3 - test_grequests_v2.py:make_requests:128 - INFO - len(all_page_ids) = 3
2019-10-07 18:12:55,293  - python37_3 - test_grequests_v2.py:make_requests:129 - INFO - len(valid_page_ids) = 3
2019-10-07 18:12:55,293  - python37_3 - test_grequests_v2.py:make_requests:130 - INFO - len(invalid_page_ids) = 0
         11223 function calls (11080 primitive calls) in 3.272 seconds

   Ordered by: cumulative time
   List reduced from 750 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.273    3.273 /usr/local/lib/python3.7/site-packages/grequests.py:103(map)
      3/1    0.000    0.000    3.272    3.272 /usr/local/lib/python3.7/site-packages/grequests.py:60(send)
      3/1    0.000    0.000    3.272    3.272 /usr/local/lib/python3.7/site-packages/requests/sessions.py:466(request)
      3/1    0.001    0.000    3.232    3.232 /usr/local/lib/python3.7/site-packages/requests/sessions.py:617(send)
      3/1    0.000    0.000    3.229    3.229 /usr/local/lib/python3.7/site-packages/requests/adapters.py:394(send)
      3/1    0.000    0.000    3.216    3.216 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:446(urlopen)
      3/1    0.001    0.000    3.211    3.211 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:319(_make_request)
        3    0.000    0.000    3.026    1.009 /usr/local/lib/python3.7/http/client.py:1277(getresponse)
        3    0.000    0.000    3.025    1.008 /usr/local/lib/python3.7/http/client.py:289(begin)
        3    0.000    0.000    3.009    1.003 /usr/local/lib/python3.7/http/client.py:256(_read_status)
       21    0.000    0.000    3.009    0.143 {method 'readline' of '_io.BufferedReader' objects}
        3    0.000    0.000    3.008    1.003 /usr/local/lib/python3.7/socket.py:575(readinto)

      6/3    0.001    0.000    3.008    1.003 /usr/local/lib/python3.7/site-packages/urllib3/contrib/pyopenssl.py:292(recv_into)

        3    0.000    0.000    3.006    1.002 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:139(wait_for_read)
        3    0.000    0.000    3.005    1.002 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:87(poll_wait_for_socket)
        4    0.000    0.000    3.005    0.751 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:41(_retry_on_intr)
        3    0.000    0.000    3.005    1.002 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:99(do_poll)
        4    3.005    0.751    3.005    0.751 {method 'poll' of 'select.poll' objects}
      3/1    0.000    0.000    2.195    2.195 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:831(_validate_conn)
      3/1    0.000    0.000    2.195    2.195 /usr/local/lib/python3.7/site-packages/urllib3/connection.py:299(connect)




2019-10-07 18:12:55,308  - python37_3 - test_grequests_v2.py:main:182 - WARNING - total_time=0:00:03.297148

2019-10-07 18:12:55,308  - python37_3 - test_grequests_v2.py:main:184 - INFO - END

=============
```
