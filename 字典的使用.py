Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dict1 = {'李宁':'一切皆有可能'，'耐克':'Just do it','阿迪达斯':'Impossible is noting','34':'hello world'}
SyntaxError: invalid character in identifier
>>> dict1 = {'李宁':'一切皆有可能','耐克':'Just do it','阿迪达斯':'Impossible is noting','34':'hello world'}
>>> print('34:',dict1['34'])
34: hello world
>>> print('李宁:',dict1['李宁'])
李宁: 一切皆有可能
>>> #上面为字典的使用和引用方法
