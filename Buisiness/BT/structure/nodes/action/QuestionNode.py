import Buisiness.BT.BT as BT
import Buisiness.BT.structure.nodes.Node as Node
from Buisiness.BT.structure.nodes.StateType import StateType as State

import Buisiness.Coordinator.Coordinator as C

class QuestionNode(Node.Node) :
	def __init__(self, id) -> None:
		super().__init__(id)
		self.message = None
		self.data_slot = None

	def toString(self):
		return ( "message "+str(self.status) + " " + str(self.id) + " " + self.message)

	def tick(self, predecessor : "Node"):

		BT.BT.getBT().logger.log("open " +self.toString())

		C.Coordinator.get().ask(self.message, self.data_slot)
		self.status = State.SUCCESS
		
		BT.BT.getBT().logger.log("closed " +self.toString())
		return self.status
	
	def reset(self):
		if(self.status == State.SUCCESS):
			self.status = State.FAILURE


