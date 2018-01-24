class SweetPotato(object):
    """烤地瓜类"""
    def __init__(self):
        # 这个属性是地瓜的生熟程度 
        self.cookedLever = 0
        # 返回给用户的字符串
        self.cookedString = "生的"
        # 地瓜的配料列表
        self.condiments = []
    def __str__(self):
        
        msg = ""

        if len(self.condiments) >0:
            for test in self.condiments:
                msg = msg + test

        return_msg = "当前的地瓜是%s,调料有%s"%(self.cookedString,msg)

        return return_msg
    
    def addCondiments(self,name):
        self.condiments.append(name)

    def cook(self,time):
        """这是烤地瓜的方法，需要给我传时间"""
        self.cookedLever += time

        if self.cookedLever>8:
            self.cookedString = "烤糊了"
        elif self.cookedLever>5:
            self.cookedString = "烤熟了"
        elif self.cookedLever>3:
            self.cookedString = "半生不熟"
        else:
            self.cookedString = "生的"

djs_kaodigua = SweetPotato()
djs_kaodigua.cook(3)
djs_kaodigua.addCondiments("番茄酱")
print(djs_kaodigua)
djs_kaodigua.cook(1)
djs_kaodigua.addCondiments("汁")
print(djs_kaodigua)



