class 车类(object):

    def __init__(self,color):

        self.颜色 = color

    def 移动(self):
        print(self.颜色)

宝马 = 车类('黄色')
宝马.移动()
宝马.颜色 = '白色'
宝马.移动()

