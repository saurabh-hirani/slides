### Stage-0 Python2.7 profiling

```
python2 ./bin/test_grequests_v1.py --url https://localhost:8082/delay/1 --url-count 5 --log-level DEBUG --profile-code --profile-stats-count 20

STAGE=0 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```

#### Sample output

```text
STAGE=0 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```

```text
=============
2019-10-07 17:53:26,107 test_grequests_v1.py:main:159 - INFO - START
2019-10-07 17:53:26,131 connectionpool.py:_new_conn:818 - DEBUG - Starting new HTTPS connection (1): localhost:8082
2019-10-07 17:53:26,132 connectionpool.py:_new_conn:818 - DEBUG - Starting new HTTPS connection (1): localhost:8082
2019-10-07 17:53:26,133 connectionpool.py:_new_conn:818 - DEBUG - Starting new HTTPS connection (1): localhost:8082
2019-10-07 17:53:26,138 connectionpool.py:_make_request:355 - DEBUG -
2019-10-07 17:53:26,138 connectionpool.py:_make_request:356 - DEBUG - sending_request
2019-10-07 17:53:26,139 connectionpool.py:_make_request:357 - DEBUG -
2019-10-07 17:53:27,140 connectionpool.py:_make_request:398 - DEBUG - https://localhost:8082 "GET /delay/1?page=2 HTTP/1.1" 200 302
2019-10-07 17:53:27,149 connectionpool.py:_make_request:355 - DEBUG -
2019-10-07 17:53:27,149 connectionpool.py:_make_request:356 - DEBUG - sending_request
2019-10-07 17:53:27,149 connectionpool.py:_make_request:357 - DEBUG -
2019-10-07 17:53:28,156 connectionpool.py:_make_request:398 - DEBUG - https://localhost:8082 "GET /delay/1?page=1 HTTP/1.1" 200 302
2019-10-07 17:53:28,163 connectionpool.py:_make_request:355 - DEBUG -
2019-10-07 17:53:28,163 connectionpool.py:_make_request:356 - DEBUG - sending_request
2019-10-07 17:53:28,163 connectionpool.py:_make_request:357 - DEBUG -
2019-10-07 17:53:29,165 connectionpool.py:_make_request:398 - DEBUG - https://localhost:8082 "GET /delay/1?page=0 HTTP/1.1" 200 302
2019-10-07 17:53:29,166 test_grequests_v1.py:make_requests:122 - INFO - len(all_page_ids) = 3
2019-10-07 17:53:29,166 test_grequests_v1.py:make_requests:123 - INFO - len(valid_page_ids) = 3
2019-10-07 17:53:29,166 test_grequests_v1.py:make_requests:124 - INFO - len(invalid_page_ids) = 0
2019-10-07 17:53:29,183 test_grequests_v1.py:main:176 - WARNING - total_time=0:00:03.084828
2019-10-07 17:53:29,183 test_grequests_v1.py:main:178 - INFO - END
         12505 function calls (12189 primitive calls) in 3.057 seconds

   Ordered by: cumulative time
   List reduced from 687 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.057    3.057 /usr/local/lib/python2.7/site-packages/grequests.py:103(map)
      3/1    0.000    0.000    3.057    3.057 /usr/local/lib/python2.7/site-packages/grequests.py:60(send)
      3/1    0.000    0.000    3.057    3.057 /usr/local/lib/python2.7/site-packages/requests/sessions.py:466(request)
      3/1    0.000    0.000    3.055    3.055 /usr/local/lib/python2.7/site-packages/requests/sessions.py:617(send)
      3/1    0.000    0.000    3.055    3.055 /usr/local/lib/python2.7/site-packages/requests/adapters.py:394(send)
      3/1    0.000    0.000    3.054    3.054 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:451(urlopen)
      3/1    0.000    0.000    3.054    3.054 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:319(_make_request)

        9    0.000    0.000    3.020    0.336 /usr/local/lib/python2.7/site-packages/urllib3/util/wait.py:139(wait_for_read)
        9    0.000    0.000    3.020    0.336 /usr/local/lib/python2.7/site-packages/urllib3/util/wait.py:87(poll_wait_for_socket)

       10    0.000    0.000    3.020    0.302 /usr/local/lib/python2.7/site-packages/urllib3/util/wait.py:45(_retry_on_intr)
        9    0.000    0.000    3.020    0.336 /usr/local/lib/python2.7/site-packages/urllib3/util/wait.py:99(do_poll)
       10    3.020    0.302    3.020    0.302 {built-in method poll}
        3    0.000    0.000    3.008    1.003 /usr/local/Cellar/python@2/2.7.15_3/Frameworks/Python.framework/Versions/2.7/lib/python2.7/httplib.py:1084(getresponse)
        3    0.000    0.000    3.008    1.003 /usr/local/Cellar/python@2/2.7.15_3/Frameworks/Python.framework/Versions/2.7/lib/python2.7/httplib.py:431(begin)
       21    0.000    0.000    3.007    0.143 /usr/local/Cellar/python@2/2.7.15_3/Frameworks/Python.framework/Versions/2.7/lib/python2.7/socket.py:410(readline)
        3    0.000    0.000    3.007    1.002 /usr/local/Cellar/python@2/2.7.15_3/Frameworks/Python.framework/Versions/2.7/lib/python2.7/httplib.py:392(_read_status)

      6/3    0.000    0.000    3.007    1.002 /usr/local/lib/python2.7/site-packages/urllib3/contrib/pyopenssl.py:271(recv)

      3/1    0.000    0.000    2.052    2.052 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:836(_validate_conn)
      3/1    0.000    0.000    2.049    2.049 /usr/local/lib/python2.7/site-packages/urllib3/connection.py:299(connect)
      3/2    0.000    0.000    2.030    1.015 /usr/local/lib/python2.7/site-packages/gevent/_socket2.py:233(connect)
=============
```
