#!/usr/bin/python

class MyInteger(object):

	def set_val(self, val):
		try:
			val = int(val)
		except ValueError:
			return
		self.val=val

	def get_val(self):
		return self.val

	def increment_val(self, x):
		self.val += x




myInt = MyInteger()
myInt.set_val(10)
print myInt.get_val()
myInt.increment_val('Hi')
print myInt.get_val()

