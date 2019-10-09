### Stage-0 Python2.7 profiling

```
STAGE=0 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```

#### Sample output

```text
STAGE=0 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```

```text
=============
localhost - START
localhost - Starting new HTTPS connection (1): localhost:8082
localhost - Starting new HTTPS connection (1): localhost:8082
localhost - Starting new HTTPS connection (1): localhost:8082
localhost -
localhost - sending_request
localhost -
localhost - https://localhost:8082 "GET /delay/1?page=1 HTTP/1.1" 200 302
localhost -
localhost - sending_request
localhost -
localhost - https://localhost:8082 "GET /delay/1?page=2 HTTP/1.1" 200 302
localhost -
localhost - sending_request
localhost -
localhost - https://localhost:8082 "GET /delay/1?page=0 HTTP/1.1" 200 302
localhost - len(all_page_ids) = 3
localhost - len(valid_page_ids) = 3
localhost - len(invalid_page_ids) = 0
localhost - total_time=0:00:03.084680
localhost - END
         11934 function calls (11618 primitive calls) in 3.055 seconds

   Ordered by: cumulative time
   List reduced from 681 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.055    3.055 grequests.py:103(map)
      3/1    0.000    0.000    3.055    3.055 grequests.py:60(send)
      3/1    0.000    0.000    3.055    3.055 sessions.py:466(request)
      3/1    0.000    0.000    3.053    3.053 sessions.py:617(send)
      3/1    0.000    0.000    3.053    3.053 adapters.py:394(send)
      3/1    0.000    0.000    3.053    3.053 connectionpool.py:451(urlopen)
      3/1    0.000    0.000    3.052    3.052 connectionpool.py:319(_make_request)
        9    0.000    0.000    3.020    0.336 wait.py:139(wait_for_read)
        9    0.000    0.000    3.020    0.336 wait.py:87(poll_wait_for_socket)
       10    0.000    0.000    3.019    0.302 wait.py:45(_retry_on_intr)
        9    0.000    0.000    3.019    0.335 wait.py:99(do_poll)
       10    3.019    0.302    3.019    0.302 {built-in method poll}
        3    0.000    0.000    3.008    1.003 httplib.py:1084(getresponse)
        3    0.000    0.000    3.008    1.003 httplib.py:431(begin)
       21    0.000    0.000    3.007    0.143 socket.py:410(readline)
        3    0.000    0.000    3.007    1.002 httplib.py:392(_read_status)
      6/3    0.000    0.000    3.007    1.002 pyopenssl.py:271(recv)
      3/1    0.000    0.000    2.050    2.050 connectionpool.py:836(_validate_conn)
      3/1    0.000    0.000    2.046    2.046 connection.py:299(connect)
      3/2    0.000    0.000    2.028    1.014 _socket2.py:233(connect)

=============
```
