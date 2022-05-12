import BT
import structure.nodes.Node as Node

class RootNode(Node.Node) :
	def __init__(self, id):
		super().__init__(id)
		self.status = 'Success'

	def toString(self):
		return ("Node : " + str(self.id) + " |  Type : ROOT")

	def tick(self, predecessor : "Node"):
		BT.BT.getBT().logger.log(self.toString())

		#set all states to failure
		self.children[0].reset()

		#run tree
		self.children[0].tick(self)