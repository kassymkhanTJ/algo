# Ставим arc
Желательно чтобы путь до `arc` был `/Users/$USER/arc/...`
https://doc.yandex-team.ru/arc/setup/arc/install.html

# Cтавим oracle Version 12.2.0.1.0 
https://www.oracle.com/database/technologies/instant-client/macos-intel-x86-downloads.html
Там же скачиваем SQL*Plus Package той же версии, распаковываем в одной директории 

```
# линкуем либы оракла 
ln -s ~/instantclient_12_2/libclntsh.dylib /usr/local/lib
ln -s ~/instantclient_12_2/libclntsh.dylib.12.1 /usr/local/lib

export PATH=~/instantclient_12_2:$PATH

# клонируем проект с tnsnames
git clone git@github.yandex-team.ru:Billing/tnsnames.git

export ORACLE_HOME=/Users/kasimt/instantclient_12_2
export LD_LIBRARY_PATH=/Users/kasimt/instantclient_12_2
export DYLD_LIBRARY_PATH=/Users/kasimt/instantclient_12_2
export TNS_ADMIN=/Users/kasimt/tnsnames/

# добавляем в /etc/hosts
# 1270.0.0.1	<machine-name>

# Проверяем соединение
sqlplus bo/balalancing@DEV_BALANCE_YANDEX_RU
```

# Скачиваем конфиги
```
export BALANCE_DIR=$HOME/arc/arcadia/billing/balance
mkdir -p $BALANCE_DIR/common_config/dev
mkdir -p ~/log

rsync -a "$USER@greed-dev2h.paysys.yandex.net:/mnt/remote/greed-dev4h.paysys.yandex.net/etc/yandex/balance-common/" $BALANCE_DIR/common_config/dev
cp -p $BALANCE_DIR/balance/balance-test.cfg.in $BALANCE_DIR/balance/balance-test.cfg

# Linux
sed -i "s/<Log /<Log rotate_count=\"3\" /g" $BALANCE_DIR/balance/balance-test.cfg
sed -i "s/@BALANCE_DB@/DEV_BALANCE_YANDEX_RU/g" $BALANCE_DIR/balance/balance-test.cfg
sed -i "s:/var/log/yb/balance-test-@USER@.log:/home/$USER/log/balance-unit-tests.log:g" $BALANCE_DIR/balance/balance-test.cfg
sed -i "s:/tools/muzzle/xreports:$BALANCE_DIR/muzzle/xreports:g" $BALANCE_DIR/balance/balance-test.cfg

# MacOS
sed -i '' -e "s/<Log /<Log rotate_count=\"3\" /g" $BALANCE_DIR/balance/balance-test.cfg
sed -i '' -e "s/@BALANCE_DB@/DEV_BALANCE_YANDEX_RU/g" $BALANCE_DIR/balance/balance-test.cfg
sed -i '' -e "s:/var/log/yb/balance-test-@USER@.log:/Users/$USER/log/balance-unit-tests.log:g" $BALANCE_DIR/balance/balance-test.cfg
sed -i '' -e "s:/tools/muzzle/xreports:$BALANCE_DIR/muzzle/xreports:g" $BALANCE_DIR/balance/balance-test.cfg
```

# virtualenv
```
# ставим virtualenv
pyenv install -f 2.7.14
pyenv virtualenv 2.7.14 balance_tools_venv

# for MacOS
pyenv init - | source

# Activate venv
pyenv activate balance_tools_venv
```


====+ Site packages для virtualenv
`vim $VIRTUAL_ENV/lib/python2.7/site-packages/balance_libs.pth`
```
/Users/$USER/arc/arcadia/billing/balance
/Users/$USER/arcsymlinks
/Users/$USER/arc/arcadia/billing/balance_utils
/Users/$USER/arc/arcadia/billing/contrib/yutil/src
/Users/$USER/arc/arcadia/billing/contrib/mdswrapper/src
/Users/$USER/arc/arcadia/billing/library/python/logfeller_utils
/Users/$USER/arc/arcadia/bindings/python/inflector_lib
/Users/$USER/arc/arcadia/library/python/nirvana_api
/Users/$USER/arc/arcadia/library/python/refsclient
/Users/$USER/arc/arcadia/library/python/resource
/Users/$USER/arc/arcadia/library/python/svn_version
/Users/$USER/arc/arcadia/library/python/yenv
/Users/$USER/arc/arcadia/library/python/startrek_python_client
/Users/$USER/arc/arcadia/geobase/python/static
#/Users/$USER/arc/arcadia/contrib/python/requests
#/Users/$USER/arc/arcadia/contrib/python/six
#/Users/$USER/arc/arcadia/contrib/python/dateutil
/Users/$USER/arc/arcadia/contrib/python/arrow
#/Users/$USER/arc/arcadia/contrib/python/backports/functools_lru_cache
/Users/$USER/arc/arcadia/contrib/python/sqlalchemy
/Users/$USER/arc/arcadia/contrib/python/cx-Oracle
#/Users/$USER/arc/arcadia/contrib/python/lxml
/Users/$USER/arc/arcadia/contrib/python/qrcode
/Users/$USER/arc/arcadia/contrib/python/python-memcached
/Users/$USER/arc/arcadia/contrib/python/python-libarchive
/Users/$USER/arc/arcadia/contrib/python/zeep
/Users/$USER/arc/arcadia/contrib/python/xlwt
/Users/$USER/arc/arcadia/contrib/python/m2crypto
/Users/$USER/arc/arcadia/contrib/python/numpy
#/Users/$USER/arc/arcadia/contrib/python/pandas
#/Users/$USER/arc/arcadia/contrib/python/mako
/Users/$USER/arc/arcadia/contrib/python/num2words
#/Users/$USER/arc/arcadia/contrib/python/sqlparse
#/Users/$USER/arc/arcadia/contrib/python/simplejson
#/Users/$USER/arc/arcadia/contrib/python/jsonschema
/Users/$USER/arc/arcadia/contrib/python/blinker
#/Users/$USER/arc/arcadia/contrib/python/boto3
/Users/$USER/arc/arcadia/contrib/python/xlrd
/Users/$USER/arc/arcadia/contrib/python/retrying
#/Users/$USER/arc/arcadia/contrib/python/Jinja2
#/Users/$USER/arc/arcadia/contrib/python/enum34
#/Users/$USER/arc/arcadia/contrib/python/attrs
```

