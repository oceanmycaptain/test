f = open('F:/双人相声.txt')
甲 = []#声明为空列表
乙 = []
for each_line in f:
    #读取文件内容
    (role, line_spoken)=each_line.split('：',1)
    #通过冒号对内容进行切片分割，左侧传给role，右侧传给line_spoken
    if role =='甲':
        #内容左侧包含甲的内容
        甲.append(line_spoken)
        #将内容都放进甲这个列表中
    if role =='乙':
        乙.append(line_spoken)
    else:
        file_甲_name = '甲' +'txt'#创建文件
        file_乙_name = '乙' +'txt'

        甲_file = open(file_甲_name,'w')#打开文件
        乙_file = open(file_乙_name,'w')

        甲_file.writelines(甲)#内容写入
        乙_file.writelines(乙)

        甲_file.close()#关闭文件
        乙_file.close()
f.close()
