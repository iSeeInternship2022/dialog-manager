import structure.nodes.Node as Node
from structure.nodes.StateType import StateType as State

class Succeder(Node.Node) :
	def __init__(self, id) -> None:
		super().__init__(id)

	def toString(self):
		return ("Node : " + str(self.id) + " |  Type : succeder")

	def tick(self, predecessor : "Node"):
		self.status = State.SUCCESS
		self.parent.tick(self)