### Stage-1

```text
cat stages/01/python27/requirements.txt

STAGE=1 PYVERSIONS=27 PROTO=https COUNT=5 ./bin/run-stages.sh | grep -E '===|total_time|installed_modules'
STAGE=1 PYVERSIONS=27 PROTO=https COUNT=5 ./bin/run-stages.sh

STAGE=1 PYVERSIONS=37 PROTO=https COUNT=5 ./bin/run-stages.sh | grep -E '===|total_time|installed_modules'
STAGE=1 PYVERSIONS=37 PROTO=https COUNT=5 ./bin/run-stages.sh
```

#### Sample output

```text
cat stages/01/python27/requirements.txt
```

```text
urllib3==1.24.1
requests==2.21.0
gevent==1.4.0
grequests==0.3.0
```

```text
STAGE=1 PYVERSIONS=27 PROTO=https COUNT=5 ./bin/run-stages.sh | grep -E '===|total_time|installed_modules'
```

```text
=============
test_grequests_python27_1: installed_modules: urllib3==1.24.1 requests==2.21.0 gevent==1.4.0 grequests==0.3.0
2019-10-07 09:43:49,269  - python27_1 - test_grequests_v1.py:main:176 - WARNING - total_time=0:00:01.256253
=============
```

```text
STAGE=1 PYVERSIONS=27 PROTO=https COUNT=5 ./bin/run-stages.sh
```

```text
=============
test_grequests_python27_1: installed_modules: urllib3==1.24.1 requests==2.21.0 gevent==1.4.0 grequests==0.3.0
2019-10-07 09:44:53,288  - python27_1 - test_grequests_v1.py:main:159 - INFO - START
2019-10-07 09:44:53,295  - python27_1 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 09:44:53,307  - python27_1 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 09:44:53,312  - python27_1 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 09:44:53,317  - python27_1 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 09:44:53,320  - python27_1 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 09:44:54,333  - python27_1 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 308
2019-10-07 09:44:54,338  - python27_1 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 308
2019-10-07 09:44:54,342  - python27_1 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 308
2019-10-07 09:44:54,344  - python27_1 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=3 HTTP/1.1" 200 308
2019-10-07 09:44:54,346  - python27_1 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=4 HTTP/1.1" 200 308
2019-10-07 09:44:54,347  - python27_1 - test_grequests_v1.py:make_requests:122 - INFO - len(all_page_ids) = 5
2019-10-07 09:44:54,347  - python27_1 - test_grequests_v1.py:make_requests:123 - INFO - len(valid_page_ids) = 5
2019-10-07 09:44:54,347  - python27_1 - test_grequests_v1.py:make_requests:124 - INFO - len(invalid_page_ids) = 0

2019-10-07 09:44:54,348  - python27_1 - test_grequests_v1.py:main:176 - WARNING - total_time=0:00:01.068423

2019-10-07 09:44:54,348  - python27_1 - test_grequests_v1.py:main:178 - INFO - END

=============
```

```text
STAGE=1 PYVERSIONS=37 PROTO=https COUNT=5 ./bin/run-stages.sh | grep -E '===|total_time|installed_modules'
```

```text
=============
test_grequests_python37_1: installed_modules: urllib3==1.24.1 requests==2.21.0 gevent==1.4.0 grequests==0.3.0
2019-10-07 09:47:13,557  - python37_1 - test_grequests_v1.py:main:176 - WARNING - total_time=0:00:01.081610
=============
```

```text
STAGE=1 PYVERSIONS=37 PROTO=https COUNT=5 ./bin/run-stages.sh
```

```text
=============
test_grequests_python37_1: installed_modules: urllib3==1.24.1 requests==2.21.0 gevent==1.4.0 grequests==0.3.0
2019-10-07 09:47:26,597  - python37_1 - test_grequests_v1.py:main:159 - INFO - START
2019-10-07 09:47:26,603  - python37_1 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 09:47:26,610  - python37_1 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 09:47:26,612  - python37_1 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 09:47:26,614  - python37_1 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 09:47:26,616  - python37_1 - connectionpool.py:_new_conn:813 - DEBUG - Starting new HTTPS connection (1): https_server:8081
2019-10-07 09:47:27,630  - python37_1 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 308
2019-10-07 09:47:27,643  - python37_1 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 308
2019-10-07 09:47:27,644  - python37_1 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=4 HTTP/1.1" 200 308
2019-10-07 09:47:27,645  - python37_1 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=3 HTTP/1.1" 200 308
2019-10-07 09:47:27,646  - python37_1 - connectionpool.py:_make_request:393 - DEBUG - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 308
2019-10-07 09:47:27,647  - python37_1 - test_grequests_v1.py:make_requests:122 - INFO - len(all_page_ids) = 5
2019-10-07 09:47:27,647  - python37_1 - test_grequests_v1.py:make_requests:123 - INFO - len(valid_page_ids) = 5
2019-10-07 09:47:27,647  - python37_1 - test_grequests_v1.py:make_requests:124 - INFO - len(invalid_page_ids) = 0

2019-10-07 09:47:27,648  - python37_1 - test_grequests_v1.py:main:176 - WARNING - total_time=0:00:01.059443

2019-10-07 09:47:27,648  - python37_1 - test_grequests_v1.py:main:178 - INFO - END

=============
```
