### Python2.7 uses recv

```text
STAGE=3 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```

#### Sample output

```text
STAGE=3 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```

```text
=============
test_grequests_python27_3: installed_modules: urllib3==1.24.1 requests==2.21.0 gevent==1.4.0 grequests==0.3.0 pyopenssl==19.0.0 gevent-openssl==1.2
2019-10-07 18:11:58,980  - python27_3 - test_grequests_v2.py:main:165 - INFO - START
2019-10-07 18:11:59,016  - python27_3 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 18:11:59,060  - python27_3 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 18:11:59,086  - python27_3 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 18:12:00,127  - python27_3 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 308
2019-10-07 18:12:00,139  - python27_3 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 308
2019-10-07 18:12:00,149  - python27_3 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 308
2019-10-07 18:12:00,156  - python27_3 - test_grequests_v2.py:make_requests:128 - INFO - len(all_page_ids) = 3
2019-10-07 18:12:00,157  - python27_3 - test_grequests_v2.py:make_requests:129 - INFO - len(valid_page_ids) = 3
2019-10-07 18:12:00,157  - python27_3 - test_grequests_v2.py:make_requests:130 - INFO - len(invalid_page_ids) = 0
         8251 function calls (8057 primitive calls) in 1.174 seconds

   Ordered by: cumulative time
   List reduced from 567 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.175    1.175 /usr/local/lib/python2.7/site-packages/grequests.py:103(map)
      3/1    0.000    0.000    1.174    1.174 /usr/local/lib/python2.7/site-packages/grequests.py:60(send)
      3/1    0.000    0.000    1.174    1.174 /usr/local/lib/python2.7/site-packages/requests/sessions.py:466(request)
      3/1    0.000    0.000    1.147    1.147 /usr/local/lib/python2.7/site-packages/requests/sessions.py:617(send)
      3/1    0.000    0.000    1.145    1.145 /usr/local/lib/python2.7/site-packages/requests/adapters.py:394(send)
      3/1    0.001    0.000    1.137    1.137 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:446(urlopen)
      3/1    0.000    0.000    1.133    1.133 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:319(_make_request)
      3/1    0.000    0.000    1.131    1.131 /usr/local/lib/python2.7/httplib.py:1084(getresponse)
      3/1    0.000    0.000    1.131    1.131 /usr/local/lib/python2.7/httplib.py:431(begin)
     21/7    0.001    0.000    1.129    0.161 /usr/local/lib/python2.7/socket.py:410(readline)
      3/1    0.000    0.000    1.128    1.128 /usr/local/lib/python2.7/httplib.py:392(_read_status)

      3/1    0.000    0.000    1.128    1.128 /usr/local/lib/python2.7/site-packages/urllib3/contrib/pyopenssl.py:271(recv)
      3/1    0.000    0.000    1.108    1.108 /usr/local/lib/python2.7/site-packages/gevent_openssl/SSL.py:61(recv)

      9/1    0.986    0.110    1.108    1.108 /usr/local/lib/python2.7/site-packages/gevent_openssl/SSL.py:24(__iowait)
        3    0.001    0.000    0.047    0.016 /usr/local/lib/python2.7/site-packages/requests/sessions.py:426(prepare_request)
     54/6    0.005    0.000    0.027    0.004 /usr/local/lib/python2.7/site-packages/gevent/builtins.py:72(__import__)
     54/6    0.009    0.000    0.025    0.004 {__import__}
        3    0.000    0.000    0.023    0.008 /usr/local/lib/python2.7/site-packages/urllib3/util/ssl_.py:229(create_urllib3_context)
       21    0.001    0.000    0.020    0.001 /usr/local/lib/python2.7/site-packages/requests/sessions.py:49(merge_setting)
        6    0.000    0.000    0.020    0.003 /usr/local/lib/python2.7/site-packages/gevent/hub.py:684(_get_resolver)




2019-10-07 18:12:00,166  - python27_3 - test_grequests_v2.py:main:182 - WARNING - total_time=0:00:01.194370

2019-10-07 18:12:00,166  - python27_3 - test_grequests_v2.py:main:184 - INFO - END

=============
```
