def deco (func):
	def warpper(*args,**kwargs):
		print('star')
		func(*args,**kwargs)
		print('end')
        return warpper
def myfunc(parameter):
    print('run with %s'% parameter)
myfunc('something')
	    
