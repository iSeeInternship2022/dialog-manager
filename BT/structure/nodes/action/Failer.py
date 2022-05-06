import structure.nodes.Node as Node

class Failer(Node.Node) :
	def __init__(self, id) -> None:
		super().__init__(id)

	def toString(self):
		return ("Node : " + str(self.id) + " |  Type : succeder")

	def tick(self, predecessor : "Node"):
		self.status = 'Failure'
		self.parent.tick(self)