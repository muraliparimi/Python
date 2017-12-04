#!/usr/bin/python

class MaxSizeList(object):
	def __init__(self, size):
		try:
			size = int(size)
		except ValueError:
			size = 0
			return
		self.size = size
		self.list = []

	def push(self, val):
		#print 'size of list: %s' % str((int(self.size)+1))
		if (len(self.list) <self.size):
			self.list.append(val)
			#print "after adding a new element:'%s' the size of list is %s" %(val, len(self.list))
			#print self.list
		else:
			self.list.pop(0)
			self.list.append(val)

	def get_list(self):
		return self.list

a=MaxSizeList(3)
b=MaxSizeList(1)

a.push('hey')
a.push('hi')
a.push("let's")
a.push('go')

b.push('hey')
b.push('go')

print(a.get_list())
print(b.get_list())