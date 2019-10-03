### Python2.7 uses recv

```shell



   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.213    1.213 /usr/local/lib/python2.7/site-packages/grequests.py:103(map)
      5/1    0.000    0.000    1.212    1.212 /usr/local/lib/python2.7/site-packages/grequests.py:60(send)
      5/1    0.000    0.000    1.212    1.212 /usr/local/lib/python2.7/site-packages/requests/sessions.py:466(request)
      5/1    0.001    0.000    1.194    1.194 /usr/local/lib/python2.7/site-packages/requests/sessions.py:617(send)
      5/1    0.000    0.000    1.191    1.191 /usr/local/lib/python2.7/site-packages/requests/adapters.py:394(send)
      5/1    0.001    0.000    1.184    1.184 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:446(urlopen)
      5/1    0.000    0.000    1.180    1.180 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:319(_make_request)
      5/1    0.000    0.000    1.178    1.178 /usr/local/lib/python2.7/httplib.py:1084(getresponse)
      5/1    0.000    0.000    1.178    1.178 /usr/local/lib/python2.7/httplib.py:431(begin)
     35/7    0.003    0.000    1.176    0.168 /usr/local/lib/python2.7/socket.py:410(readline)
      5/1    0.000    0.000    1.176    1.176 /usr/local/lib/python2.7/httplib.py:392(_read_status)
      5/1    0.000    0.000    1.175    1.175 /usr/local/lib/python2.7/site-packages/urllib3/contrib/pyopenssl.py:271(recv)
     15/3    0.978    0.065    1.167    0.389 /usr/local/lib/python2.7/site-packages/gevent_openssl/SSL.py:24(__iowait)

      5/1    0.000    0.000    1.163    1.163 /usr/local/lib/python2.7/site-packages/gevent_openssl/SSL.py:61(recv)

        5    0.001    0.000    0.046    0.009 /usr/local/lib/python2.7/site-packages/requests/sessions.py:426(prepare_request)
        5    0.000    0.000    0.026    0.005 /usr/local/lib/python2.7/site-packages/urllib3/util/ssl_.py:229(create_urllib3_context)
        5    0.000    0.000    0.023    0.005 /usr/local/lib/python2.7/site-packages/urllib3/contrib/pyopenssl.py:418(set_ciphers)
        5    0.000    0.000    0.022    0.004 /usr/local/lib/python2.7/site-packages/OpenSSL/SSL.py:1170(set_cipher_list)
        5    0.000    0.000    0.020    0.004 /usr/local/lib/python2.7/site-packages/requests/models.py:307(prepare)
     1090    0.009    0.000    0.020    0.000 {isinstance}
```
