import structure.nodes.Node as Node
class DecisionNode(Node.Node) :
	def __init__(self, id, label) -> None:
		super().__init__(id)
		self.predicate = label

	def toString(self):
		return "Node : " + str(self.id) + " |  Type : desicion |  Label : " + self.predicate

	def goToNext(self, predecessor : "Node"):
		pass