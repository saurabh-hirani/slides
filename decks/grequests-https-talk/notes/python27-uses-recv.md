### Python2.7 uses recv

```text
STAGE=3 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh

STAGE=3 PYVERSIONS=27 PROTO=https COUNT=3 TRACE=1 ./bin/run-stages.sh > stages/03/python27/trace.txt

less stages/03/python27/trace.txt
```

#### Sample output

```text
STAGE=3 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```

```text
=============
test_grequests_python27_3: installed_module: urllib3==1.24.1
test_grequests_python27_3: installed_module: requests==2.21.0
test_grequests_python27_3: installed_module: gevent==1.4.0
test_grequests_python27_3: installed_module: grequests==0.3.0
test_grequests_python27_3: installed_module: pyopenssl==19.0.0
test_grequests_python27_3: installed_module: gevent-openssl==1.2
=============
python27_3 - START
python27_3 - Starting new HTTPS connection (1): https_server:8081
python27_3 - Starting new HTTPS connection (1): https_server:8081
python27_3 - Starting new HTTPS connection (1): https_server:8081
python27_3 - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 308
python27_3 - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 308
python27_3 - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 308
python27_3 - len(all_page_ids) = 3
python27_3 - len(valid_page_ids) = 3
python27_3 - len(invalid_page_ids) = 0
         8243 function calls (8044 primitive calls) in 1.143 seconds

   Ordered by: cumulative time
   List reduced from 562 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.144    1.144 grequests.py:103(map)
      3/1    0.000    0.000    1.143    1.143 grequests.py:60(send)
      3/1    0.000    0.000    1.143    1.143 sessions.py:466(request)
      3/1    0.000    0.000    1.125    1.125 sessions.py:617(send)
      3/1    0.000    0.000    1.123    1.123 adapters.py:394(send)
      3/1    0.000    0.000    1.116    1.116 connectionpool.py:446(urlopen)
      3/1    0.000    0.000    1.113    1.113 connectionpool.py:319(_make_request)
      3/1    0.000    0.000    1.111    1.111 httplib.py:1084(getresponse)
      3/1    0.000    0.000    1.111    1.111 httplib.py:431(begin)
     21/7    0.002    0.000    1.109    0.158 socket.py:410(readline)
      3/1    0.000    0.000    1.108    1.108 httplib.py:392(_read_status)
      3/1    0.000    0.000    1.108    1.108 pyopenssl.py:271(recv)
      3/1    0.000    0.000    1.095    1.095 SSL.py:61(recv)
      9/1    0.998    0.111    1.095    1.095 SSL.py:24(__iowait)
        3    0.000    0.000    0.030    0.010 sessions.py:426(prepare_request)
     54/6    0.003    0.000    0.016    0.003 builtins.py:72(__import__)
        3    0.000    0.000    0.016    0.005 ssl_.py:229(create_urllib3_context)
     54/6    0.005    0.000    0.015    0.003 {__import__}
      662    0.005    0.000    0.014    0.000 {isinstance}
        3    0.000    0.000    0.014    0.005 pyopenssl.py:418(set_ciphers)




python27_3 - total_time=0:00:01.162499

python27_3 - END

=============
```
