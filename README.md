Python nginx Log Parser
=======================

Parse nginx logs with Python.

.. image:: https://img.shields.io/pypi/v/nginxlib.svg
        :target: https://pypi.python.org/pypi/nginxlib

.. image:: https://img.shields.io/travis/briandant/nginxlib.svg
        :target: https://travis-ci.org/briandant/nginxlib

.. image:: https://readthedocs.org/projects/nginxlib/badge/?version=latest
        :target: https://nginxlib.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

* Free software: MIT license

<! -- Docs not yet published
* Documentation: https://nginxlib.readthedocs.io.
-->

This package parses nginx logs and provides a Python
object representing each log. It also has some procedures
to aggregate log data.

Inspired by: https://code.richard.do/explore/projects.

Installation 
==============

With pip:

```
$ pip install nginxlib
```

For development: 

```
$ python setup.py develop
```

Run the tests:

```
$ make test
```

Usage 
========

Given this nginx log entry: 

```
96.49.212.83 - - [16/Jun/2019:22:52:21 +0000] "GET /vs/editor/editor.main.nls.js HTTP/1.1" 200 34027 "https://3000-98358490.staging-avl.appsembler.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:67.0) Gecko/20100101 Firefox/67.0" "-"  # noqa E503
```

the `entryparse` object will behave as follows:

```
>>> from nginxparser import entryparse

>>> entry = entryparse(log_string)
>>> entry.timestamp
datetime.datetime(2019, 6, 16, 23, 54, 5, 624139)
>>> entry.url
ParseResult(scheme='https', netloc='3000-98358490.staging-avl.appsembler.com', path='', params='', query='', fragment='')
>>> entry.deploy_id
'98358490'
```



Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
