### Stage-2

```text
cat stages/02/python27/requirements.txt

cat stages/02/python37/requirements.txt

STAGE=2 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh | grep -E '===|total_time|installed_modules'
STAGE=2 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh

STAGE=2 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh | grep -E '===|total_time|installed_modules'
STAGE=2 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```


#### Sample output

```text
cat stages/02/python27/requirements.txt
```

```text
urllib3==1.24.1
requests==2.21.0
gevent==1.4.0
grequests==0.3.0
pyopenssl==19.0.0
```

```text
cat stages/02/python37/requirements.txt
```

```text
urllib3==1.24.1
requests==2.21.0
gevent==1.4.0
grequests==0.3.0
pyopenssl==19.0.0
```

```text
STAGE=2 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh | grep -E '===|total_time|installed_modules'
```

```text
=============
test_grequests_python27_2: installed_modules: urllib3==1.24.1 requests==2.21.0 gevent==1.4.0 grequests==0.3.0 pyopenssl==19.0.0
2019-10-07 10:08:27,694  - python27_2 - test_grequests_v1.py:main:176 - WARNING - total_time=0:00:03.221667
=============
```

```text
STAGE=2 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```

```text
=============
test_grequests_python27_2: installed_modules: urllib3==1.24.1 requests==2.21.0 gevent==1.4.0 grequests==0.3.0 pyopenssl==19.0.0
2019-10-07 10:09:09,031  - python27_2 - test_grequests_v1.py:main:159 - INFO - START
2019-10-07 10:09:09,067  - python27_2 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 10:09:09,131  - python27_2 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 10:09:09,170  - python27_2 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 10:09:10,178  - python27_2 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 308
2019-10-07 10:09:11,207  - python27_2 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 308
2019-10-07 10:09:12,230  - python27_2 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 308
2019-10-07 10:09:12,238  - python27_2 - test_grequests_v1.py:make_requests:122 - INFO - len(all_page_ids) = 3
2019-10-07 10:09:12,238  - python27_2 - test_grequests_v1.py:make_requests:123 - INFO - len(valid_page_ids) = 3
2019-10-07 10:09:12,238  - python27_2 - test_grequests_v1.py:make_requests:124 - INFO - len(invalid_page_ids) = 0
         8230 function calls (8066 primitive calls) in 3.205 seconds

   Ordered by: cumulative time
   List reduced from 567 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.206    3.206 /usr/local/lib/python2.7/site-packages/grequests.py:103(map)
      3/1    0.000    0.000    3.205    3.205 /usr/local/lib/python2.7/site-packages/grequests.py:60(send)
      3/1    0.000    0.000    3.205    3.205 /usr/local/lib/python2.7/site-packages/requests/sessions.py:466(request)
      3/1    0.000    0.000    3.177    3.177 /usr/local/lib/python2.7/site-packages/requests/sessions.py:617(send)
      3/1    0.000    0.000    3.175    3.175 /usr/local/lib/python2.7/site-packages/requests/adapters.py:394(send)
      3/1    0.000    0.000    3.167    3.167 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:446(urlopen)
      3/1    0.001    0.000    3.163    3.163 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:319(_make_request)
        3    0.000    0.000    2.980    0.993 /usr/local/lib/python2.7/httplib.py:1084(getresponse)
        3    0.000    0.000    2.980    0.993 /usr/local/lib/python2.7/httplib.py:431(begin)

        7    0.000    0.000    2.974    0.425 /usr/local/lib/python2.7/site-packages/urllib3/util/wait.py:139(wait_for_read)
        7    0.001    0.000    2.974    0.425 /usr/local/lib/python2.7/site-packages/urllib3/util/wait.py:87(poll_wait_for_socket)
        8    0.000    0.000    2.973    0.372 /usr/local/lib/python2.7/site-packages/urllib3/util/wait.py:45(_retry_on_intr)
       21    0.002    0.000    2.973    0.142 /usr/local/lib/python2.7/socket.py:410(readline)
        7    0.000    0.000    2.973    0.425 /usr/local/lib/python2.7/site-packages/urllib3/util/wait.py:99(do_poll)
        8    2.972    0.372    2.972    0.372 {built-in method poll}
        3    0.000    0.000    2.970    0.990 /usr/local/lib/python2.7/httplib.py:392(_read_status)

      6/3    0.000    0.000    2.969    0.990 /usr/local/lib/python2.7/site-packages/urllib3/contrib/pyopenssl.py:271(recv)

      3/1    0.000    0.000    2.155    2.155 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:831(_validate_conn)
      3/1    0.001    0.000    2.155    2.155 /usr/local/lib/python2.7/site-packages/urllib3/connection.py:299(connect)
      3/1    0.000    0.000    2.145    2.145 /usr/local/lib/python2.7/site-packages/urllib3/connection.py:145(_new_conn)




2019-10-07 10:09:12,248  - python27_2 - test_grequests_v1.py:main:176 - WARNING - total_time=0:00:03.221844

2019-10-07 10:09:12,249  - python27_2 - test_grequests_v1.py:main:178 - INFO - END

=============
```

