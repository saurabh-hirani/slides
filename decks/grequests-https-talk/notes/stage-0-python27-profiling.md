### Stage-0 Python2.7 profiling

```sh
python2 ./bin/test_grequests_v1.py --url https://localhost:8082/delay/1 --url-count 10 --log-level DEBUG --profile-code --profile-stats-count 20
```
