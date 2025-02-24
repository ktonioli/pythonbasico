Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
n = input ('Digite um número inteiro: ')
Digite um número inteiro: 37
print(n)
37
>>> f = input ('Digite um número real: ')
Digite um número real: 31.47
>>> print(f)
31.47
>>> r = n + f
>>> print(r)
3731.47
>>> type(n)
<class 'str'>
>>> type(f)
<class 'str'>
>>> print(n)
37
>>> print(f)
31.47
>>> int(n)
37
>>> flo(f)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    flo(f)
NameError: name 'flo' is not defined
>>> float(f)
31.47
>>> n = int(n)
>>> type(n)
<class 'int'>
>>> print(n)
37
>>> f = float(f)
>>> f
31.47
>>> type(f)
<class 'float'>
>>> r = n + f
>>> r
68.47
>>> r = n*f
>>> print(r)
1164.3899999999999
