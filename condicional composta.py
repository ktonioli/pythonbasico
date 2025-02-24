Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
## Condições compostas
a = 0
a > 0
False
not A > 0
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    not A > 0
NameError: name 'A' is not defined. Did you mean: 'a'?
not a > 0
True
a = 0
a = 0
a == 0
True
not a == 0
False

##and
a < 0 and b < 0
False
a < 0 and b == 1
False
a == 0 and b ==1
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a == 0 and b ==1
NameError: name 'b' is not defined
a == 0 and b == 1
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a == 0 and b == 1
NameError: name 'b' is not defined
b = 1
a < 0 and b <0
False
a < 0 and b == 1
False
a == 0 and b==1
True
a == 0 and b == 1
True
a <=0 and b <=1
True
True
True
>>> ## or
>>> a
0
>>> b
1
>>> a < 0 or b < 0
False
>>> a < 0 or b == 1
True
>>> a > 0 or b == 1
True
>>> a == 0 or b< 1
True
>>> a == 0 or b ==
SyntaxError: invalid syntax
>>> a == 0 or b ==1
True
>>> 
>>> ##comando condicional - completo
>>> a = 15
>>> b = 9
>>> c = 9
>>> b == or c a < b and a < c
SyntaxError: invalid syntax
>>> b == c or a < b and a < c
True
>>> ## primeiro é resolvido a segunda expressão (a<b and a<c) e depois o b == c ( True or false and false) = true and false = true
>>> (b == c or a < b) and a < c
False
>>> (true or false) and false
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    (true or false) and false
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> false
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    false
NameError: name 'false' is not defined. Did you mean: 'False'?
