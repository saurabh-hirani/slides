### Patch urllib3

```shell
2019-10-06 20:09:05,575 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:_make_request:396 - DEBUG - https://localhost:8082 "GET /delay/1?page=0 HTTP/1.1" 200 302
```

```shell
2019-10-06 21:40:07,861 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:_make_request:400 - DEBUG - https://localhost:8082 "GET /delay/1?page=2 HTTP/1.1" 200 302
```


```shell
vim /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py
vim /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py
# Find where request is being sent
# Add debugging statement
```
