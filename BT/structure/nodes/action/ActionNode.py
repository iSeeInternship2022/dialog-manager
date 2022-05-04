import structure.nodes.Node as Node
class ActionNode(Node.Node) :
	def __init__(self, id, label) -> None:
		super().__init__(id)
		self.action = label

	def toString(self):
		return ("Node : " + str(self.id) + " |  Type : action |  Label : " + self.action)

	def goToNext(self, predecessor : "Node"):
		pass