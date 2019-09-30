## Stage-4 before patching demo

```shell
./docker-exec.sh test_grequests_python37_4 \
   /usr/local/bin/python /app/test_grequests_v2.py \
   --url https://https_server:8081/delay/1 --url-count 10 \
   --log-level DEBUG --profile-code --profile-stats-count 20
```
