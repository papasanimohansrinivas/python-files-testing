class Solution():
	def __init__(self):
		self.keys = [None for index in xrange(100000)]
		self.values = [None for index_1 in xrange(100000)]
		self.size_1 = 0


	def insert(self,key,value):
		index = self.rank(key)

		if index==self.size_1:
			self.keys[self.size_1]=key
			self.values[self.size_1]=value
			self.size_1+=1
			return 

		size = self.size_1

		for q in xrange(size,index-1,-1):
			self.keys[q]=self.keys[q-1]
			self.values[q]=self.values[q-1]

		self.keys[index] = key
		self.values[index] = value
		self.size_1+=1
		return 


	def rank(self,key):

		low = 0
		high = self.size_1-1

		while low<=high:

			mid = int((low+high)/2)
			elem = self.keys[mid]
			# self.compare(key,elem)
			if elem==key:
				return mid
			if key>elem:
				low = mid + 1

			if key<elem:
				high = mid - 1

		return low

	def select(self,rank):

		if rank>0 and rank<self.size_1:
			return self.keys[rank]

		return "called select() with invalid argument: "+str(rank)

	def size(self):

		return self.size_1

	def min(self):

		return self.keys[0]

	def max(self):

		return self.keys[self.size_1-1]

	def contains(self,key):
		index = self.rank(key)

		if index>self.size_1-1:
			return "false"
		if self.keys[index]!=key:
			return "false"
		return "true"

	def floor(self,key):
		if self.size_1==0:
			return "null"
		index = self.rank(key)
		if index == 0:
			return self.keys[index]

		return self.keys[index-1]

	def ceiling(self,key):
		if self.size_1==0:
			return "null"
		index = self.rank(key)
		if index==self.size_1:
			return self.keys[index-1]
		if index==self.size_1-1:
			return self.keys[index]

		return self.keys[index+1]

	def deleteMin(self):
		if self.size_1==1:
			self.keys[self.size_1-1]=None
			self.size_1-=1
			return "Symbol table underflow error"
		if self.size_1==0:
			return "Symbol table underflow error"
		for z in xrange(self.size_1):
			self.keys[z]=self.keys[z+1]
			self.values[z]=self.values[z+1]

		self.size_1-=1
		return self.string()


	def deleteMax(self):
		if self.size_1==1:
			self.keys[self.size_1-1]=None
			self.size_1-=1
			return "Symbol table underflow error"
		if self.size_1==0:
			return "Symbol table underflow error"
		self.keys[self.size_1-1]=None
		self.size_1-=1
		return self.string()




	def string(self):
		stri = ""

		for a in xrange(self.size_1):
			if a!=self.size_1-1:
				stri = stri +self.keys[a] + ", "
			else:
				stri = stri + self.keys[a]
		return stri


def test_cases():

	t = input()

	for number  in xrange(t):
		s = Solution()
		n = input()
		for operations in xrange(n):
			process = raw_input()
			temp = process.strip().split()
			if len(temp)==1:
				operation = temp[0]
				if operation == "min":
					print s.min()
				if operation == "max":
					print s.max()
				if operation == "size":
					print s.size()
				if operation == "deleteMin":
					print s.deleteMin()
					# print s.string()
				if operation == "deleteMax":
					print s.deleteMax()
					# print s.string()

			if len(temp)==2:
				operation = temp[0]
				arg = temp[1]
				if operation == "select":
					print s.select(arg)
				if operation == "contains":
					print s.contains(arg)
				if operation == "floor":
					print s.floor(arg)
				if operation == "ceiling":
					print s.ceiling(arg)

			if len(temp)==3:
				operation = temp[0]
				key = temp[1]
				value = int(temp[2])
				if operation == "insert":
					s.insert(key,value)
					print s.string()


test_cases()
