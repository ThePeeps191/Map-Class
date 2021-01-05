class Map:
	def __init__(self):
		self.map = {}
	def put(self, key, val):
		self.map[key] = val
	def get(self, key):
		return self.map.get(key)
	def delete(self, key):
		del self.map[key]
	def length(self):
		return len(self.map)
	def inside(self, key):
		return (key in self.map)
