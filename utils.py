class Storage(dict):
	"""
	"""
	def __getattr_(self,key):
		try:
			return self[key]
		except KeyError,k:
			raise AttributeError,k
	def __setattr__(self,key,value):
		self[key] = value
	def __delattr__(self,key):
		try:
			del self[key]
		except KeyError,k:
			raise AttributeError,k
	def __repr__(self):
		return '<Storage ' + dict.__repr__(self) + '>'

def group(seq,size):
	"""
	>>>list(group([1,2,3,4,5],2))
	[[1,2],[3,4],[5]]
	"""

	def take(seq,n):
		for i in xrange(n):
			yield seq.next()
	
	if not hasattr(seq,'next'):#not a iter object
		seq = iter(seq)
	while True:
		x = list(take(seq,size))
		if x:
			yield x
		else:
			break

if __name__ == "__main__":
	s = Storage(a=1)
	s.b = "hello"
	print s

	print list(group([1,2,3,4,5,6,7,8,9,0],3))
