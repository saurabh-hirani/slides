## Stage-4 after patching demo

```shell
./docker-exec.sh test_grequests_python37_4 \
   /usr/local/bin/python /app/test_grequests_v2.py \
   --url https://https_server:8081/delay/1 --url-count 5 \
   --log-level DEBUG --profile-code --profile-stats-count 20
```

```shell

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.490    1.490 /usr/local/lib/python3.7/site-packages/grequests.py:103(map)
     10/1    0.000    0.000    1.489    1.489 /usr/local/lib/python3.7/site-packages/grequests.py:60(send)
     10/1    0.001    0.000    1.489    1.489 /usr/local/lib/python3.7/site-packages/requests/sessions.py:466(request)
     10/1    0.002    0.000    1.461    1.461 /usr/local/lib/python3.7/site-packages/requests/sessions.py:617(send)
     10/1    0.001    0.000    1.459    1.459 /usr/local/lib/python3.7/site-packages/requests/adapters.py:394(send)
     10/1    0.001    0.000    1.452    1.452 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:446(urlopen)
     10/1    0.001    0.000    1.449    1.449 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:319(_make_request)
     10/1    0.000    0.000    1.447    1.447 /usr/local/lib/python3.7/http/client.py:1277(getresponse)
     10/1    0.001    0.000    1.447    1.447 /usr/local/lib/python3.7/http/client.py:289(begin)
     10/1    0.001    0.000    1.443    1.443 /usr/local/lib/python3.7/http/client.py:256(_read_status)
     70/7    0.001    0.000    1.443    0.206 {method 'readline' of '_io.BufferedReader' objects}
     10/1    0.001    0.000    1.443    1.443 /usr/local/lib/python3.7/socket.py:575(readinto)

     10/1    0.001    0.000    1.409    1.409 /usr/local/lib/python3.7/site-packages/urllib3/contrib/pyopenssl.py:292(recv_into)
     10/1    0.001    0.000    1.409    1.409 /usr/local/lib/python3.7/site-packages/gevent_openssl/SSL.py:76(recv_into)
     30/1    0.978    0.033    1.408    1.408 /usr/local/lib/python3.7/site-packages/gevent_openssl/SSL.py:24(__iowait)

       10    0.001    0.000    0.081    0.008 /usr/local/lib/python3.7/site-packages/requests/sessions.py:426(prepare_request)
       10    0.001    0.000    0.066    0.007 /usr/local/lib/python3.7/site-packages/requests/sessions.py:690(merge_environment_settings)
       10    0.001    0.000    0.064    0.006 /usr/local/lib/python3.7/site-packages/urllib3/util/ssl_.py:229(create_urllib3_context)
       10    0.000    0.000    0.061    0.006 /usr/local/lib/python3.7/site-packages/requests/utils.py:755(get_environ_proxies)
      560    0.012    0.000    0.053    0.000 /usr/local/lib/python3.7/_collections_abc.py:742(__iter__)
```
