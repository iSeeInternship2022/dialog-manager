import  Buisiness.BT.structure.nodes.Node as Node
from  Buisiness.BT.structure.nodes.StateType import StateType as State
import Buisiness.BT.BT as BT

class Succeder(Node.Node) :
	def __init__(self, id) -> None:
		super().__init__(id)

	def toString(self):
		return ( "SUCCEDER "+str(self.status) + " " + str(self.id))

	def tick(self):

		self.status = State.SUCCESS
		return self.status

	def reset(self):
		self.status = State.FAILURE