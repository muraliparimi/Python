#!/usr/bin/python

import abc

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

class GetSetInt(GetSetParent):

	def set_val(self, value):
		if not isinstance(value, int):
			value=0
		super(GerSetInt, self).set_val(value)

	def showdoc(self):
		print '(GetSetInt object:{0} only accepts integer values.'.format(id(self))


A = GetSetInt(5)

print A.get_val()
A.showdoc()