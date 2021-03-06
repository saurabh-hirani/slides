To view in Chrome - install the markdown viewer plugin - https://chrome.google.com/webstore/detail/markdown-viewer/ckkdlimhmcjmikdlpkmbgfkaikojcbjk?hl=en


### Table of Contents

* [Local setup](#local-setup)
* [Python2.7 HTTP Demo](#python27-http-demo)
* [Python2.7 HTTPS Demo](#python27-https-demo)
* [Python3.7 HTTP Demo](#python37-http-demo)
* [Python3.7 HTTPS Demo](#python37-https-demo)
* [Monkey patching demo](#monkey-patching-demo)
* [Stage-0](#stage-0)
* [Stage-1](#stage-1)
* [Compare Stage-0 and Stage-1](#compare-stage-0-and-stage-1)
* [Stage-2](#stage-2)
* [Why is pyopenssl making code slow?](#why-is-pyopenssl-making-code-slow)
* [Verify monkey patching in Stage-1 - without pyopenssl](#verify-monkey-patching-in-stage-1---without-pyopenssl)
* [Verify monkey patching in Stage-2 - with pyopenssl](#verify-monkey-patching-in-stage-2---with-pyopenssl)
* [Stage-1 socket class](#stage-1-socket-class)
* [Stage-2 socket class](#stage-2-socket-class)

### Local setup

```shell
./server/run_http_server.sh
./server/run_https_server.sh
docker-compose --project-name test_grequests up \
               --build --force-recreate
```

### Python2.7 HTTP Demo

```shell
python2 ./bin/test_grequests_v1.py --url http://localhost:8081/delay/1 --url-count 5
python2 ./bin/test_grequests_v1.py --url http://localhost:8081/delay/1 --url-count 50
```

### Python2.7 HTTPS Demo

```shell
python2 ./bin/test_grequests_v1.py --url https://localhost:8082/delay/1 --url-count 5
python2 ./bin/test_grequests_v1.py --url https://localhost:8082/delay/0.1 --url-count 50
```

### Python3.7 HTTP Demo

```shell
python3 ./bin/test_grequests_v1.py --url http://localhost:8081/delay/1 --url-count 5
```

### Python3.7 HTTPS Demo

```shell
python3 ./bin/test_grequests_v1.py --url https://localhost:8082/delay/1 --url-count 5
python3 ./bin/test_grequests_v1.py --url https://localhost:8082/delay/0.1 --url-count 50
```

### Monkey patching demo

```
python

import inspect
import socket
inspect.getsourcefile(socket.ssl) # should output '/usr/local/Cellar/python@2/2.7.15_3/Frameworks/Python.framework/Versions/2.7/lib/python2.7/socket.py'
exit()

python

from gevent import monkey
monkey.patch_all()
import inspect
import socket
inspect.getsourcefile(socket.ssl) # should output '/usr/local/lib/python2.7/site-packages/gevent/_socket2.py'
import gevent._hub_primitives
gevent._hub_primitives.__file__ # should output /usr/local/lib/python2.7/site-packages/gevent/__hub_primitives.so

vim '/usr/local/lib/python2.7/site-packages/gevent/_socket2.py'
# grep wait
```

```
cd monkey_patching_demo
cat mysocket.py
cat patched_socket.py
cat call_mysocket.py
python call_mysocket.py
cat patch_and_call_mysocket.py
python patch_and_call_mysocket.py
cat patcher.py
```

### Stage-0

```shell
python2 ./bin/test_grequests_v1.py --url https://localhost:8082/delay/1 --url-count 5
python3 ./bin/test_grequests_v1.py --url https://localhost:8082/delay/1 --url-count 5
```

### Stage-1

```shell
cat requirements.txt

./docker-exec.sh test_grequests_python27_1 \
/usr/local/bin/python /app/test_grequests_v2.py \
--log-level DEBUG \
--url https://https_server:8081/delay/1 --url-count 5

./docker-exec.sh test_grequests_python37_1 \
/usr/local/bin/python /app/test_grequests_v2.py \
--log-level DEBUG \
--url https://https_server:8081/delay/1 --url-count 5

./docker-exec.sh test_grequests_python27_1 \
 /usr/local/bin/python /app/test_grequests_v2.py \
 --url https://https_server:8081/delay/1 --url-count 5 \
 --profile-code --profile-stats-count 20

./docker-exec.sh test_grequests_python37_1 \
 /usr/local/bin/python /app/test_grequests_v2.py \
 --url https://https_server:8081/delay/1 --url-count 5 \
 --profile-code --profile-stats-count 20
```

### Compare Stage-0 and Stage-1

```
vim /usr/local/lib/python2.7/site-packages/urllib3/util/wait.py
```

### Stage-2

```shell
cat requirements.txt

./docker-exec.sh test_grequests_python27_2 \
/usr/local/bin/python /app/test_grequests_v2.py \
--log-level DEBUG \
--url https://https_server:8081/delay/1 --url-count 5

./docker-exec.sh test_grequests_python37_2 \
/usr/local/bin/python /app/test_grequests_v2.py \
--log-level DEBUG \
--url https://https_server:8081/delay/1 --url-count 5

./docker-exec.sh test_grequests_python27_2 \
 /usr/local/bin/python /app/test_grequests_v2.py \
 --url https://https_server:8081/delay/1 --url-count 5 \
 --profile-code --profile-stats-count 20

./docker-exec.sh test_grequests_python37_2 \
 /usr/local/bin/python /app/test_grequests_v2.py \
 --url https://https_server:8081/delay/1 --url-count 5 \
 --profile-code --profile-stats-count 20
```

### Why is pyopenssl making code slow?

```shell
./docker-exec.sh test_grequests_python27_2 bash

vim /usr/local/lib/python2.7/site-packages/requests/__init__.py
# grep pyopenssl

vim /usr/local/lib/python2.7/site-packages/urllib3/contrib/pyopenssl.py
# read heading documentation
# grep inject_into_urllib3
```

 ### Verify monkey patching in Stage-1 - without pyopenssl

```shell
./docker-exec.sh test_grequests_python27_1 /usr/local/bin/python

from __future__ import print_function
import gevent
from gevent import monkey
monkey.patch_all()
import urllib3
print(urllib3.util.ssl_.SSLContext) # should output <class 'gevent._sslgte279.SSLContext'>
exit()

from __future__ import print_function
import grequests
import urllib3
print(urllib3.util.ssl_.SSLContext) # should output <class 'gevent._sslgte279.SSLContext'>
exit()
```

### Verify monkey patching in Stage-2 - with pyopenssl

```shell
./docker-exec.sh test_grequests_python27_2 /usr/local/bin/python

from __future__ import print_function
import gevent
from gevent import monkey
monkey.patch_all()
import urllib3
print(urllib3.util.ssl_.SSLContext) # should output <class 'gevent._sslgte279.SSLContext'>
exit()

./docker-exec.sh test_grequests_python27_2 /usr/local/bin/python

from __future__ import print_function
import grequests
import urllib3
print(urllib3.util.ssl_.SSLContext) # <class 'urllib3.contrib.pyopenssl.PyOpenSSLContext'>
exit()

./docker-exec.sh test_grequests_python27_2 bash
# grep monkey
```

### Stage-1 socket class

```shell
./docker-exec.sh test_grequests_python27_1 \
/usr/local/bin/python /app/test_grequests_v2.py \
--url https://https_server:8081/delay/1 --url-count 5 \
--socket-class
```

### Stage-2 socket class

```shell
./docker-exec.sh test_grequests_python27_2 \
/usr/local/bin/python /app/test_grequests_v2.py \
--url https://https_server:8081/delay/1 --url-count 5 \
--socket-class
```
