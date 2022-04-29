import threading

import data.TreeGenerator as tg
from network.BT_Network import BT_Network as Network
from ui.UiConsole import UiConsole


class BT:
	__instance = None

	@staticmethod 
	def getBT():
		
		if BT.__instance == None:
			BT()
		return BT.__instance
	
	def __init__(self):
		#Virtually private constructor
		if BT.__instance != None:
			raise Exception("This is a singleton")
		else:
			BT.__instance = self
		
		self.tree = tg.generateTree("data\BT-editor.JSON")
		self.tree.print_tree()
		self.user_satisfied = False	
		self.currentState = self.tree.root
		self.interface = UiConsole()

	def run(self):
		self.interface.send_to_user("Welcome!")

		#one thread will do the needed action
		#t = threading.Thread(target=self.do, args=(self.tree.getCurrentAction,))
		#t.start()

		#one other will traverse the tree to check that nothing has changed and what is the current action to do
		# creating thread
		#t = threading.Thread(target=do, args=("greet",))
		# starting thread 2
		#t.start()


	def do(action):

		print(action)




#WIP main

BT().getBT().run()