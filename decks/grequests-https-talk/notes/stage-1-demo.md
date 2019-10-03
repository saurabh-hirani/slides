### Stage-1

```shell
cat stages/01/python27/requirements.txt

cat stages/01/python37/requirements.txt

./docker-exec.sh test_grequests_python27_1 \
 /usr/local/bin/python /app/test_grequests_v1.py \
--log-level DEBUG \
 --url https://https_server:8081/delay/1 --url-count 5 \
 --profile-code --profile-stats-count 20

./docker-exec.sh test_grequests_python37_1 \
 /usr/local/bin/python /app/test_grequests_v1.py \
--log-level DEBUG \
 --url https://https_server:8081/delay/1 --url-count 5 \
 --profile-code --profile-stats-count 20
```
