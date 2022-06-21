import Buisiness.BT.BT as BT
import Buisiness.BT.structure.nodes.Node as Node
from Buisiness.BT.structure.nodes.StateType import StateType as State
from Buisiness.BT.structure.nodes.action.ActionNode import ActionNode
from Buisiness.BT.structure.nodes.action.ExplanationExpType import ExplanationExp
from Buisiness.BT.structure.nodes.properties import Properties as P

import Buisiness.Coordinator.Coordinator as C

class ExplanationExperienceNode(ActionNode) :
	def __init__(self, id) -> None:
		super().__init__(id)


	def toString(self):
		return ( "EXPLANATION "+str(self.status) + " " + str(self.id)  + " " + str(self.prop[P.SAVE]))

	def tick(self):
		if(self.prop[P.TYPE] == ExplanationExp.EXPLANATION):
			print("calling " + self.prop[P.URL])
			message = C.Coordinator.API_querry(self.prop[P.URL])
			C.Coordinator.get().modifyWorld(self.prop[P.SAVE], str(message["text"]))
			self.status = State.SUCCESS
		else :
			subtree_json = C.Coordinator.API_querry_raw(self.prop[P.URL])
			C.Coordinator.API_plug_subtree(self, subtree_json)
			pass
		
		return self.status
	
	def reset(self):
		if(self.status == State.SUCCESS):
			self.status = State.FAILURE

