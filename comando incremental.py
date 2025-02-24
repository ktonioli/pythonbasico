Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ## Comando de atribuição incremental
>>> A =10
>>> A = A +1
>>> print(A)
11
>>> A+ = 1 #isso equivale a fazer A = A+1
SyntaxError: invalid syntax
>>> A += 1 #isso equivale a fazer A=A+1
>>> print(A)
12
>>> 
>>> A = 10
>>> P = 4
>>> A += P
>>> ##isso equivale a fazer A = A+P
>>> print(A)
14
>>> A -=P
>>> print(A)
10
>>> A *= P
>>> print(A)
40
>>> A /= P
>>> print(A)
10.0
>>> type(A)
<class 'float'>
>>> A = 40
>>> A //= P
>>> print(A)
10
