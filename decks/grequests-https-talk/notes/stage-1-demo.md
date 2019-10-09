### Stage-1

```text
cat stages/01/python27/requirements.txt

cat stages/01/python37/requirements.txt
```

### All the below commands are equal

```text
docker exec -it test_grequests_python27_1 \
/usr/local/bin/python /app/test_grequests_v1.py \
 --log-level DEBUG \
--url https://https_server:8081/delay/1 --url-count 5
```

```text
./docker-exec.sh test_grequests_python27_1 \
 /usr/local/bin/python /app/test_grequests_v1.py \
 --log-level DEBUG \
 --url https://https_server:8081/delay/1 --url-count 5
```

```text
STAGE=1 PYVERSIONS=27 PROTO=https COUNT=5 LOG_LEVEL=DEBUG ./bin/run-stages.sh
```

### Using the following commands for readability

```text
STAGE=1 PYVERSIONS=27 PROTO=https COUNT=5 ./bin/run-stages.sh | \
grep -E '===|total_time|installed_module'

STAGE=1 PYVERSIONS=27 PROTO=https COUNT=5 LOG_LEVEL=DEBUG ./bin/run-stages.sh

STAGE=1 PYVERSIONS=37 PROTO=https COUNT=5 ./bin/run-stages.sh | \
grep -E '===|total_time|installed_module'

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
cat stages/01/python37/requirements.txt
```

```text
urllib3==1.24.1
requests==2.21.0
gevent==1.4.0
grequests==0.3.0
```

```text
STAGE=1 PYVERSIONS=27 PROTO=https COUNT=5 ./bin/run-stages.sh | \
grep -E '===|total_time|installed_module'
```

```text
=============
test_grequests_python27_1: installed_module: urllib3==1.24.1
test_grequests_python27_1: installed_module: requests==2.21.0
test_grequests_python27_1: installed_module: gevent==1.4.0
test_grequests_python27_1: installed_module: grequests==0.3.0
=============
python27_1 - total_time=0:00:01.042442
=============
```

```text
STAGE=1 PYVERSIONS=27 PROTO=https COUNT=5 ./bin/run-stages.sh
```

```text
=============
test_grequests_python27_1: installed_module: urllib3==1.24.1
test_grequests_python27_1: installed_module: requests==2.21.0
test_grequests_python27_1: installed_module: gevent==1.4.0
test_grequests_python27_1: installed_module: grequests==0.3.0
=============
python27_1 - START
python27_1 - Starting new HTTPS connection (1): https_server:8081
python27_1 - Starting new HTTPS connection (1): https_server:8081
python27_1 - Starting new HTTPS connection (1): https_server:8081
python27_1 - Starting new HTTPS connection (1): https_server:8081
python27_1 - Starting new HTTPS connection (1): https_server:8081
python27_1 - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 308
python27_1 - https://https_server:8081 "GET /delay/1?page=4 HTTP/1.1" 200 308
python27_1 - https://https_server:8081 "GET /delay/1?page=3 HTTP/1.1" 200 308
python27_1 - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 308
python27_1 - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 308
python27_1 - len(all_page_ids) = 5
python27_1 - len(valid_page_ids) = 5
python27_1 - len(invalid_page_ids) = 0

python27_1 - total_time=0:00:01.047341

python27_1 - END

=============
```

```text
STAGE=1 PYVERSIONS=37 PROTO=https COUNT=5 ./bin/run-stages.sh | \
grep -E '===|total_time|installed_module'
```

```text
=============
test_grequests_python37_1: installed_module: urllib3==1.24.1
test_grequests_python37_1: installed_module: requests==2.21.0
test_grequests_python37_1: installed_module: gevent==1.4.0
test_grequests_python37_1: installed_module: grequests==0.3.0
=============
python37_1 - total_time=0:00:01.048807
=============
```

```text
STAGE=1 PYVERSIONS=37 PROTO=https COUNT=5 ./bin/run-stages.sh
```

```text
=============
test_grequests_python37_1: installed_module: urllib3==1.24.1
test_grequests_python37_1: installed_module: requests==2.21.0
test_grequests_python37_1: installed_module: gevent==1.4.0
test_grequests_python37_1: installed_module: grequests==0.3.0
=============
python37_1 - START
python37_1 - Starting new HTTPS connection (1): https_server:8081
python37_1 - Starting new HTTPS connection (1): https_server:8081
python37_1 - Starting new HTTPS connection (1): https_server:8081
python37_1 - Starting new HTTPS connection (1): https_server:8081
python37_1 - Starting new HTTPS connection (1): https_server:8081
python37_1 - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 308
python37_1 - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 308
python37_1 - https://https_server:8081 "GET /delay/1?page=4 HTTP/1.1" 200 308
python37_1 - https://https_server:8081 "GET /delay/1?page=3 HTTP/1.1" 200 308
python37_1 - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 308
python37_1 - len(all_page_ids) = 5
python37_1 - len(valid_page_ids) = 5
python37_1 - len(invalid_page_ids) = 0

python37_1 - total_time=0:00:01.041407

python37_1 - END

=============
```
