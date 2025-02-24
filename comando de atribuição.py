Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> print(a)
10
>>> b = a
>>> type(b)
<class 'int'>
>>> c = a +10
>>> print(c)
20
>>> c = a + b
>>> print(c)
20
>>> d = a/b
>>> print(d)
1.0
>>> 
>>> e = len(b)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    e = len(b)
TypeError: object of type 'int' has no len()
>>> d = len('exemplo')
>>> print(d)
7
>>> ## len = comprimento (quantidade)
>>> type(d)
<class 'int'>
