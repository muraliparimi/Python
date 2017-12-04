#!/usr/bin/python

import abc
import datetime

class WriteFile(object):

	__metaclass__ = abc.ABCMeta

	def __init__(self, inputFile):
		self.inputFile = inputFile
	
	@abc.abstractmethod
	def write(self, inputText):
		""" writes to a file """
		return

	def write_line(self,inputText):
		fh = open(self.inputFile,'a')
		fh.write(inputText + '\n')
		fh.close()

class LogFile(WriteFile):

	
	def __init__(self, inputFile):
		super(LogFile,self).__init__(inputFile)


	def write(self, inputText):
		dt_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		self.write_line(dt_str + "  " + inputText)





class DelimFile(WriteFile):

	def __init__(self, inputFile, Delimiter):
		super(DelimFile,self).__init__(inputFile)
		self.Delimiter = Delimiter

	def write(self,inputText):
		writeString=self.Delimiter.join(inputText)
		self.write_line(writeString)
'''		for item in inputText[:-1]:
			if item.find(self.Delimiter):
				writeString += "'"+item+"'" + self.Delimiter
			else:
			    writeString += item + self.Delimiter
		writeString += inputText[-1]'''




log = LogFile("log.txt")
log.write("First Log message")
log.write("Second Log message")

pipeFile = DelimFile('text.psv','|')
pipeFile.write(['1','2','3','4'])

pipeFile = DelimFile('text.csv',',')
pipeFile.write(['a,1','b,2','c,3','4'])

