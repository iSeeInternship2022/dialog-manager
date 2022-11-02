import Buisiness.BT.BT as BT
import Buisiness.BT.structure.nodes.Node as Node
from Buisiness.BT.structure.nodes.StateType import StateType as State
from Buisiness.BT.structure.nodes.action.ActionNode import ActionNode
from Buisiness.BT.structure.nodes.properties import Properties as P

import Buisiness.Coordinator.Coordinator as C

class QuestionNode(ActionNode) :
	def __init__(self, id) -> None:
		super().__init__(id)


	def toString(self):
		return ( "QUESTION "+str(self.status) + " " + str(self.id)  + " " + str(self.prop[P.QUESTION]) + " " + str(self.prop[P.ANSWER]))

	def tick(self):
		question = C.Coordinator.checkWorld(self.prop[P.QUESTION])
		C.Coordinator.get().ask(question, self.prop[P.ANSWER])
		self.status = State.SUCCESS
		
		return self.status
	
	def reset(self):
		if(self.status == State.SUCCESS):
			self.status = State.FAILURE


