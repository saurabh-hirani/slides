### Stage-2

```shell
cat requirements.txt

./docker-exec.sh test_grequests_python27_2 \
 /usr/local/bin/python /app/test_grequests_v1.py \
--log-level DEBUG \
 --url https://https_server:8081/delay/1 --url-count 10 \
 --profile-code --profile-stats-count 20

./docker-exec.sh test_grequests_python37_2 \
 /usr/local/bin/python /app/test_grequests_v1.py \
--log-level DEBUG \
 --url https://https_server:8081/delay/1 --url-count 10 \
 --profile-code --profile-stats-count 20
```
