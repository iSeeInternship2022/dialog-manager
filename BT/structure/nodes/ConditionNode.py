from structure.nodes.Node import Node

class ConditioNode(Node) :
	def __init__(self, id, label) -> None:
		super().__init__(id)
		self.predicate = label

	def toString(self):
		return "Node : " + str(self.id) + " |  Type : desicion |  Label : " + self.predicate

	def tick(self, predecessor : "Node"):
		pass