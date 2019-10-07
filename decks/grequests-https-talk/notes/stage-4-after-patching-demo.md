## Stage-4 after patching demo

```text
STAGE=4 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh | grep -E '===|total_time|installed_modules'
STAGE=4 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```

### Sample output

```text
STAGE=4 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh | grep -E '===|total_time|installed_modules'
```

```text
=============
test_grequests_python37_4: installed_modules: urllib3==1.24.1 requests==2.21.0 gevent==1.4.0 grequests==0.3.0 pyopenssl==19.0.0 gevent-openssl==1.2
2019-10-07 10:51:07,474  - python37_4 - test_grequests_v2.py:main:182 - WARNING - total_time=0:00:01.194025
=============
```

```text
STAGE=4 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```

```text
=============
test_grequests_python37_4: installed_modules: urllib3==1.24.1 requests==2.21.0 gevent==1.4.0 grequests==0.3.0 pyopenssl==19.0.0 gevent-openssl==1.2
2019-10-07 10:51:21,255  - python37_4 - test_grequests_v2.py:main:165 - INFO - START
2019-10-07 10:51:21,289  - python37_4 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 10:51:21,339  - python37_4 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 10:51:21,360  - python37_4 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 10:51:22,401  - python37_4 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 308
2019-10-07 10:51:22,415  - python37_4 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 308
2019-10-07 10:51:22,427  - python37_4 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 308
2019-10-07 10:51:22,433  - python37_4 - test_grequests_v2.py:make_requests:128 - INFO - len(all_page_ids) = 3
2019-10-07 10:51:22,434  - python37_4 - test_grequests_v2.py:make_requests:129 - INFO - len(valid_page_ids) = 3
2019-10-07 10:51:22,434  - python37_4 - test_grequests_v2.py:make_requests:130 - INFO - len(invalid_page_ids) = 0
         11160 function calls (10985 primitive calls) in 1.177 seconds

   Ordered by: cumulative time
   List reduced from 742 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.178    1.178 /usr/local/lib/python3.7/site-packages/grequests.py:103(map)
      3/1    0.000    0.000    1.177    1.177 /usr/local/lib/python3.7/site-packages/grequests.py:60(send)
      3/1    0.000    0.000    1.177    1.177 /usr/local/lib/python3.7/site-packages/requests/sessions.py:466(request)
      3/1    0.000    0.000    1.150    1.150 /usr/local/lib/python3.7/site-packages/requests/sessions.py:617(send)
      3/1    0.000    0.000    1.148    1.148 /usr/local/lib/python3.7/site-packages/requests/adapters.py:394(send)
      3/1    0.000    0.000    1.142    1.142 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:446(urlopen)
      3/1    0.000    0.000    1.138    1.138 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:319(_make_request)
      3/1    0.000    0.000    1.136    1.136 /usr/local/lib/python3.7/http/client.py:1277(getresponse)
      3/1    0.000    0.000    1.136    1.136 /usr/local/lib/python3.7/http/client.py:289(begin)
      3/1    0.000    0.000    1.132    1.132 /usr/local/lib/python3.7/http/client.py:256(_read_status)
     21/7    0.000    0.000    1.132    0.162 {method 'readline' of '_io.BufferedReader' objects}
      3/1    0.000    0.000    1.132    1.132 /usr/local/lib/python3.7/socket.py:575(readinto)

      3/1    0.000    0.000    1.103    1.103 /usr/local/lib/python3.7/site-packages/urllib3/contrib/pyopenssl.py:292(recv_into)
      3/1    0.000    0.000    1.103    1.103 /usr/local/lib/python3.7/site-packages/gevent_openssl/SSL.py:76(recv_into)
      9/1    0.984    0.109    1.102    1.102 /usr/local/lib/python3.7/site-packages/gevent_openssl/SSL.py:24(__iowait)

     10/3    0.001    0.000    0.039    0.013 <frozen importlib._bootstrap>:978(_find_and_load)
     10/3    0.001    0.000    0.038    0.013 <frozen importlib._bootstrap>:948(_find_and_load_unlocked)
        3    0.000    0.000    0.033    0.011 /usr/local/lib/python3.7/site-packages/requests/sessions.py:426(prepare_request)
     10/4    0.001    0.000    0.032    0.008 <frozen importlib._bootstrap>:663(_load_unlocked)
     12/4    0.000    0.000    0.030    0.008 <frozen importlib._bootstrap>:211(_call_with_frames_removed)




2019-10-07 10:51:22,443  - python37_4 - test_grequests_v2.py:main:182 - WARNING - total_time=0:00:01.194834

2019-10-07 10:51:22,443  - python37_4 - test_grequests_v2.py:main:184 - INFO - END

=============

```
