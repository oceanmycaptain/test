import urllib.request#用于访问网址
response = urllib.request.urlopen('http://www.fishc.com/')
html = response.read()
print(html)#此时往往打印出来的是二进制的方法编码
html = html.decode('utf-8')
#这是用于改变我们的之前打印的编码，我们可以按自己需要的改变编码
print(html)
#此时我们打印出来的网址内容就和浏览器的相同，如果我们使用的是浏览器相对应的编码。
