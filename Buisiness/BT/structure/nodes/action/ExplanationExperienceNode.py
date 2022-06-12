import Buisiness.BT.BT as BT
import Buisiness.BT.structure.nodes.Node as Node
from Buisiness.BT.structure.nodes.StateType import StateType as State
from Buisiness.BT.structure.nodes.action.ActionNode import ActionNode
from Buisiness.BT.structure.nodes.action.ExplanationExpType import ExplanationExp

import Buisiness.Coordinator.Coordinator as C

class ExplanationExperienceNode(ActionNode) :
	def __init__(self, id) -> None:
		super().__init__(id)
		self.url = None
		self.type = None
		self.data_slot = None

	def toString(self):
		return ( "EXPLANATION "+str(self.status) + " " + str(self.id)  + " " + str(self.data_slot) + " " + str(self.message))

	def tick(self):
		if(self.type == ExplanationExp.EXPLANATION):
			message = C.Coordinator.API_querry(self.url)
			C.Coordinator.get().modifyWorld(self.data_slot, str(message["text"]))
			self.status = State.SUCCESS
		else :
			#plug the tree in
			pass
		
		return self.status
	
	def reset(self):
		if(self.status == State.SUCCESS):
			self.status = State.FAILURE

