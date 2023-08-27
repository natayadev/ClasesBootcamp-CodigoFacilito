# Multi Maths

## About package

Package for arithmetic, geometry y statistics


### Install with pip3

```
pip install multi-maths

or

pip3 install multi-maths
```


### Using from console

```
python -m multi_maths.cli ari add 2 3 -l en -r text
>>> 5.0
```

```
python -m multi_maths.cli ari add 2 3 7
>>> 12.0
```


### Init the class: the variable "response" on "digit" value returns only value:

```
from multi_maths.core import Core

core = Core()
core.set_lang('en')  # en, es
core.set_response('digit')  # digit, text
print(core.run('ari', 'add', (2, 3, 4)))
9.0
```


### Init the class: the variable "response" on "text" value returns value inside legend:

```
from multi_maths.core import Core

core = Core()
core.set_lang('en')  # en, es
core.set_response('text')  # digit, text
```


## Arithmetic
```
print(core.run('ari', 'add', (2, 3, 4)))
The addition result is: 9.0
```

```
print(core.run('ari', 'sub', (4, 3)))
The subtraction result is: 1.0
```

```
print(core.run('ari', 'mul', (3, 3, 2)))
The multiplication result is: 18.0
```

```
print(core.run('ari', 'div', (9, 3)))
The division result is: 3.0
```

```
print(core.run('ari', 'mod', (21, 200)))
The modulus result is: 42.0
```

```
print(core.run('ari', 'mod', (32, 517)))
The modulus result is: 165.44
```

```
print(core.run('ari', 'exp', (3, 3)))
The exponentiation result is: 27.0
```

```
print(core.run('ari', 'flo', (9, 3)))
The floor division result is: 3.0
```


## Geometry

```
print(core.run('geo', 'ca', (4,)))
The circle area result is: 50.26548245743669
```

```
print(core.run('geo', 'cc', (5,)))
The circle circumference result is: 31.41592653589793
```

```
print(core.run('geo', 'ta', (5,5)))
The triangle area result is: 12.5
```

```
print(core.run('geo', 'tp', (5, 5, 5)))
The triangle perimeter result is: 5.0
```

```
print(core.run('geo', 'sa', (5, 5)))
The square area result is: 25.0
```

```
print(core.run('geo', 'sp', (5,)))
The square perimeter result is: 20.0
```

```
print(core.run('geo', 'ra', (4, 2)))
The rectangle area result is: 8.0
```

```
print(core.run('geo', 'rp', (4, 2)))
The rectangle perimeter result is: 12.0
```

```
print(core.run('geo', 'pa', (4, 3)))
The parallelogram area result is: 12.0
```

```
print(core.run('geo', 'pp', (4, 3)))
The parallelogram perimeter result is: 14.0
```


## Statistics

```
print(core.run('stat', 'sd', (data_list,)))
The standard deviation result is: 12.739141034061687
```

```
print(core.run('stat', 'sd', (data_list, 7)))
The standard deviation result is: 12.739141034061687
```

```
print(core.run('stat', 'mean', (data_list,)))
The mean result is: 17.5
```

```
print(core.run('stat', 'med', (data_list,)))
The median result is: 14.0
```

```
print(core.run('stat', 'mode', (data_list,)))
The mode result is: 8
```

## Repository

* [Class 03 Challenge's Repository](https://github.com/gsmx64/python-adv-bootcamp-cf/tree/main/class03/challenge)
