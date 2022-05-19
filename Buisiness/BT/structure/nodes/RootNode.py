import Buisiness.BT.BT as BT
import Buisiness.BT.structure.nodes.Node as Node

class RootNode(Node.Node) :
	def __init__(self, id):
		super().__init__(id)
		self.status = 'Success'
		self.children = []

	def toString(self):
		return ("Node : " + str(self.id) + " |  Type : ROOT")

	def tick(self):

		#set all states to failure
		self.children[0].reset()

		#run tree
		self.children[0].tick()