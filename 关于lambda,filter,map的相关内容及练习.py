Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> count = 5
>>> def myfun():
	count = 10
	print(count)

	
>>> myfun
<function myfun at 0x02B826A8>
>>> myfun()
10
>>> count
5
>>> def fun1():
	print('调用函数fun1--')
	def fun2():
	    print('调用函数fun2———')
	fun2()

	
>>> fun1()
调用函数fun1--
调用函数fun2———
>>> def FunX(x):
	def FunY(y):
		return x*y
	return FunY

>>> FunX(4)(6)
24
>>> i=FunX(8)
>>> i
<function FunX.<locals>.FunY at 0x02B8A078>
>>> type(i)
<class 'function'>
>>> i(5)
40
>>> def FunX(x):
	def FunY(y):
		return x*y
	return FunX

>>> FunX(5)(6)
<function FunX at 0x02B8A0C0>
>>> FunY(5)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    FunY(5)
NameError: name 'FunY' is not defined
>>> def FunX(x):
	def FunY(y):
		return x*y
	return FunY

>>> FunX(6)(7)
42
>>> def FunX(x):
	def FunY(y):
		return x*y
	return FunY()

>>> FunX(5)(5)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    FunX(5)(5)
  File "<pyshell#35>", line 4, in FunX
    return FunY()
TypeError: FunY() missing 1 required positional argument: 'y'
>>> def FunX(x):
	def FunY(y):
		return x*y
	return FunY

>>> FunX(2)
<function FunX.<locals>.FunY at 0x02B8A0C0>
>>> FunX(2)(5)
10
>>> help(filter)
Help on class filter in module builtins:

class filter(object)
 |  filter(function or None, iterable) --> filter object
 |  
 |  Return an iterator yielding those items of iterable for which function(item)
 |  is true. If function is None, return the items that are true.
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.

>>> filter(None,[1,0,False,True])
<filter object at 0x02B94510>
>>> list(filter(None,[1,0,False,True]))
[1, True]
>>> def add(x):
	return x%2

>>> temp = range(10)
>>> show = filter(add,temp)
>>> list(show)
[1, 3, 5, 7, 9]
>>> list(filter(lambda x:x%2,range(10)))
[1, 3, 5, 7, 9]
>>> lambda x: range(10)
<function <lambda> at 0x02B8AF60>
>>> list(lambda x: range(10))
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    list(lambda x: range(10))
TypeError: 'function' object is not iterable
>>> a=[lambda x: range(10)]
>>> a
[<function <lambda> at 0x02B8AF18>]
>>> list(a)
[<function <lambda> at 0x02B8AF18>]
>>> list[a]
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    list[a]
TypeError: 'type' object is not subscriptable
>>> lambda x: range(10)
<function <lambda> at 0x02B8AE40>
>>> type(lambda x: range(10))
<class 'function'>
>>> list(filter(lambda x:x%2,range(10)))
[1, 3, 5, 7, 9]
>>> list(lambda x:x%2,range(10))
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    list(lambda x:x%2,range(10))
TypeError: list() takes at most 1 argument (2 given)
>>> a=[lambda x:x%2,range(10)]
>>> a
[<function <lambda> at 0x02B8AFA8>, range(0, 10)]
>>> range(10)
range(0, 10)
>>> type(a)
<class 'list'>
>>> a=lambda x:range(10)
>>> a
<function <lambda> at 0x02B8AF18>
>>> for b in a:
	print(b)

	
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    for b in a:
TypeError: 'function' object is not iterable
>>> a=lambda x: x+=2
SyntaxError: invalid syntax
>>> a=lambda x: x*=x
SyntaxError: invalid syntax
>>> a=lambda x: x*==2
SyntaxError: invalid syntax
>>> a=lambda x:'yes' if x==1 else 'no'
>>> a(0)
'no'
>>> a=lambda x:x%2
>>> a(45)
1
>>> a(2)
0
>>> a=lambda (x,y):
	
SyntaxError: invalid syntax
>>> a=lambda x,y: x*y
>>> a(1,6)
6
>>> a=lambda x: x=x+2
SyntaxError: can't assign to lambda
>>> a=lambda x: x+x
>>> a(10)
20
>>> list(map(lambda x: x % 2,range(10)))
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
>>> list(map(lambda x: x*2,range(10)))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> list(map(lambda x:range(10)))
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    list(map(lambda x:range(10)))
TypeError: map() must have at least two arguments.
>>> list(filter(lambda x:range(10)))
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    list(filter(lambda x:range(10)))
TypeError: filter expected 2 arguments, got 1
>>> a=lambda x:range(10)
>>> a
<function <lambda> at 0x02BA8390>
>>> a[2]
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    a[2]
TypeError: 'function' object is not subscriptable
>>> a(2)
range(0, 10)
>>> a(3)
range(0, 10)
>>> a(100)
range(0, 10)
>>> a=(list(lambda x:x%1,range(10)))
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    a=(list(lambda x:x%1,range(10)))
TypeError: list() takes at most 1 argument (2 given)
>>> a=(list(map(lambda x:x%1,range(10))))
>>> a
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> a=(list(map(lambda x:x%2,range(10))))
>>> 
>>> a
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
>>> 10%1
0
>>> 35%2
1
>>> print range(10)
SyntaxError: invalid syntax
>>> x=range(10)
>>> print(x)
range(0, 10)
>>> a=map(lambda x,y:x**y,[1,23,45,6],[3,45,67,3])
>>> a
<map object at 0x02B94CB0>
>>> print(a)
<map object at 0x02B94CB0>
>>> print map(lambda x,y:x**y,[1,23,45,6],[3,45,67,3])
SyntaxError: invalid syntax
>>> print(map(lambda x,y:x**y,[1,23,45,6],[3,45,67,3]))
<map object at 0x02B94E10>
>>> list(map(lambda x,y:x**y,[1,23,45,6],[3,45,67,3]))
[1, 18956258430116202791319715713277227626159289499745290235663543, 582422873843435732243403659008236909175319421543815500182225909081156108026977591407558065839111804962158203125, 216]
>>> list(map(lambda x,y:x**y,[1,3,4,6],[3,6,5,3]))
[1, 729, 1024, 216]
>>> print(map(lambda x,y:x**y,[1,3,4,6],[3,6,5,3]))
<map object at 0x02B94E10>
>>> map(5,6,7)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    map(5,6,7)
TypeError: 'int' object is not iterable
>>> map(int,(1,2,3))
<map object at 0x02B94D30>
>>> list[map(int,(1,2,3))]
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    list[map(int,(1,2,3))]
TypeError: 'type' object is not subscriptable
>>> list(map(int,(1,2,3)))
[1, 2, 3]
>>> 
