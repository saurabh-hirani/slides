### Stage-3

```text
cat stages/03/python27/requirements.txt

cat stages/03/python37/requirements.txt

STAGE=3 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh | \
grep -E '===|total_time|installed_module'

STAGE=3 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh

STAGE=3 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh | \
grep -E '===|total_time|installed_module'

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
STAGE=3 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh | \
grep -E '===|total_time|installed_module'
```

```text
=============
test_grequests_python27_3: installed_module: urllib3==1.24.1
test_grequests_python27_3: installed_module: requests==2.21.0
test_grequests_python27_3: installed_module: gevent==1.4.0
test_grequests_python27_3: installed_module: grequests==0.3.0
test_grequests_python27_3: installed_module: pyopenssl==19.0.0
test_grequests_python27_3: installed_module: gevent-openssl==1.2
=============
python27_3 - total_time=0:00:01.148449
=============
```

```text
STAGE=3 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```

```text
=============
test_grequests_python27_3: installed_module: urllib3==1.24.1
test_grequests_python27_3: installed_module: requests==2.21.0
test_grequests_python27_3: installed_module: gevent==1.4.0
test_grequests_python27_3: installed_module: grequests==0.3.0
test_grequests_python27_3: installed_module: pyopenssl==19.0.0
test_grequests_python27_3: installed_module: gevent-openssl==1.2
=============
python27_3 - START
python27_3 - Starting new HTTPS connection (1): https_server:8081
python27_3 - Starting new HTTPS connection (1): https_server:8081
python27_3 - Starting new HTTPS connection (1): https_server:8081
python27_3 - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 308
python27_3 - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 308
python27_3 - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 308
python27_3 - len(all_page_ids) = 3
python27_3 - len(valid_page_ids) = 3
python27_3 - len(invalid_page_ids) = 0
         8243 function calls (8044 primitive calls) in 1.162 seconds

   Ordered by: cumulative time
   List reduced from 562 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.163    1.163 grequests.py:103(map)
      3/1    0.000    0.000    1.162    1.162 grequests.py:60(send)
      3/1    0.000    0.000    1.162    1.162 sessions.py:466(request)
      3/1    0.001    0.000    1.139    1.139 sessions.py:617(send)
      3/1    0.000    0.000    1.137    1.137 adapters.py:394(send)
      3/1    0.001    0.000    1.129    1.129 connectionpool.py:446(urlopen)
      3/1    0.000    0.000    1.124    1.124 connectionpool.py:319(_make_request)
      3/1    0.000    0.000    1.123    1.123 httplib.py:1084(getresponse)
      3/1    0.000    0.000    1.123    1.123 httplib.py:431(begin)
     21/7    0.002    0.000    1.121    0.160 socket.py:410(readline)
      3/1    0.000    0.000    1.120    1.120 httplib.py:392(_read_status)
      3/1    0.000    0.000    1.120    1.120 pyopenssl.py:271(recv)
      3/1    0.000    0.000    1.105    1.105 SSL.py:61(recv)
      9/1    1.002    0.111    1.105    1.105 SSL.py:24(__iowait)
        3    0.000    0.000    0.036    0.012 sessions.py:426(prepare_request)
     54/6    0.004    0.000    0.022    0.004 builtins.py:72(__import__)
     54/6    0.008    0.000    0.020    0.003 {__import__}
      3/1    0.000    0.000    0.018    0.018 connection.py:145(_new_conn)
      3/1    0.000    0.000    0.018    0.018 connection.py:33(create_connection)
        3    0.000    0.000    0.016    0.005 ssl_.py:229(create_urllib3_context)




python27_3 - total_time=0:00:01.183905

python27_3 - END

=============
```

```text
STAGE=3 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh | \
grep -E '===|total_time|installed_module'
```

```text
=============
test_grequests_python37_3: installed_module: urllib3==1.24.1
test_grequests_python37_3: installed_module: requests==2.21.0
test_grequests_python37_3: installed_module: gevent==1.4.0
test_grequests_python37_3: installed_module: grequests==0.3.0
test_grequests_python37_3: installed_module: pyopenssl==19.0.0
test_grequests_python37_3: installed_module: gevent-openssl==1.2
=============
python37_3 - total_time=0:00:03.219669
=============
```

```text
STAGE=3 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```

```text
=============
test_grequests_python37_3: installed_module: urllib3==1.24.1
test_grequests_python37_3: installed_module: requests==2.21.0
test_grequests_python37_3: installed_module: gevent==1.4.0
test_grequests_python37_3: installed_module: grequests==0.3.0
test_grequests_python37_3: installed_module: pyopenssl==19.0.0
test_grequests_python37_3: installed_module: gevent-openssl==1.2
=============
python37_3 - START
python37_3 - Starting new HTTPS connection (1): https_server:8081
python37_3 - Starting new HTTPS connection (1): https_server:8081
python37_3 - Starting new HTTPS connection (1): https_server:8081
python37_3 - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 308
python37_3 - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 308
python37_3 - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 308
python37_3 - len(all_page_ids) = 3
python37_3 - len(valid_page_ids) = 3
python37_3 - len(invalid_page_ids) = 0
         11205 function calls (11057 primitive calls) in 3.163 seconds

   Ordered by: cumulative time
   List reduced from 746 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.164    3.164 grequests.py:103(map)
      3/1    0.000    0.000    3.164    3.164 grequests.py:60(send)
      3/1    0.000    0.000    3.164    3.164 sessions.py:466(request)
      3/1    0.000    0.000    3.139    3.139 sessions.py:617(send)
      3/1    0.001    0.000    3.136    3.136 adapters.py:394(send)
      3/1    0.000    0.000    3.130    3.130 connectionpool.py:446(urlopen)
      3/1    0.001    0.000    3.126    3.126 connectionpool.py:319(_make_request)
        3    0.000    0.000    2.994    0.998 client.py:1277(getresponse)
        3    0.000    0.000    2.993    0.998 client.py:289(begin)
        3    0.000    0.000    2.975    0.992 client.py:256(_read_status)
       21    0.000    0.000    2.975    0.142 {method 'readline' of '_io.BufferedReader' objects}
        3    0.000    0.000    2.974    0.991 socket.py:575(readinto)
      6/3    0.001    0.000    2.974    0.991 pyopenssl.py:292(recv_into)
        3    0.000    0.000    2.972    0.991 wait.py:139(wait_for_read)
        3    0.000    0.000    2.972    0.991 wait.py:87(poll_wait_for_socket)
        4    0.000    0.000    2.971    0.743 wait.py:41(_retry_on_intr)
        3    0.000    0.000    2.971    0.990 wait.py:99(do_poll)
        4    2.971    0.743    2.971    0.743 {method 'poll' of 'select.poll' objects}
      3/1    0.000    0.000    2.149    2.149 connectionpool.py:831(_validate_conn)
      3/1    0.000    0.000    2.149    2.149 connection.py:299(connect)




python37_3 - total_time=0:00:03.186629

python37_3 - END

=============
```
