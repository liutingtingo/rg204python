# 打开一个已经存在的文件
f = open("test2.txt","r")
str = f.read(30)
print("读取的数据是：",str)

# 查找当前位置
position = f.tell()
print("当前文件位置:",position)

# 重新设置位置(从文件开头，偏移5个字节）
f.seek(5,0)

# 查找当前位置
position = f.tell()
print("当前文件位置:",position)


f.close()

