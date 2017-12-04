#!/usr/bin/python

class A(object):

	def __init__(self,name):
		self.name = name

	def doThis(self, action):
		print self.name + "does " + str(action) + " occasionally!"
    


class B(A):
	pass

class C(A):
	def doThis(self):
		print self.name + " always runs"

class D(B,C):
	pass


d = D('Horse')

d.doThis()
print D.mro()