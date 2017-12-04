#!/usr/bin/python

import random
import StringIO

class WriteMyStuff(object):

	def __init__(self, writer):
		self.writer = writer

	def write(self, message):
		self.writer.write(message)


fh = open('test.txt','w')
w1 = WriteMyStuff(fh)


w1.write("Hello World!")
fh.close()

sioh = StringIO.StringIO()

w2 = WriteMyStuff(sioh)

w2.write("Hello World!")
'''sioh.close()'''

print 'File object: ', open('test.txt','r').read()
print 'StringIO object: ',sioh.getvalue()  
