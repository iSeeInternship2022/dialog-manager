from asyncore import loop
import threading
from ui.Logger import Logger
from structure.Tree import printTree
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
		
		self.tree = tg.generateTree("Data\Data_Parser\BT-editor.JSON")
		printTree(self.tree.root)
		self.user_satisfied = False	
		#self.currentState = self.tree.root
		self.interface = UiConsole()
		self.logger = Logger()
		self.last_user_answer = None
		self.user_intent = ''
		self.survey_is_completed = False
		self.user_greeted = False

	def run(self):
		self.interface.send_to_user("Welcome!")
		while(True):
			self.tree.root.tick(self.tree.root)
		



	def send(self, message):
		self.interface.send_to_user("Bot : " + message)
	
	def receive(self):
		self.last_user_answer = self.interface.get_response()

	def restart(self):
		pass


#WIP main
