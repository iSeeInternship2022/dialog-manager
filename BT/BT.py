import threading

import data.TreeGenerator as tg
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
		
		self.tree = tg.generateTree("BT\data\BT-editor.JSON")
		self.tree.print_tree()
		self.user_satisfied = False	
		#self.currentState = self.tree.root
		self.interface = UiConsole()
		self.last_user_answer = ''
		self.user_intent = ''
		self.survey_is_completed = False

	def run(self):
		self.interface.send_to_user("Welcome!")
		self.tree.root.tick(self.tree.root)



	def send(self, message):
		self.interface.send_to_user(message)
	
	def receive(self):
		self.last_user_answer = self.interface.get_response



#WIP main
