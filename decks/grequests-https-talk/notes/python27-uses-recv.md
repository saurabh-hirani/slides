### Python2.7 uses recv

```shell
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.456    1.456 /usr/local/lib/python2.7/site-packages/grequests.py:103(map)
     10/1    0.000    0.000    1.455    1.455 /usr/local/lib/python2.7/site-packages/grequests.py:60(send)
     10/1    0.001    0.000    1.455    1.455 /usr/local/lib/python2.7/site-packages/requests/sessions.py:466(request)
     10/1    0.002    0.000    1.436    1.436 /usr/local/lib/python2.7/site-packages/requests/sessions.py:617(send)
     10/1    0.001    0.000    1.434    1.434 /usr/local/lib/python2.7/site-packages/requests/adapters.py:394(send)
     10/1    0.001    0.000    1.427    1.427 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:446(urlopen)
     10/1    0.001    0.000    1.423    1.423 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:319(_make_request)
     10/1    0.000    0.000    1.422    1.422 /usr/local/lib/python2.7/httplib.py:1084(getresponse)
     10/1    0.001    0.000    1.422    1.422 /usr/local/lib/python2.7/httplib.py:431(begin)
     70/7    0.006    0.000    1.420    0.203 /usr/local/lib/python2.7/socket.py:410(readline)
     10/1    0.001    0.000    1.419    1.419 /usr/local/lib/python2.7/httplib.py:392(_read_status)

     10/1    0.000    0.000    1.419    1.419 /usr/local/lib/python2.7/site-packages/urllib3/contrib/pyopenssl.py:271(recv)
     10/1    0.000    0.000    1.406    1.406 /usr/local/lib/python2.7/site-packages/gevent_openssl/SSL.py:61(recv)
     30/1    0.976    0.033    1.406    1.406 /usr/local/lib/python2.7/site-packages/gevent_openssl/SSL.py:24(__iowait)

     10/1    0.001    0.000    0.124    0.124 /usr/local/lib/python2.7/site-packages/gevent/_socketcommon.py:382(_resolve_addr)
       10    0.001    0.000    0.088    0.009 /usr/local/lib/python2.7/site-packages/requests/sessions.py:426(prepare_request)
       10    0.001    0.000    0.073    0.007 /usr/local/lib/python2.7/site-packages/urllib3/util/ssl_.py:229(create_urllib3_context)
       10    0.001    0.000    0.062    0.006 /usr/local/lib/python2.7/site-packages/urllib3/contrib/pyopenssl.py:418(set_ciphers)
       10    0.001    0.000    0.061    0.006 /usr/local/lib/python2.7/site-packages/OpenSSL/SSL.py:1170(set_cipher_list)
       10    0.019    0.002    0.053    0.005 /usr/local/lib/python2.7/site-packages/OpenSSL/SSL.py:2007(get_cipher_list)
```
