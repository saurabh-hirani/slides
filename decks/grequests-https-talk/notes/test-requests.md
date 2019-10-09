### Test requests

#### Commands

```shell
python2 ./bin/test-requests.py https 3
python3 ./bin/test-requests.py https 3
```




#### Sample output

```shell
python2 ./bin/test-requests.py https 3
```

```text
localhost - START
localhost - Starting new HTTPS connection (1): localhost:8082
localhost - https://localhost:8082 "GET /delay/1?page=0 HTTP/1.1" 200 302
localhost - Starting new HTTPS connection (1): localhost:8082
localhost - https://localhost:8082 "GET /delay/1?page=1 HTTP/1.1" 200 302
localhost - Starting new HTTPS connection (1): localhost:8082
localhost - https://localhost:8082 "GET /delay/1?page=2 HTTP/1.1" 200 302
localhost - END
localhost - total_time = 3.036 seconds
```

```shell
python3 ./bin/test-requests.py https 3
```

```text
localhost - START
localhost - Starting new HTTPS connection (1): localhost:8082
localhost - https://localhost:8082 "GET /delay/1?page=0 HTTP/1.1" 200 302
localhost - Starting new HTTPS connection (1): localhost:8082
localhost - https://localhost:8082 "GET /delay/1?page=1 HTTP/1.1" 200 302
localhost - Starting new HTTPS connection (1): localhost:8082
localhost - https://localhost:8082 "GET /delay/1?page=2 HTTP/1.1" 200 302
localhost - END
localhost - total_time = 3.088 seconds
```
