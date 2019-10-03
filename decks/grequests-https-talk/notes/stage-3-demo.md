### Stage-3

```
cat requirements.txt

./docker-exec.sh test_grequests_python27_3 \
/usr/local/bin/python /app/test_grequests_v2.py \
--log-level DEBUG \
--url https://https_server:8081/delay/1 --url-count 5 \
--profile-code --profile-stats-count 20

./docker-exec.sh test_grequests_python37_3 \
/usr/local/bin/python /app/test_grequests_v2.py \
--log-level DEBUG \
--url https://https_server:8081/delay/1 --url-count 5 \
--profile-code --profile-stats-count 20
```