```text
STAGE=2 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh | grep -E '===|total_time|installed_modules'
```

```text
=============
test_grequests_python37_2: installed_modules: urllib3==1.24.1 requests==2.21.0 gevent==1.4.0 grequests==0.3.0 pyopenssl==19.0.0
2019-10-07 10:09:27,232  - python37_2 - test_grequests_v1.py:main:176 - WARNING - total_time=0:00:03.266638
=============
```

```text
STAGE=2 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```

```text
=============
test_grequests_python37_2: installed_modules: urllib3==1.24.1 requests==2.21.0 gevent==1.4.0 grequests==0.3.0 pyopenssl==19.0.0
2019-10-07 10:09:37,086  - python37_2 - test_grequests_v1.py:main:159 - INFO - START
2019-10-07 10:09:37,134  - python37_2 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 10:09:37,206  - python37_2 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 10:09:37,229  - python37_2 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 10:09:38,261  - python37_2 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 308
2019-10-07 10:09:39,290  - python37_2 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 308
2019-10-07 10:09:40,289  - python37_2 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 308
2019-10-07 10:09:40,297  - python37_2 - test_grequests_v1.py:make_requests:122 - INFO - len(all_page_ids) = 3
2019-10-07 10:09:40,297  - python37_2 - test_grequests_v1.py:make_requests:123 - INFO - len(valid_page_ids) = 3
2019-10-07 10:09:40,297  - python37_2 - test_grequests_v1.py:make_requests:124 - INFO - len(invalid_page_ids) = 0
         11190 function calls (11052 primitive calls) in 3.208 seconds

   Ordered by: cumulative time
   List reduced from 744 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.209    3.209 /usr/local/lib/python3.7/site-packages/grequests.py:103(map)
      3/1    0.000    0.000    3.209    3.209 /usr/local/lib/python3.7/site-packages/grequests.py:60(send)
      3/1    0.001    0.000    3.209    3.209 /usr/local/lib/python3.7/site-packages/requests/sessions.py:466(request)
      3/1    0.001    0.000    3.172    3.172 /usr/local/lib/python3.7/site-packages/requests/sessions.py:617(send)
      3/1    0.000    0.000    3.170    3.170 /usr/local/lib/python3.7/site-packages/requests/adapters.py:394(send)
      3/1    0.000    0.000    3.160    3.160 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:446(urlopen)
      3/1    0.000    0.000    3.155    3.155 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:319(_make_request)
        3    0.000    0.000    2.991    0.997 /usr/local/lib/python3.7/http/client.py:1277(getresponse)
        3    0.000    0.000    2.991    0.997 /usr/local/lib/python3.7/http/client.py:289(begin)

        9    0.000    0.000    2.979    0.331 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:139(wait_for_read)
        9    0.000    0.000    2.978    0.331 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:87(poll_wait_for_socket)
       10    0.000    0.000    2.977    0.298 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:41(_retry_on_intr)
        9    0.000    0.000    2.977    0.331 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:99(do_poll)
       10    2.977    0.298    2.977    0.298 {method 'poll' of 'select.poll' objects}

        3    0.000    0.000    2.974    0.991 /usr/local/lib/python3.7/http/client.py:256(_read_status)
       21    0.000    0.000    2.974    0.142 {method 'readline' of '_io.BufferedReader' objects}
        3    0.000    0.000    2.974    0.991 /usr/local/lib/python3.7/socket.py:575(readinto)

      6/3    0.000    0.000    2.974    0.991 /usr/local/lib/python3.7/site-packages/urllib3/contrib/pyopenssl.py:292(recv_into)

      3/1    0.000    0.000    2.175    2.175 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:831(_validate_conn)
      3/1    0.000    0.000    2.175    2.175 /usr/local/lib/python3.7/site-packages/urllib3/connection.py:299(connect)




2019-10-07 10:09:40,307  - python37_2 - test_grequests_v1.py:main:176 - WARNING - total_time=0:00:03.228147

2019-10-07 10:09:40,307  - python37_2 - test_grequests_v1.py:main:178 - INFO - END

=============
```

