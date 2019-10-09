### Test grequests after debug statement

```shell
python2 ./bin/test-grequests.py https 5
python3 ./bin/test-grequests.py https 5

python2 ./bin/test-grequests.py https 5
python3 ./bin/test-grequests.py https 100
```



#### Sample output

```shell
python2 ./bin/test-grequests.py https 5
```

```text
localhost - START
localhost - Starting new HTTPS connection (1): localhost:8082
localhost - Starting new HTTPS connection (1): localhost:8082
localhost - Starting new HTTPS connection (1): localhost:8082
localhost - Starting new HTTPS connection (1): localhost:8082
localhost - Starting new HTTPS connection (1): localhost:8082
localhost -
localhost - sending_request
localhost -
localhost - https://localhost:8082 "GET /delay/1?page=0 HTTP/1.1" 200 302
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
localhost - https://localhost:8082 "GET /delay/1?page=4 HTTP/1.1" 200 302
localhost -
localhost - sending_request
localhost -
localhost - https://localhost:8082 "GET /delay/1?page=3 HTTP/1.1" 200 302
localhost - END
localhost - total_time = 5.083 seconds
```

```shell
python3 ./bin/test-grequests.py https 5
```

```text
localhost - START
localhost - Starting new HTTPS connection (1): localhost:8082
localhost - Starting new HTTPS connection (1): localhost:8082
localhost - Starting new HTTPS connection (1): localhost:8082
localhost - Starting new HTTPS connection (1): localhost:8082
localhost - Starting new HTTPS connection (1): localhost:8082
localhost -
localhost - sending_request
localhost -
localhost -
localhost - sending_request
localhost -
localhost -
localhost - sending_request
localhost -
localhost -
localhost - sending_request
localhost -
localhost -
localhost - sending_request
localhost -
localhost - https://localhost:8082 "GET /delay/1?page=1 HTTP/1.1" 200 302
localhost - https://localhost:8082 "GET /delay/1?page=0 HTTP/1.1" 200 302
localhost - https://localhost:8082 "GET /delay/1?page=2 HTTP/1.1" 200 302
localhost - https://localhost:8082 "GET /delay/1?page=3 HTTP/1.1" 200 302
localhost - https://localhost:8082 "GET /delay/1?page=4 HTTP/1.1" 200 302
localhost - END
localhost - total_time = 1.102 seconds
```
