### Stage-1 Python2.7 profiling

```text
STAGE=1 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 LOG_LEVEL=DEBUG ./bin/run-stages.sh
```

### Sample output

```text
STAGE=1 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 LOG_LEVEL=DEBUG ./bin/run-stages.sh
```

```text
=============
test_grequests_python27_1: installed_modules: urllib3==1.24.1 requests==2.21.0 gevent==1.4.0 grequests==0.3.0
2019-10-07 09:58:34,094  - python27_1 - test_grequests_v1.py:main:159 - INFO - START
2019-10-07 09:58:34,121  - python27_1 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 09:58:34,159  - python27_1 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 09:58:34,177  - python27_1 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 09:58:35,200  - python27_1 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 308
2019-10-07 09:58:35,213  - python27_1 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 308
2019-10-07 09:58:35,226  - python27_1 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 308
2019-10-07 09:58:35,234  - python27_1 - test_grequests_v1.py:make_requests:122 - INFO - len(all_page_ids) = 3
2019-10-07 09:58:35,234  - python27_1 - test_grequests_v1.py:make_requests:123 - INFO - len(valid_page_ids) = 3
2019-10-07 09:58:35,234  - python27_1 - test_grequests_v1.py:make_requests:124 - INFO - len(invalid_page_ids) = 0
         6949 function calls (6761 primitive calls) in 1.139 seconds

   Ordered by: cumulative time
   List reduced from 506 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.139    1.139 /usr/local/lib/python2.7/site-packages/grequests.py:103(map)
      3/1    0.000    0.000    1.138    1.138 /usr/local/lib/python2.7/site-packages/grequests.py:60(send)
      3/1    0.000    0.000    1.138    1.138 /usr/local/lib/python2.7/site-packages/requests/sessions.py:466(request)
      3/1    0.000    0.000    1.117    1.117 /usr/local/lib/python2.7/site-packages/requests/sessions.py:617(send)
      3/1    0.000    0.000    1.115    1.115 /usr/local/lib/python2.7/site-packages/requests/adapters.py:394(send)
      3/1    0.000    0.000    1.108    1.108 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:446(urlopen)
      3/1    0.000    0.000    1.104    1.104 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:319(_make_request)
      3/1    0.000    0.000    1.102    1.102 /usr/local/lib/python2.7/httplib.py:1084(getresponse)
      3/1    0.000    0.000    1.102    1.102 /usr/local/lib/python2.7/httplib.py:431(begin)
     21/7    0.002    0.000    1.100    0.157 /usr/local/lib/python2.7/socket.py:410(readline)
      3/1    0.000    0.000    1.099    1.099 /usr/local/lib/python2.7/httplib.py:392(_read_status)

      3/1    0.000    0.000    1.099    1.099 /usr/local/lib/python2.7/site-packages/gevent/_sslgte279.py:448(recv)

      3/1    1.000    0.333    1.083    1.083 /usr/local/lib/python2.7/site-packages/gevent/_sslgte279.py:298(read)
        3    0.001    0.000    0.034    0.011 /usr/local/lib/python2.7/site-packages/requests/sessions.py:426(prepare_request)
     54/6    0.004    0.000    0.021    0.004 /usr/local/lib/python2.7/site-packages/gevent/builtins.py:72(__import__)
     54/6    0.007    0.000    0.020    0.003 {__import__}
        6    0.000    0.000    0.016    0.003 /usr/local/lib/python2.7/site-packages/gevent/hub.py:684(_get_resolver)
        5    0.000    0.000    0.015    0.003 /usr/local/lib/python2.7/site-packages/gevent/_config.py:49(getter)
        5    0.000    0.000    0.015    0.003 /usr/local/lib/python2.7/site-packages/gevent/_config.py:140(get)
        2    0.000    0.000    0.015    0.007 /usr/local/lib/python2.7/site-packages/gevent/_config.py:245(validate)




2019-10-07 09:58:35,244  - python27_1 - test_grequests_v1.py:main:176 - WARNING - total_time=0:00:01.154739

2019-10-07 09:58:35,244  - python27_1 - test_grequests_v1.py:main:178 - INFO - END

=============
```
