## Stage-4 after patching demo

```text
STAGE=4 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh | \
grep -E '===|total_time|installed_module'

STAGE=4 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```


#### Sample output

```text
STAGE=4 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh | \
grep -E '===|total_time|installed_module'

```

```text
=============
test_grequests_python37_4: installed_module: urllib3==1.24.1
test_grequests_python37_4: installed_module: requests==2.21.0
test_grequests_python37_4: installed_module: gevent==1.4.0
test_grequests_python37_4: installed_module: grequests==0.3.0
test_grequests_python37_4: installed_module: pyopenssl==19.0.0
test_grequests_python37_4: installed_module: gevent-openssl==1.2
=============
python37_4 - total_time=0:00:01.234369
=============
```

```text
STAGE=4 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```

```text
=============
test_grequests_python37_4: installed_module: urllib3==1.24.1
test_grequests_python37_4: installed_module: requests==2.21.0
test_grequests_python37_4: installed_module: gevent==1.4.0
test_grequests_python37_4: installed_module: grequests==0.3.0
test_grequests_python37_4: installed_module: pyopenssl==19.0.0
test_grequests_python37_4: installed_module: gevent-openssl==1.2
=============
python37_4 - START
python37_4 - Starting new HTTPS connection (1): https_server:8081
python37_4 - Starting new HTTPS connection (1): https_server:8081
python37_4 - Starting new HTTPS connection (1): https_server:8081
python37_4 - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 308
python37_4 - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 308
python37_4 - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 308
python37_4 - len(all_page_ids) = 3
python37_4 - len(valid_page_ids) = 3
python37_4 - len(invalid_page_ids) = 0
         11164 function calls (10994 primitive calls) in 1.185 seconds

   Ordered by: cumulative time
   List reduced from 738 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.186    1.186 grequests.py:103(map)
      3/1    0.000    0.000    1.185    1.185 grequests.py:60(send)
      3/1    0.000    0.000    1.185    1.185 sessions.py:466(request)
      3/1    0.000    0.000    1.160    1.160 sessions.py:617(send)
      3/1    0.000    0.000    1.158    1.158 adapters.py:394(send)
      3/1    0.000    0.000    1.151    1.151 connectionpool.py:446(urlopen)
      3/1    0.000    0.000    1.148    1.148 connectionpool.py:319(_make_request)
      3/1    0.000    0.000    1.146    1.146 client.py:1277(getresponse)
      3/1    0.000    0.000    1.146    1.146 client.py:289(begin)
      3/1    0.000    0.000    1.141    1.141 client.py:256(_read_status)
     21/7    0.000    0.000    1.141    0.163 {method 'readline' of '_io.BufferedReader' objects}
      3/1    0.000    0.000    1.141    1.141 socket.py:575(readinto)
      3/1    0.000    0.000    1.112    1.112 pyopenssl.py:292(recv_into)
      3/1    0.000    0.000    1.112    1.112 SSL.py:76(recv_into)
      9/1    0.995    0.111    1.111    1.111 SSL.py:24(__iowait)
     10/3    0.001    0.000    0.039    0.013 <frozen importlib._bootstrap>:978(_find_and_load)
     10/3    0.000    0.000    0.038    0.013 <frozen importlib._bootstrap>:948(_find_and_load_unlocked)
        3    0.000    0.000    0.032    0.011 sessions.py:426(prepare_request)
     10/4    0.001    0.000    0.032    0.008 <frozen importlib._bootstrap>:663(_load_unlocked)
        6    0.000    0.000    0.030    0.005 hub.py:684(_get_resolver)




python37_4 - total_time=0:00:01.206663

python37_4 - END

=============
```
