from Buisiness.BT.structure.Tree import printTree
from ui.Logger import Logger
import Buisiness.BT.structure.TreeGenerator as tg



class BT:

	def __init__(self):

		self.tree = tg.generateTree("Data\Data_Parser\dialog-BT.JSON")
		printTree(self.tree.root)

		#self.currentState = self.tree.root
		
		self.logger = Logger()
		self.coordinator = None


	def run(self):
		while(True):
			self.tree.root.tick()
		
	def restart(self):
		pass


#WIP main

