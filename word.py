# -*- coding:utf-8 -*-
import datetime

list = {}
with open("《邮箱地址20200807》.txt", "r") as f:
    for line in f.readlines():
        line = line.strip('\n')  # 去掉列表中每一个元素的换行符
        #print(line)
        pos1 = line.find("/") # 找到/的位置
        pos2 = line.find("@") #找到@的位置
        line = line[pos1+1: pos2] #生产新的字符串 eg. zhangsan123
        #print(line)
        for index in range(len(line)):
            if(line[index].isdigit()):
                value = line[index:] #获得123
                break
        list[line] = value #以字典的形式存储

#print(list) 
#按value进行排序
result = sorted(list.items(),key=lambda x:x[1])
#print(result)

#获取当前时间
data = datetime.datetime.now().strftime('%Y%m%d')
#print(data)

#新的文件名
newtiite1 = "《邮箱地址" + data +"》.txt"

#写入到新文件中
with open(newtiite1,"w") as f:
    for (k,v) in result:
        f.write(k+"\n")#注意加换行符