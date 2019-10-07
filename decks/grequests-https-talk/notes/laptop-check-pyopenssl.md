#### Laptop check pyopenssl

```shell
python2 -c 'import OpenSSL'
python3 -c 'import OpenSSL'
```


#### Sample output

```shell
python2 -c 'import OpenSSL'
```

```
python3 -c 'import OpenSSL'

Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'OpenSSL'
```

