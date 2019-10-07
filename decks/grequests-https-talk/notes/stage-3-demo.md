### Stage-3

```text
cat stages/03/python27/requirements.txt

cat stages/03/python37/requirements.txt

STAGE=3 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh | grep -E '===|total_time|installed_modules'
STAGE=3 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh

STAGE=3 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh | grep -E '===|total_time|installed_modules'
STAGE=3 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```


#### Sample output

```text
cat stages/03/python27/requirements.txt
```

```text
urllib3==1.24.1
requests==2.21.0
gevent==1.4.0
grequests==0.3.0
pyopenssl==19.0.0
gevent-openssl==1.2
```

```text
cat stages/03/python37/requirements.txt
```

```text
urllib3==1.24.1
requests==2.21.0
gevent==1.4.0
grequests==0.3.0
pyopenssl==19.0.0
gevent-openssl==1.2
```

```text
STAGE=3 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh | grep -E '===|total_time|installed_modules'
```

```text
=============
test_grequests_python27_3: installed_modules: urllib3==1.24.1 requests==2.21.0 gevent==1.4.0 grequests==0.3.0 pyopenssl==19.0.0 gevent-openssl==1.2
2019-10-07 10:29:59,028  - python27_3 - test_grequests_v2.py:main:182 - WARNING - total_time=0:00:01.213074
=============
```

```text
STAGE=3 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```

```text
=============
test_grequests_python27_3: installed_modules: urllib3==1.24.1 requests==2.21.0 gevent==1.4.0 grequests==0.3.0 pyopenssl==19.0.0 gevent-openssl==1.2
2019-10-07 10:30:12,333  - python27_3 - test_grequests_v2.py:main:165 - INFO - START
2019-10-07 10:30:12,363  - python27_3 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 10:30:12,398  - python27_3 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 10:30:12,415  - python27_3 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 10:30:13,455  - python27_3 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 309
2019-10-07 10:30:13,468  - python27_3 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 309
2019-10-07 10:30:13,480  - python27_3 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 309
2019-10-07 10:30:13,488  - python27_3 - test_grequests_v2.py:make_requests:128 - INFO - len(all_page_ids) = 3
2019-10-07 10:30:13,489  - python27_3 - test_grequests_v2.py:make_requests:129 - INFO - len(valid_page_ids) = 3
2019-10-07 10:30:13,489  - python27_3 - test_grequests_v2.py:make_requests:130 - INFO - len(invalid_page_ids) = 0
         8262 function calls (8063 primitive calls) in 1.154 seconds

   Ordered by: cumulative time
   List reduced from 567 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.154    1.154 /usr/local/lib/python2.7/site-packages/grequests.py:103(map)
      3/1    0.000    0.000    1.154    1.154 /usr/local/lib/python2.7/site-packages/grequests.py:60(send)
      3/1    0.000    0.000    1.154    1.154 /usr/local/lib/python2.7/site-packages/requests/sessions.py:466(request)
      3/1    0.000    0.000    1.131    1.131 /usr/local/lib/python2.7/site-packages/requests/sessions.py:617(send)
      3/1    0.000    0.000    1.128    1.128 /usr/local/lib/python2.7/site-packages/requests/adapters.py:394(send)
      3/1    0.000    0.000    1.121    1.121 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:446(urlopen)
      3/1    0.000    0.000    1.117    1.117 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:319(_make_request)
      3/1    0.000    0.000    1.115    1.115 /usr/local/lib/python2.7/httplib.py:1084(getresponse)
      3/1    0.000    0.000    1.115    1.115 /usr/local/lib/python2.7/httplib.py:431(begin)
     21/7    0.002    0.000    1.113    0.159 /usr/local/lib/python2.7/socket.py:410(readline)
      3/1    0.000    0.000    1.112    1.112 /usr/local/lib/python2.7/httplib.py:392(_read_status)

      3/1    0.000    0.000    1.112    1.112 /usr/local/lib/python2.7/site-packages/urllib3/contrib/pyopenssl.py:271(recv)
      3/1    0.000    0.000    1.097    1.097 /usr/local/lib/python2.7/site-packages/gevent_openssl/SSL.py:61(recv)

      9/1    0.997    0.111    1.097    1.097 /usr/local/lib/python2.7/site-packages/gevent_openssl/SSL.py:24(__iowait)
        3    0.000    0.000    0.036    0.012 /usr/local/lib/python2.7/site-packages/requests/sessions.py:426(prepare_request)
     54/6    0.004    0.000    0.021    0.003 /usr/local/lib/python2.7/site-packages/gevent/builtins.py:72(__import__)
     54/6    0.008    0.000    0.019    0.003 {__import__}
      3/1    0.000    0.000    0.019    0.019 /usr/local/lib/python2.7/site-packages/urllib3/connection.py:145(_new_conn)
      3/1    0.000    0.000    0.019    0.019 /usr/local/lib/python2.7/site-packages/urllib3/util/connection.py:33(create_connection)
        3    0.000    0.000    0.015    0.005 /usr/local/lib/python2.7/site-packages/urllib3/util/ssl_.py:229(create_urllib3_context)




2019-10-07 10:30:13,501  - python27_3 - test_grequests_v2.py:main:182 - WARNING - total_time=0:00:01.173061

2019-10-07 10:30:13,501  - python27_3 - test_grequests_v2.py:main:184 - INFO - END

=============
```

