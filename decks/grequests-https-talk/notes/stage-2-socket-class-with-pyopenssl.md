### Stage-2 socket class with pyopenssl

```shell
./docker-exec.sh test_grequests_python27_2 \
/usr/local/bin/python /app/test_grequests_v1.py \
--url https://https_server:8081/delay/1 --url-count 10 \
--socket-class
```
