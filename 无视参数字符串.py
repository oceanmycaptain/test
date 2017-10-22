Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def myfirstfunction():
	print('看尽人间雪花落')

	
>>> myfirstfunction
<function myfirstfunction at 0x02C436A8>
>>> list(myfirstfunction)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    list(myfirstfunction)
TypeError: 'function' object is not iterable
>>> myfirstfunction()
看尽人间雪花落
>>> def mysecondfunction(name1,name2):
	print(name1+name2)

	
>>> mysecondfunction(2,3)
5
>>> def add(a,b):
	c=a+b
	print(c)

	
>>> add(4,5)
9
>>> def mythirdfunction():
	print(+'方知春日不复存')

	
>>> mythirdfunction('以下')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    mythirdfunction('以下')
TypeError: mythirdfunction() takes 0 positional arguments but 1 was given
>>> def mythirdfunction(a):
	print(a+'方知春日不复存')

	
>>> mythirdfunction('以下')
以下方知春日不复存
>>> def sum(x):
	result = 0
	for each in x:
		if (type(each) == int) or (type(each) == float):
			result += each
		else:
			continue
	return result
print(sum([1,2.1,2.3,'a','1',True]))
SyntaxError: invalid syntax
>>> def sum(x):
	result = 0
	for each in x:
		if (type(each) == int) or (type(each) == float):
			result += each
		else:
			continue
	return result
    print(sum([1,2.1,2.3,'a','1',True]))
    
SyntaxError: unindent does not match any outer indentation level
>>> 
