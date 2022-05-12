import structure.nodes.Node as Node
from structure.nodes.StateType import StateType as State
import BT

class Failer(Node.Node) :
	def __init__(self, id) -> None:
		super().__init__(id)

	def toString(self):
		return ( "FAILER "+str(self.status) + " " + str(self.id))

	def tick(self, predecessor : "Node"):
		BT.BT.getBT().logger.log(self.toString())
		self.status = State.FAILURE
		return self.status


	def reset(self):
		self.status = State.FAILURE