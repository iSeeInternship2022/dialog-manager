import threading
import time

exitFlag = 0


#DRAFT - Not currently in use
class threadTicks (threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print ("Starting " + self.name)

		

		print ("Exiting " + self.name)



# Create new threads
thread1 = threadTicks(1, "Thread-1", 1)
thread2 = threadTicks(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

print ("Exiting Main Thread")