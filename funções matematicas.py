Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
## Funções Matemáticas
# 1º from math import sqrt
import math
##importando a biblioteca inteira
>>> math.sqrt(49)
7.0
>>> math.exp(49)
1.9073465724950998e+21
>>> math.sqrt(81)
9.0
>>> math.exp(81)
1.5060973145850306e+35
>>> math.pi
3.141592653589793
>>> math.sin(45)
0.8509035245341184
>>> math.sin(math.pi / 2)
1.0
>>> math.cos(math.pi / 2)
6.123233995736766e-17
>>> 0.0000
KeyboardInterrupt
>>> c = math.cos(math.pi / 2)
>>> c
6.123233995736766e-17
>>> r = round(c)
>>> r
0
>>> r = round(c, 3)
>>> r
0.0
>>> r = round(c, 10)
>>> r
0.0
>>> c = 18.7142999
>>> r = round(c, 4)
>>> r
18.7143
>>> 18.7143
18.7143
>>> c = 18.71458999
>>> r= round(c, 3)
>>> r
18.715
