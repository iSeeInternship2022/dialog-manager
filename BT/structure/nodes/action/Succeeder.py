import structure.nodes.Node as Node

class Succeder(Node.Node) :
	def __init__(self, id) -> None:
		super().__init__(id)

	def toString(self):
		return ("Node : " + str(self.id) + " |  Type : succeder")

	def tick(self, predecessor : "Node"):
		self.status = 'Success'
		self.parent.tick(self)