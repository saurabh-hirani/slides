### Trace Python2.7 code

```shell
python2 ./bin/test_grequests_v1.py --url https://localhost:8082/delay/1 --url-count 5 --trace
less stages/00/python2.7-trace.txt

# /usr/local/lib/python2.7/site-packages/OpenSSL/SSL.py:1713:send
# /usr/local/lib/python2.7/site-packages/OpenSSL/SSL.py:1777:recv
# /usr/local/lib/python2.7/site-packages/urllib3/util/wait.py:136:wait_for_socket
```
