import BT
import structure.nodes.Node as Node

class RootNode(Node.Node) :
	def __init__(self, id):
		super().__init__(id)
		self.status = 'Success'

	def toString(self):
		return ("Node : " + str(self.id) + " |  Type : ROOT")

	def tick(self, predecessor : "Node"):
		BT.BT.getBT().logger.log("Ticking : " + self.toString())
		self.children[0].tick(self)