`mkdir /Users/$USER/arcsymlinks`
====+ Симлинки для аркадийных либ
```
ln -s /Users/$USER/arc/arcadia/contrib/python/attrs/attr /Users/$USER/arcsymlinks/attr
ln -s /Users/$USER/arc/arcadia/billing /Users/$USER/arcsymlinks/billing
ln -s /Users/$USER/arc/arcadia/contrib/python/certifi/certifi /Users/$USER/arcsymlinks/certifi
ln -s /Users/$USER/arc/arcadia/contrib/python/chardet/chardet /Users/$USER/arcsymlinks/chardet
ln -s /Users/$USER/arc/arcadia/contrib/python/click/click /Users/$USER/arcsymlinks/click
ln -s /Users/$USER/arc/arcadia/contrib/python/dateutil/dateutil /Users/$USER/arcsymlinks/dateutil
ln -s /Users/$USER/arc/arcadia/contrib/python/Flask/flask /Users/$USER/arcsymlinks/flask
ln -s /Users/$USER/arc/arcadia/contrib/python/functools32/functools32 /Users/$USER/arcsymlinks/functools32
ln -s /Users/$USER/arc/arcadia/contrib/python/PyHamcrest/src/hamcrest /Users/$USER/arcsymlinks/hamcrest
ln -s /Users/$USER/arc/arcadia/contrib/python/HTTPretty/httpretty /Users/$USER/arcsymlinks/httpretty
ln -s /Users/$USER/arc/arcadia/contrib/python/idna/idna /Users/$USER/arcsymlinks/idna
ln -s /Users/$USER/arc/arcadia/contrib/python/itsdangerous/itsdangerous /Users/$USER/arcsymlinks/itsdangerous
ln -s /Users/$USER/arc/arcadia/contrib/python/Jinja2/jinja2 /Users/$USER/arcsymlinks/jinja2
ln -s /Users/$USER/arc/arcadia/contrib/python/mock/mock /Users/$USER/arcsymlinks/mock
ln -s /Users/$USER/arc/arcadia/contrib/python/pyrsistent/py2/pyrsistent /Users/$USER/arcsymlinks/pyrsistent
ln -s /Users/$USER/arc/arcadia/contrib/python/requests/requests /Users/$USER/arcsymlinks/requests
ln -s /Users/$USER/arc/arcadia/contrib/python/sentry-sdk/sentry_sdk /Users/$USER/arcsymlinks/sentry_sdk
ln -s /Users/$USER/arc/arcadia/contrib/python/sqlalchemy/sqlalchemy /Users/$USER/arcsymlinks/sqlalchemy
ln -s /Users/$USER/arc/arcadia/contrib/python/timeout-decorator/timeout_decorator /Users/$USER/arcsymlinks/timeout_decorator
ln -s /Users/$USER/arc/arcadia/contrib/python/urllib3/urllib3 /Users/$USER/arcsymlinks/urllib3
ln -s /Users/$USER/arc/arcadia/yt/yt/python/yt_yson_bindings /Users/$USER/arcsymlinks/yt_yson_bindings
```

`vim requirements.txt`
====+Пакеты для pip
```
appnope==0.1.0
atomicwrites==1.4.0
attrs==20.2.0
backports.functools-lru-cache==1.6.1
backports.shutil-get-terminal-size==1.0.0
certifi==2020.6.20
chardet==3.0.4
configparser==4.0.2
contextlib2==0.6.0.post1
cx-Oracle==7.1.3
decorator==4.4.2
enum34==1.1.10
funcsigs==1.0.2
functools32==3.2.3.post2
future==0.18.2
graphviz==0.14.2
idna==2.10
importlib-metadata==2.0.0
ipython==5.10.0
ipython-genutils==0.2.0
jsonschema==3.2.0
lxml==4.6.1
Mako==1.1.3
MarkupSafe==1.1.1
more-itertools==5.0.0
nirvana-api==2.2.0.post6695484
packaging==20.4
pathlib2==2.3.5
pexpect==4.8.0
pickleshare==0.7.5
pluggy==0.13.1
prompt-toolkit==1.0.18
ptyprocess==0.6.0
py==1.9.0
Pygments==2.5.2
pyparsing==2.4.7
pyrsistent==0.16.1
pytest==4.6.11
requests==2.24.0
scandir==1.10.0
setproctitle==1.1.10
simplegeneric==0.8.1
six==1.15.0
ticket-parser2==2.4.2
traitlets==4.3.3
tvmtool-bin==1.3.6
typing==3.7.4.3
urllib3==1.25.11
wcwidth==0.2.5
Werkzeug==1.0.1
yandex-yt==0.10.3
zipp==1.2.0
```
==Устанавливаем зависимости 
`pip install -r requirements.txt -i https://pypi.yandex-team.ru/simple/`
```
ipython

import os
from butils import application

os.environ['YANDEX_XML_CONFIG'] = "/Users/$USER/arc/arcadia/billing/balance/balance/balance-test.cfg"
app = application.Application(database_id='balance')

session = app.new_session()
session.execute("select 1 from dual")
```