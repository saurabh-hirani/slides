## Stage-4 before patching demo

```text
STAGE=4 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh | \
grep -E '===|total_time|installed_module'

STAGE=4 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```


#### Sample output

```text
STAGE=4 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh | \
grep -E '===|total_time|installed_module'
```

```text
=============
test_grequests_python37_4: installed_module: urllib3==1.24.1
test_grequests_python37_4: installed_module: requests==2.21.0
test_grequests_python37_4: installed_module: gevent==1.4.0
test_grequests_python37_4: installed_module: grequests==0.3.0
test_grequests_python37_4: installed_module: pyopenssl==19.0.0
test_grequests_python37_4: installed_module: gevent-openssl==1.2
=============
python37_4 - total_time=0:00:03.228567
=============
```

```text
STAGE=4 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```

```text
=============
test_grequests_python37_4: installed_module: urllib3==1.24.1
test_grequests_python37_4: installed_module: requests==2.21.0
test_grequests_python37_4: installed_module: gevent==1.4.0
test_grequests_python37_4: installed_module: grequests==0.3.0
test_grequests_python37_4: installed_module: pyopenssl==19.0.0
test_grequests_python37_4: installed_module: gevent-openssl==1.2
=============
python37_4 - START
python37_4 - Starting new HTTPS connection (1): https_server:8081
python37_4 - Starting new HTTPS connection (1): https_server:8081
python37_4 - Starting new HTTPS connection (1): https_server:8081
python37_4 - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 308
python37_4 - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 308
python37_4 - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 308
python37_4 - len(all_page_ids) = 3
python37_4 - len(valid_page_ids) = 3
python37_4 - len(invalid_page_ids) = 0
         11205 function calls (11057 primitive calls) in 3.196 seconds

   Ordered by: cumulative time
   List reduced from 746 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.197    3.197 grequests.py:103(map)
      3/1    0.000    0.000    3.196    3.196 grequests.py:60(send)
      3/1    0.000    0.000    3.196    3.196 sessions.py:466(request)
      3/1    0.000    0.000    3.171    3.171 sessions.py:617(send)
      3/1    0.000    0.000    3.168    3.168 adapters.py:394(send)
      3/1    0.000    0.000    3.161    3.161 connectionpool.py:446(urlopen)
      3/1    0.000    0.000    3.158    3.158 connectionpool.py:319(_make_request)
        3    0.000    0.000    3.026    1.009 client.py:1277(getresponse)
        3    0.000    0.000    3.026    1.009 client.py:289(begin)
        3    0.000    0.000    3.008    1.003 client.py:256(_read_status)
       21    0.000    0.000    3.008    0.143 {method 'readline' of '_io.BufferedReader' objects}
        3    0.000    0.000    3.008    1.003 socket.py:575(readinto)
      6/3    0.001    0.000    3.007    1.002 pyopenssl.py:292(recv_into)
        3    0.000    0.000    3.005    1.002 wait.py:139(wait_for_read)
        3    0.000    0.000    3.005    1.002 wait.py:87(poll_wait_for_socket)
        4    0.000    0.000    3.005    0.751 wait.py:41(_retry_on_intr)
        3    0.000    0.000    3.004    1.001 wait.py:99(do_poll)
        4    3.004    0.751    3.004    0.751 {method 'poll' of 'select.poll' objects}
      3/1    0.000    0.000    2.145    2.145 connectionpool.py:831(_validate_conn)
      3/1    0.000    0.000    2.145    2.145 connection.py:299(connect)




python37_4 - total_time=0:00:03.220309

python37_4 - END

=============
```
