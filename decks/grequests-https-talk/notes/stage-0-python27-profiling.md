### Stage-0 Python2.7 profiling

```
python2 ./bin/test_grequests_v1.py --url https://localhost:8082/delay/1 --url-count 5 --log-level DEBUG --profile-code --profile-stats-count 20

STAGE=0 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh 2>&1 | grep 'total_time'
STAGE=0 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```
