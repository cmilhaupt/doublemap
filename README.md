DoubleMap API Client
====================


This library helps you to pull data from DoubleMap.
Included is a command line utility for determining when buses will arrive and which one to get on.


[www.doublemap.com](http://www.doublemap.com/)


Installation
------------

Via source code / GitHub:

    $ git clone https://github.com/travcunn/doublemap.git doublemap
    $ cd doublemap
    $ python setup.py install


Usage
-----
```python
>>> from doublmap import DoubleMap
>>> tracker = DoubleMap()
>>>
>>> # retrieve all of the buses
>>> tracker.buses
>>> # retrieve info about route 23
>>> tracker.route_info(23)
```

