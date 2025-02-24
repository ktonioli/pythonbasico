Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##Modelo de Dados do Python
>>> obj1=8
>>> id(obj1)
140709385018008
>>> obj1 = 12
>>> id(obj1)
140709385018136
>>> ##objeto imutável, o interpetrador exclui o objeto antigo e cria um novo.
>>> 
>>> L = [44, 17, 26, 35, 20]
>>> type(L)
<class 'list'>
>>> print(L)
[44, 17, 26, 35, 20]
>>> len(L)
5
>>> id(L)
1894978125440
>>> print(L[0])
44
>>> print(L[3])
35
>>> ##L[0] - índice
>>> 
>>> L[0] = 12
>>> id(L)
1894978125440
>>> print(L)
[12, 17, 26, 35, 20]
>>> print(L[0])
12
>>> 
>>> ##objeto imutável = a alteração de conteúdo implica na alteração do id númerico do objeto
>>> ##objeto mutável = a alteração de conteúdo ocorre sem a alteração do id númerico do objeto
>>> 
