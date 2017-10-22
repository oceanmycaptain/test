#关于python中的读取文件的注意事项。
file1 = open('C:\windows\temp\readme.txt',r)
#此时的该文本会报错，会报错是因为在字符串中，我们约定“\t”
#和“\r”分别表示“横向制表符（tab）”和“回车符”，因此不会
#按照我们的计划路径打开文件。
我们可以用以下方式来解决该问题
file1 = open(r'C:\windows\temp\readme.txt','r')
#只是需要使用原始字符串操作符（R或r）即可。
