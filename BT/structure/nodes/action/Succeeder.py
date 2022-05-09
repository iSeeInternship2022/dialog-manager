import structure.nodes.Node as Node
from structure.nodes.StateType import StateType as State
import BT

class Succeder(Node.Node) :
	def __init__(self, id) -> None:
		super().__init__(id)

	def toString(self):
		return ( "SUCCEDER "+str(self.status) + " " + str(self.id))

	def tick(self, predecessor : "Node"):
		BT.BT.getBT().logger.log(self.toString())
		self.status = State.SUCCESS
		self.parent.tick(self)