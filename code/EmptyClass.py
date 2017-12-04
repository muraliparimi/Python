#!/usr/bin/python

import random

class MyClass(object):
	
	def describeme(self1):
		print "This is a describeme method call from an instance:"
		print self1
	def generateId(self1):
		self1.id = random.randint(1,100)
	def set_val(self1,val):
		self1.value = val;
	def get_val(self1):
		return self1.value;



Obj1= MyClass()
Obj2= MyClass()

Obj1.set_val(10);
Obj2.set_val(100);
print Obj1.get_val();
print Obj2.get_val();

