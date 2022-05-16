from Buisiness.BT.structure.Tree import printTree
from ui.Logger import Logger
import Buisiness.BT.structure.TreeGenerator as tg



class BT:

	def __init__(self):

		self.tree = tg.generateTree("Data\Data_Parser\BT-editor.JSON")
		printTree(self.tree.root)

		#self.currentState = self.tree.root
		
		self.logger = Logger()
		self.coordinator = None


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