```text
STAGE=3 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh | grep -E '===|total_time|installed_modules'
```

```text
=============
test_grequests_python37_3: installed_modules: urllib3==1.24.1 requests==2.21.0 gevent==1.4.0 grequests==0.3.0 pyopenssl==19.0.0 gevent-openssl==1.2
2019-10-07 10:30:50,850  - python37_3 - test_grequests_v2.py:main:182 - WARNING - total_time=0:00:03.254853
=============
```

```text
STAGE=3 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```

```text
=============
test_grequests_python37_3: installed_modules: urllib3==1.24.1 requests==2.21.0 gevent==1.4.0 grequests==0.3.0 pyopenssl==19.0.0 gevent-openssl==1.2
2019-10-07 10:31:01,024  - python37_3 - test_grequests_v2.py:main:165 - INFO - START
2019-10-07 10:31:01,067  - python37_3 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 10:31:01,128  - python37_3 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 10:31:01,153  - python37_3 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 10:31:02,206  - python37_3 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 309
2019-10-07 10:31:03,230  - python37_3 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 309
2019-10-07 10:31:04,251  - python37_3 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 309
2019-10-07 10:31:04,265  - python37_3 - test_grequests_v2.py:make_requests:128 - INFO - len(all_page_ids) = 3
2019-10-07 10:31:04,265  - python37_3 - test_grequests_v2.py:make_requests:129 - INFO - len(valid_page_ids) = 3
2019-10-07 10:31:04,265  - python37_3 - test_grequests_v2.py:make_requests:130 - INFO - len(invalid_page_ids) = 0
         11223 function calls (11075 primitive calls) in 3.239 seconds

   Ordered by: cumulative time
   List reduced from 750 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.240    3.240 /usr/local/lib/python3.7/site-packages/grequests.py:103(map)
      3/1    0.000    0.000    3.239    3.239 /usr/local/lib/python3.7/site-packages/grequests.py:60(send)
      3/1    0.000    0.000    3.239    3.239 /usr/local/lib/python3.7/site-packages/requests/sessions.py:466(request)
      3/1    0.000    0.000    3.204    3.204 /usr/local/lib/python3.7/site-packages/requests/sessions.py:617(send)
      3/1    0.000    0.000    3.202    3.202 /usr/local/lib/python3.7/site-packages/requests/adapters.py:394(send)
      3/1    0.001    0.000    3.192    3.192 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:446(urlopen)
      3/1    0.001    0.000    3.185    3.185 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:319(_make_request)
        3    0.000    0.000    3.023    1.008 /usr/local/lib/python3.7/http/client.py:1277(getresponse)
        3    0.000    0.000    3.023    1.008 /usr/local/lib/python3.7/http/client.py:289(begin)
        3    0.000    0.000    3.007    1.002 /usr/local/lib/python3.7/http/client.py:256(_read_status)
       21    0.000    0.000    3.007    0.143 {method 'readline' of '_io.BufferedReader' objects}
        3    0.000    0.000    3.007    1.002 /usr/local/lib/python3.7/socket.py:575(readinto)

      6/3    0.001    0.000    3.007    1.002 /usr/local/lib/python3.7/site-packages/urllib3/contrib/pyopenssl.py:292(recv_into)

        3    0.000    0.000    3.004    1.001 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:139(wait_for_read)
        3    0.000    0.000    3.004    1.001 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:87(poll_wait_for_socket)
        4    0.000    0.000    3.004    0.751 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:41(_retry_on_intr)
        3    0.000    0.000    3.004    1.001 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:99(do_poll)

        4    3.004    0.751    3.004    0.751 {method 'poll' of 'select.poll' objects}
      3/1    0.000    0.000    2.171    2.171 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:831(_validate_conn)
      3/1    0.000    0.000    2.171    2.171 /usr/local/lib/python3.7/site-packages/urllib3/connection.py:299(connect)




2019-10-07 10:31:04,276  - python37_3 - test_grequests_v2.py:main:182 - WARNING - total_time=0:00:03.258986

2019-10-07 10:31:04,277  - python37_3 - test_grequests_v2.py:main:184 - INFO - END

=============
```

