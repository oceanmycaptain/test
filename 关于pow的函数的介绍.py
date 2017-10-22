def power(x,y):
	result = 1#该处只是为了后面的循环自乘。
	for i in range(y):
		result *=x
	return result
print(power(2,3))#此处用于检验power函数。
