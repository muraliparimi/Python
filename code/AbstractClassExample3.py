

#!/usr/bin/python

import abc

"""
This code is an example of method overriding , method overloading and polymorphism in python
"""

class GetSetParent(object):

	__metaclass__ = abc.ABCMeta

	def __init__(self,value):
		self.value = value

	def set_val(self, value):
		self.valu = value

	def get_val(self):
		return self.value

	@abc.abstractmethod
	def showdoc(self):
		return

class GetSetList(GetSetParent):

	def __init__(self):
		self.vallist = []

	def set_val(self, val):
		self.vallist.append(val)

	def get_val(self):
		return self.vallist[-1]

	def get_vals(self):
		return self.vallist[:]

	def showdoc(self):
		print "The GetSetList object:{0} of length:{1} is a container data structure that stores all the values".format(id(self), len(self.vallist))

A = GetSetList()

A.set_val(10)
print A.get_val()
print A.get_vals()
A.set_val(20)
print A.get_val()
print A.get_vals()
A.set_val('Murali')
print A.get_val()
print A.get_vals()

A.showdoc()