
from  Buisiness.BT.structure.nodes.Node import Node
import threading
import Buisiness.BT.BT as BT
from  Buisiness.BT.structure.nodes.StateType import StateType as State
import Buisiness.Coordinator.Coordinator as C

class ConditionNode(Node) :
	def __init__(self, id) -> None:
		super().__init__(id)
		self.data_slot = None

	def toString(self):
		return ( "DECISION "+str(self.status) + " " + str(self.id))

	def tick(self):


		bool = C.Coordinator.get().checkWorld(self.data_slot)

		if(bool):
				self.status = State.SUCCESS
		else:
			self.status = State.FAILURE

		return self.status

	def reset(self):
		self.status = State.FAILURE