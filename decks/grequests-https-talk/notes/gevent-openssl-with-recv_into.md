### gevent-openssl with recv_into

```shell
./docker-exec.sh test_grequests_python37_4 /usr/local/bin/python

import gevent_openssl
import inspect
import json
print(json.dumps([x[0] for x in inspect.getmembers(gevent_openssl.SSL.Connection)], indent=2, default=str))
```
