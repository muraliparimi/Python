#!/usr/bin/python

import abc

class GetterSetter(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def set_val(self,input):
		""" Set a value in the instance """
		return

	@abc.abstractmethod
	def get_val(self):
		""" Return the instance value """
		return


class Myclass(GetterSetter):

	def __init__(self, val):
		self.val = val

	def set_val(self, input):
		self.val = input

	def get_val(self):
		return self.val

A = Myclass('one')

print A.get_val()

B = GetterSetter()