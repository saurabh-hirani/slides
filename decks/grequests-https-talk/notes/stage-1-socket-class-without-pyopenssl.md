### Stage-1 socket class without pyopenssl

```shell
./docker-exec.sh test_grequests_python27_1 \
/usr/local/bin/python /app/test_grequests_v1.py \
--url https://https_server:8081/delay/1 --url-count 5 \
--socket-class
```
