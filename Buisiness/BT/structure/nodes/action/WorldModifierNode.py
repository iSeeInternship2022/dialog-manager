from cProfile import label
import threading
import Buisiness.BT.BT as BT
import Buisiness.BT.structure.nodes.Node as Node
from Buisiness.BT.structure.nodes.action.ActionNode import ActionNode
from  Buisiness.BT.structure.reactions.Actions import do_action
from  Buisiness.BT.structure.nodes.StateType import StateType as State
import Buisiness.Coordinator.Coordinator as C
from Buisiness.BT.structure.nodes.properties import Properties as P

class WorldModifierNode(ActionNode) :
	def __init__(self, id) -> None:
		super().__init__(id)


	def toString(self):
		return ( "MODIFIER "+str(self.status) + " " + str(self.id) + " " + str(self.prop[P.DATA_TO_MODIFY]) + " " + str(self.prop[P.VALUE]))

	def tick(self):

		C.Coordinator.get().modifyWorld(self.prop[P.DATA_TO_MODIFY], self.prop[P.VALUE])
		self.status = State.SUCCESS

		return self.status
	
	def reset(self):
		if(self.status == State.SUCCESS):
			self.status = State.FAILURE


