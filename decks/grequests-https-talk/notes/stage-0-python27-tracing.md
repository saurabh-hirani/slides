### Trace Python2.7 code

```shell
python2 ./bin/test_grequests_v1.py --url https://localhost:8082/delay/1 --url-count 10 --trace
cat stages/00/python2.7-trace.txt
```
