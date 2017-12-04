#!/usr/bin/python

class InstanceCounter(object):
    counter = 0

    def __init__(self, val):
	self.val = self.evalaute(val)
	InstanceCounter.counter +=1

    @staticmethod
    def evalaute(val):
        if not isinstance(val,int):
            return 0
        else:
            return val

    def set_val(self,val):
	self.val = val

    def get_val(self):
	return self.val

    @classmethod
    def get_count(cls):
	return cls.counter

A = InstanceCounter(2)
B = InstanceCounter(3)
C = InstanceCounter('10')

print A.get_val()
print A.get_count()

print B.get_val()
print B.get_count()

print C.get_val()
print C.get_count()
