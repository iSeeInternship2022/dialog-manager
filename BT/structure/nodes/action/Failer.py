import structure.nodes.Node as Node
from structure.nodes.StateType import StateType as State
import BT

class Failer(Node.Node) :
	def __init__(self, id) -> None:
		super().__init__(id)

	def toString(self):
		return ("Node : " + str(self.id) + " |  Type : succeder")

	def tick(self, predecessor : "Node"):
		BT.BT.getBT().logger.log("Ticking : " + self.toString())
		self.status = State.FAILURE
		self.parent.tick(self)