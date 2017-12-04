#!/usr/bin/python

import random

class Date(object):
	def get_date(self):
		return '2013-10-12'

class Time(Date):
	def get_time(self):
		return "12:15:29"

	def get_date(self):
		return '2017-11-08'

class Animal(object):
	def __init__(self,name):
		self.name = name
	def eat(self,food):
		print '%s is eating %s.' % (self.name, food)
	def show_affection(self):
		print "{0} wags tail".format(self.name)


class Dog(Animal):
	def __init__(self,name):
		super(Dog,self).__init__(name)
		self.breed = random.choice(['Labrador','German Sheferd', 'pug'])


	def fetch(self, thing):
		print '%s goes after %s.' %(self.name, thing)

class Cat(Animal):
	def swatstring(self):
		print '%s shreds the string' %(self.name)
	def show_affection(self):
		print "{0} purss".format(self.name)


dt = Date()
tm = Time()

print dt.get_date()

print tm.get_time()
print tm.get_date()

r = Dog('Rover')
f = Cat('Fluffy')

print r.name + ' is a ' + r.breed
r.eat('Meat')
f.eat('Egg')
f.swatstring()
f.show_affection()
r.fetch('thief')
r.show_affection()

print len([('a','b','c'), ('b','c','d')])
var='1'
print var.__sizeof__()

print Dog.mro()
print Cat.mro()