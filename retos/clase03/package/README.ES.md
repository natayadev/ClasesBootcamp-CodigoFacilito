# Multi Maths

## Sobre el paquete

Módulo de funciones aritméticas, geometría y estadísticas


### Instalar con pip3

```
pip install multi-maths

o

pip3 install multi-maths
```


### Uso desde la consola

```
python -m multi_maths.cli ari add 2 3 -l es -r text
>>> 5.0
```

```
python -m multi_maths.cli ari add 2 3 7
>>> 12.0
```


### Iniciar la clase: la variable "response" en valor "digit" retorna solamente el valor:

```
from multi_maths.core import Core

core = Core()
core.set_lang('es')  # en, es
core.set_response('digit')  # digit, text
print(core.run('ari', 'add', (2, 3, 4)))
9.0
```


### Iniciar la clase: la variable "response" en valor "text" retorna valor con leyenda:

```
from multi_maths.core import Core

core = Core()
core.set_lang('es')  # en, es
core.set_response('text')  # digit, text
```


## Aritmética
```
print(core.run('ari', 'add', (2, 3, 4)))
El resultado de la suma es: 9.0
```

```
print(core.run('ari', 'sub', (4, 3)))
El resultado de la resta es: 1.0
```

```
print(core.run('ari', 'mul', (3, 3, 2)))
El resultado de la multiplicación es: 18.0
```

```
print(core.run('ari', 'div', (9, 3)))
El resultado de la división es: 3.0
```

```
print(core.run('ari', 'mod', (21, 200)))
El resultado del porcentaje es: 42.0
```

```
print(core.run('ari', 'mod', (32, 517)))
El resultado del porcentaje es: 165.44
```

```
print(core.run('ari', 'exp', (3, 3)))
El resultado de la potencia es: 27.0
```

```
print(core.run('ari', 'flo', (9, 3)))
El resultado de la raíz cuadrada es: 3.0
```


## Geometría

```
print(core.run('geo', 'ca', (4,)))
El resultado del área del círculo es: 50.26548245743669
```

```
print(core.run('geo', 'cc', (5,)))
El resultado de la circumferencia del círculo es: 31.41592653589793
```

```
print(core.run('geo', 'ta', (5,5)))
El resultado del área del triángulo es: 12.5
```

```
print(core.run('geo', 'tp', (5, 5, 5)))
El resultado del perímetro del triángulo es: 5.0
```

```
print(core.run('geo', 'sa', (5, 5)))
El resultado del área del cuadrado es: 25.0
```

```
print(core.run('geo', 'sp', (5,)))
El resultado del perímetro del cuadrado es: 20.0
```

```
print(core.run('geo', 'ra', (4, 2)))
El resultado del área del rectángulo es: 8.0
```

```
print(core.run('geo', 'rp', (4, 2)))
El resultado del perímetro del rectángulo es: 12.0
```

```
print(core.run('geo', 'pa', (4, 3)))
El resultado del área del paralelogramo es: 12.0
```

```
print(core.run('geo', 'pp', (4, 3)))
El resultado del perímetro del paralelogramo es: 14.0
```


## Estadística

```
print(core.run('stat', 'sd', (data_list,)))
El resultado de la desviación estándar es: 12.739141034061687
```

```
print(core.run('stat', 'sd', (data_list, 7)))
El resultado de la desviación estándar es: 12.739141034061687
```

```
print(core.run('stat', 'mean', (data_list,)))
El resultado de la media es: 17.5
```

```
print(core.run('stat', 'med', (data_list,)))
El resultado de la mediana es: 14.0
```

```
print(core.run('stat', 'mode', (data_list,)))
El resultado de la moda es: 8
```


## Repositorio

* [Repositorio Reto Clase 03](https://github.com/gsmx64/python-adv-bootcamp-cf/tree/main/class03/challenge)
