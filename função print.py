Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print ('Olá mundo')
Olá mundo
>>> x = 26
>>> print(x)
26
>>> y = 58
>>> print(y)
58
>>> print(x, y)
26 58
>>> print(x, 'e', y)
26 e 58
>>> print('Valor de x:', x, 'Valor de y:',y)
Valor de x: 26 Valor de y: 58
>>> print('Valor de x:',x, 'e', 'Valor de y', y)
Valor de x: 26 e Valor de y 58
>>> print('Valores: x = {0} e y = {1}'.format(x,y))
Valores: x = 26 e y = 58
>>> print('Valores: x = {0} e y = {1}'.format(y,x))
Valores: x = 58 e y = 26
>>> print('Valores: y = {0} e x = {1}'.format(y,x))
Valores: y = 58 e x = 26
>>> print('Valores: x = {1} e y = {0}'.format(y,x))
Valores: x = 26 e y = 58
