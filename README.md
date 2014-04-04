elpylog 
=======
Python library for sending events to Elasticsearch over its bulk UDP api, in a logstash compatible fashion.


Install
-------
```
git clone https://github.com/ondergetekende/elpylog.git
easy_install elpylog
```

Example Usage
-------

```
import logging
import elpylog

el_log = elpylog.BulkUdp('127.0.0.1')

my_logger = logging.getLogger('test_logger')
my_logger.setLevel(logging.DEBUG)
my_logger.addHandler(el_log)

my_logger.debug('Hello world.')
```

