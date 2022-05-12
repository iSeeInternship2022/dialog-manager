import threading
import time

#DRAFT - Not currently in use
class threadAction (threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter

        
	def run(self):
		print ("Starting " + self.name)

		

		print ("Exiting " + self.name)

