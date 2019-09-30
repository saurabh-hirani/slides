## Stage-4 before patching demo

```shell
./docker-exec.sh test_grequests_python37_4 \
   /usr/local/bin/python /app/test_grequests_v2.py \
   --url https://https_server:8081/delay/1 --url-count 10 \
   --log-level DEBUG --profile-code --profile-stats-count 20
```

```shell
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   10.756   10.756 /usr/local/lib/python3.7/site-packages/grequests.py:103(map)
     10/1    0.001    0.000   10.754   10.754 /usr/local/lib/python3.7/site-packages/grequests.py:60(send)
     10/1    0.001    0.000   10.754   10.754 /usr/local/lib/python3.7/site-packages/requests/sessions.py:466(request)
     10/1    0.002    0.000   10.716   10.716 /usr/local/lib/python3.7/site-packages/requests/sessions.py:617(send)
     10/1    0.001    0.000   10.713   10.713 /usr/local/lib/python3.7/site-packages/requests/adapters.py:394(send)
     10/1    0.002    0.000   10.701   10.701 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:446(urlopen)
     10/1    0.002    0.000   10.692   10.692 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:319(_make_request)
       10    0.000    0.000   10.087    1.009 /usr/local/lib/python3.7/http/client.py:1277(getresponse)
       10    0.001    0.000   10.086    1.009 /usr/local/lib/python3.7/http/client.py:289(begin)
       10    0.001    0.000   10.031    1.003 /usr/local/lib/python3.7/http/client.py:256(_read_status)
       70    0.001    0.000   10.030    0.143 {method 'readline' of '_io.BufferedReader' objects}
       10    0.001    0.000   10.028    1.003 /usr/local/lib/python3.7/socket.py:575(readinto)

    20/10    0.002    0.000   10.027    1.003 /usr/local/lib/python3.7/site-packages/urllib3/contrib/pyopenssl.py:292(recv_into)

       10    0.000    0.000   10.019    1.002 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:139(wait_for_read)
       10    0.001    0.000   10.018    1.002 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:87(poll_wait_for_socket)
       11    0.000    0.000   10.016    0.911 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:41(_retry_on_intr)
       10    0.000    0.000   10.016    1.002 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:99(do_poll)
       11   10.016    0.911   10.016    0.911 {method 'poll' of 'select.poll' objects}
     10/1    0.001    0.000    9.678    9.678 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:831(_validate_conn)
     10/1    0.002    0.000    9.678    9.678 /usr/local/lib/python3.7/site-packages/urllib3/connection.py:299(connect)
```
