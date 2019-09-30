### Python2.7 uses recv

```shell

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   10.630   10.630 /usr/local/lib/python3.7/site-packages/grequests.py:103(map)
     10/1    0.001    0.000   10.629   10.629 /usr/local/lib/python3.7/site-packages/grequests.py:60(send)
     10/1    0.000    0.000   10.629   10.629 /usr/local/lib/python3.7/site-packages/requests/sessions.py:466(request)
     10/1    0.001    0.000   10.600   10.600 /usr/local/lib/python3.7/site-packages/requests/sessions.py:617(send)
     10/1    0.001    0.000   10.597   10.597 /usr/local/lib/python3.7/site-packages/requests/adapters.py:394(send)
     10/1    0.001    0.000   10.588   10.588 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:446(urlopen)
     10/1    0.002    0.000   10.583   10.583 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:319(_make_request)
       10    0.000    0.000   10.096    1.010 /usr/local/lib/python3.7/http/client.py:1277(getresponse)
       10    0.001    0.000   10.095    1.009 /usr/local/lib/python3.7/http/client.py:289(begin)
       10    0.001    0.000   10.037    1.004 /usr/local/lib/python3.7/http/client.py:256(_read_status)
       70    0.001    0.000   10.036    0.143 {method 'readline' of '_io.BufferedReader' objects}
       10    0.000    0.000   10.035    1.004 /usr/local/lib/python3.7/socket.py:575(readinto)

    20/10    0.002    0.000   10.034    1.003 /usr/local/lib/python3.7/site-packages/urllib3/contrib/pyopenssl.py:292(recv_into)

       10    0.000    0.000   10.026    1.003 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:139(wait_for_read)
       10    0.001    0.000   10.025    1.003 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:87(poll_wait_for_socket)
       11    0.000    0.000   10.024    0.911 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:41(_retry_on_intr)
       10    0.001    0.000   10.024    1.002 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:99(do_poll)
       11   10.023    0.911   10.023    0.911 {method 'poll' of 'select.poll' objects}
     10/1    0.001    0.000    9.564    9.564 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:831(_validate_conn)
     10/1    0.001    0.000    9.564    9.564 /usr/local/lib/python3.7/site-packages/urllib3/connection.py:299(connect)
```
