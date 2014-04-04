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
-------------

```
import logging
import elpylog

el_log = elpylog.BulkUdp('127.0.0.1')

my_logger = logging.getLogger('test_logger')
my_logger.setLevel(logging.DEBUG)
my_logger.addHandler(el_log)

my_logger.debug('Hello world.')
```

Example Usage with `logging.config`
-----------------------------------
Your `logging.conf`:
```
[loggers]
keys = root

[handlers]
keys = elasticsearch

[formatters]
keys = default

[logger_root]
level = DEBUG
handlers = elasticsearch

[handler_elasticsearch]
class = elpylog.BulkUdp
args = ('10.42.255.53',)
formatter = default

[formatter_default]
format = %(message)s
```


Your main application:
```
import logging
import logging.config

logging.config.fileConfig("logging.conf")
logging.getLogger().debug('Hello world.')
```

