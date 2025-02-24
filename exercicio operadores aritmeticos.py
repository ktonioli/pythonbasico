Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 10
b = 25
c = 7
r = 2* A + B
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    r = 2* A + B
NameError: name 'A' is not defined. Did you mean: 'a'?
r = 2* a + b
print(r)
45
>>> r = 2*(a+b)
>>> print(r)
70
>>> 70
70
>>> r = a*b
>>> print(r)
250
>>> r = a ** b
>>> print(r)
10000000000000000000000000
>>> r= a/b
>>> print(r)
0.4
>>> r = A//B
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    r = A//B
NameError: name 'A' is not defined. Did you mean: 'a'?
>>> r = a//b
>>> print(r)
0
>>> r = a % b
>>> print(r)
10
>>> x = a +b +c
>>> print(x)
42
>>> x = (a+b) * c
>>> print(x)
245
>>> x= (a+b) / c
>>> print(x)
5.0
>>> x = (a+c) * b
>>> print(x)
425
>>> x = a//c
>>> print(x)
1
