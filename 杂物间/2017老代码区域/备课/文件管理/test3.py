f = open('test2.txt','r')
content = f.read(5)
print(content)
print('*'*20)
content = f.read()
print(content)
f.close()

