Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 50
>>> y = 12 + 38
>>> z = 100 - 50
>>> id(x)
140709385019352
>>> id(y)
140709385019352
>>> id(z)
140709385019352
>>> print(x,y,z)
50 50 50
>>> z = 90
>>> id(z)
140709385020632
>>> 
