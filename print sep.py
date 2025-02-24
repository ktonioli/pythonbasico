Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a =
SyntaxError: invalid syntax
>>> SyntaxError: invalid syntax
SyntaxError: invalid syntax
>>> a = 12
>>> b = 19
>>> print(a,b)
12 19
>>> print(a, b, sep='-')
12-19
>>> print(a, b, sep = ',')
12,19
>>> print('um\ndois\ntrÊs')
um
dois
trÊs
>>> print('um dois três')
um dois três
>>> print('um\tdois\ttrÊs)
...       
SyntaxError: unterminated string literal (detected at line 1)
