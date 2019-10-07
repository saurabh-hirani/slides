### Docker setup

```
docker-compose --project-name test_grequests up \
               --build --force-recreate
```

#### Sample output

```
CONTAINER ID        IMAGE                          NAMES
81c3a57c00d9        mccutchen/go-httpbin:v2.1.3    test_grequests_http_server_1
00ac294f1ada        mccutchen/go-httpbin:v2.1.3    test_grequests_https_server_1
4adf2edd4f2a        test_grequests_python27_1      test_grequests_python27_1
ce2230b72ce1        test_grequests_python37_1      test_grequests_python37_1
782cfca1a0c4        test_grequests_python27_2      test_grequests_python27_2
df0318535e81        test_grequests_python37_2      test_grequests_python37_2
5fc07034d5ef        test_grequests_python27_3      test_grequests_python27_3
f6e84c9a77b7        test_grequests_python37_3      test_grequests_python37_3
d37103fae789        test_grequests_python37_4      test_grequests_python37_4
0770c8c3e201        test_grequests_python27_4      test_grequests_python27_4
```
