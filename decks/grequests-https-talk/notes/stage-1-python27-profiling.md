### Stage-1 Python2.7 profiling

```text
STAGE=1 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 LOG_LEVEL=DEBUG ./bin/run-stages.sh
```


#### Sample output

```text
STAGE=1 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 LOG_LEVEL=DEBUG ./bin/run-stages.sh
```

```text
=============
test_grequests_python27_1: installed_module: urllib3==1.24.1
test_grequests_python27_1: installed_module: requests==2.21.0
test_grequests_python27_1: installed_module: gevent==1.4.0
test_grequests_python27_1: installed_module: grequests==0.3.0
=============
python27_1 - START
python27_1 - Starting new HTTPS connection (1): https_server:8081
python27_1 - Starting new HTTPS connection (1): https_server:8081
python27_1 - Starting new HTTPS connection (1): https_server:8081
python27_1 - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 308
python27_1 - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 308
python27_1 - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 308
python27_1 - len(all_page_ids) = 3
python27_1 - len(valid_page_ids) = 3
python27_1 - len(invalid_page_ids) = 0
         6916 function calls (6727 primitive calls) in 1.123 seconds

   Ordered by: cumulative time
   List reduced from 502 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.123    1.123 grequests.py:103(map)
      3/1    0.000    0.000    1.123    1.123 grequests.py:60(send)
      3/1    0.000    0.000    1.123    1.123 sessions.py:466(request)
      3/1    0.000    0.000    1.104    1.104 sessions.py:617(send)
      3/1    0.000    0.000    1.101    1.101 adapters.py:394(send)
      3/1    0.000    0.000    1.095    1.095 connectionpool.py:446(urlopen)
      3/1    0.000    0.000    1.091    1.091 connectionpool.py:319(_make_request)
      3/1    0.000    0.000    1.089    1.089 httplib.py:1084(getresponse)
      3/1    0.000    0.000    1.089    1.089 httplib.py:431(begin)
     21/7    0.002    0.000    1.087    0.155 socket.py:410(readline)
      3/1    0.000    0.000    1.086    1.086 httplib.py:392(_read_status)
      3/1    0.000    0.000    1.086    1.086 _sslgte279.py:448(recv)
      3/1    0.992    0.331    1.074    1.074 _sslgte279.py:298(read)
        3    0.000    0.000    0.031    0.010 sessions.py:426(prepare_request)
     54/6    0.003    0.000    0.017    0.003 builtins.py:72(__import__)
     54/6    0.007    0.000    0.017    0.003 {__import__}
        3    0.000    0.000    0.013    0.004 models.py:307(prepare)
       21    0.001    0.000    0.013    0.001 sessions.py:49(merge_setting)
        6    0.000    0.000    0.012    0.002 hub.py:684(_get_resolver)
        3    0.000    0.000    0.012    0.004 adapters.py:292(get_connection)




python27_1 - total_time=0:00:01.143969

python27_1 - END

=============
```
