import  Buisiness.BT.structure.nodes.Node as Node
from  Buisiness.BT.structure.nodes.StateType import StateType as State
import Buisiness.BT.BT as BT
from Buisiness.BT.structure.nodes.action.ActionNode import ActionNode

class Succeeder(ActionNode) :
	def __init__(self, id) -> None:
		super().__init__(id)

	def toString(self):
		return ( "SUCCEDER "+str(self.status) + " " + str(self.id))

	def tick(self):

		self.status = State.SUCCESS
		return self.status

	def reset(self):
		self.status = State.FAILURE