### Python2.7 HTTP Demo

```shell
python2 ./bin/test-grequests.py
python2 ./bin/test_grequests_v1.py --url http://localhost:8081/delay/1 --url-count 5 --log-level DEBUG --profile-code --profile-stats-count 20
python2 ./bin/test_grequests_v1.py --url http://localhost:8081/delay/0.1 --url-count 50 --log-level DEBUG --profile-code --profile-stats-count 20
```
