class MusicPlayer(object):
	
	instance = None
	def __new__(cls):

		if cls.instance is None:
			cls.instance = super().__new__(cls)			

		return cls.instance
	
	def __init__(self):
		self.name = "段金松"
		print(id(self))

a = MusicPlayer()
a1 = MusicPlayer()
a2 = MusicPlayer()

a2.name = "蔡英文"
print(a.name)
print(a1.name)
a1.name = "马英九"
print(a2.name)
# a = MusicPlayer()
# a1 = MusicPlayer()
# a2 = MusicPlayer()
# print(id(a))
# print(id(a1))
# print(id(a2))


