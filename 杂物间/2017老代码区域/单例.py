class MusicPlayer(object):

	a = None
	# 如果是1 代表没有初始化过 如果是2代表已经初始化过
	b = 1

	def __new__(cls):
		if cls.a is None:
			cls.a = super().__new__(cls)
		return cls.a
	def __init__(self):
		if MusicPlayer.b == 2:
			return

		print("调用了")

		MusicPlayer.b = 2


		return 

A = MusicPlayer()
B = MusicPlayer()

print(id(A))
print(id(B))