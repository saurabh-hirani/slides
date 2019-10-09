### Stage-2

```text
cat stages/02/python27/requirements.txt

cat stages/02/python37/requirements.txt

STAGE=2 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh | \
grep -E '===|total_time|installed_module'

STAGE=2 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh

STAGE=2 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh | \
grep -E '===|total_time|installed_module'

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
STAGE=2 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh | \
grep -E '===|total_time|installed_module'
```

```text
=============
test_grequests_python27_2: installed_module: urllib3==1.24.1
test_grequests_python27_2: installed_module: requests==2.21.0
test_grequests_python27_2: installed_module: gevent==1.4.0
test_grequests_python27_2: installed_module: grequests==0.3.0
test_grequests_python27_2: installed_module: pyopenssl==19.0.0
=============
python27_2 - total_time=0:00:03.188926
=============
```

```text
STAGE=2 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```

```text
=============
test_grequests_python27_2: installed_module: urllib3==1.24.1
test_grequests_python27_2: installed_module: requests==2.21.0
test_grequests_python27_2: installed_module: gevent==1.4.0
test_grequests_python27_2: installed_module: grequests==0.3.0
test_grequests_python27_2: installed_module: pyopenssl==19.0.0
=============
python27_2 - START
python27_2 - Starting new HTTPS connection (1): https_server:8081
python27_2 - Starting new HTTPS connection (1): https_server:8081
python27_2 - Starting new HTTPS connection (1): https_server:8081
python27_2 - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 309
python27_2 - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 309
python27_2 - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 309
python27_2 - len(all_page_ids) = 3
python27_2 - len(valid_page_ids) = 3
python27_2 - len(invalid_page_ids) = 0
         8215 function calls (8051 primitive calls) in 3.142 seconds

   Ordered by: cumulative time
   List reduced from 562 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.142    3.142 grequests.py:103(map)
      3/1    0.000    0.000    3.141    3.141 grequests.py:60(send)
      3/1    0.000    0.000    3.141    3.141 sessions.py:466(request)
      3/1    0.000    0.000    3.122    3.122 sessions.py:617(send)
      3/1    0.000    0.000    3.118    3.118 adapters.py:394(send)
      3/1    0.000    0.000    3.106    3.106 connectionpool.py:446(urlopen)
      3/1    0.000    0.000    3.102    3.102 connectionpool.py:319(_make_request)
        3    0.000    0.000    3.021    1.007 httplib.py:1084(getresponse)
        3    0.000    0.000    3.021    1.007 httplib.py:431(begin)
       21    0.002    0.000    3.013    0.143 socket.py:410(readline)
        3    0.000    0.000    3.010    1.003 httplib.py:392(_read_status)
        7    0.000    0.000    3.010    0.430 wait.py:139(wait_for_read)
        7    0.000    0.000    3.010    0.430 wait.py:87(poll_wait_for_socket)
      6/3    0.001    0.000    3.009    1.003 pyopenssl.py:271(recv)
        8    0.000    0.000    3.009    0.376 wait.py:45(_retry_on_intr)
        7    0.000    0.000    3.009    0.430 wait.py:99(do_poll)
        8    3.009    0.376    3.009    0.376 {built-in method poll}
      3/1    0.000    0.000    2.087    2.087 connectionpool.py:831(_validate_conn)
      3/1    0.000    0.000    2.086    2.086 connection.py:299(connect)
      3/1    0.000    0.000    2.075    2.075 connection.py:145(_new_conn)




python27_2 - total_time=0:00:03.171143

python27_2 - END

=============
```

```text
STAGE=2 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh | \
grep -E '===|total_time|installed_module'
```

```text
=============
test_grequests_python37_2: installed_module: urllib3==1.24.1
test_grequests_python37_2: installed_module: requests==2.21.0
test_grequests_python37_2: installed_module: gevent==1.4.0
test_grequests_python37_2: installed_module: grequests==0.3.0
test_grequests_python37_2: installed_module: pyopenssl==19.0.0
=============
python37_2 - total_time=0:00:03.229380
=============
```

```text
STAGE=2 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```

```text
=============
test_grequests_python37_2: installed_module: urllib3==1.24.1
test_grequests_python37_2: installed_module: requests==2.21.0
test_grequests_python37_2: installed_module: gevent==1.4.0
test_grequests_python37_2: installed_module: grequests==0.3.0
test_grequests_python37_2: installed_module: pyopenssl==19.0.0
=============
python37_2 - START
python37_2 - Starting new HTTPS connection (1): https_server:8081
python37_2 - Starting new HTTPS connection (1): https_server:8081
python37_2 - Starting new HTTPS connection (1): https_server:8081
python37_2 - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 308
python37_2 - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 308
python37_2 - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 308
python37_2 - len(all_page_ids) = 3
python37_2 - len(valid_page_ids) = 3
python37_2 - len(invalid_page_ids) = 0
         11135 function calls (10997 primitive calls) in 3.275 seconds

   Ordered by: cumulative time
   List reduced from 740 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.276    3.276 grequests.py:103(map)
      3/1    0.000    0.000    3.275    3.275 grequests.py:60(send)
      3/1    0.000    0.000    3.275    3.275 sessions.py:466(request)
      3/1    0.001    0.000    3.233    3.233 sessions.py:617(send)
      3/1    0.000    0.000    3.231    3.231 adapters.py:394(send)
      3/1    0.001    0.000    3.221    3.221 connectionpool.py:446(urlopen)
      3/1    0.001    0.000    3.216    3.216 connectionpool.py:319(_make_request)
        3    0.000    0.000    3.025    1.008 client.py:1277(getresponse)
        3    0.000    0.000    3.025    1.008 client.py:289(begin)
        7    0.000    0.000    3.010    0.430 wait.py:139(wait_for_read)
        7    0.000    0.000    3.009    0.430 wait.py:87(poll_wait_for_socket)
        8    0.000    0.000    3.009    0.376 wait.py:41(_retry_on_intr)
        7    0.000    0.000    3.008    0.430 wait.py:99(do_poll)
        8    3.008    0.376    3.008    0.376 {method 'poll' of 'select.poll' objects}
        3    0.000    0.000    3.008    1.003 client.py:256(_read_status)
       21    0.000    0.000    3.008    0.143 {method 'readline' of '_io.BufferedReader' objects}
        3    0.000    0.000    3.007    1.002 socket.py:575(readinto)
      6/3    0.000    0.000    3.007    1.002 pyopenssl.py:292(recv_into)
      3/1    0.000    0.000    2.202    2.202 connectionpool.py:831(_validate_conn)
      3/1    0.001    0.000    2.201    2.201 connection.py:299(connect)




python37_2 - total_time=0:00:03.302343

python37_2 - END

=============
```
