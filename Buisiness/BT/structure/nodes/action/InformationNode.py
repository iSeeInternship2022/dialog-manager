from cProfile import label
import threading
import Buisiness.BT.BT as BT
import Buisiness.BT.structure.nodes.Node as Node
from Buisiness.BT.structure.nodes.action.ActionNode import ActionNode
from  Buisiness.BT.structure.reactions.Actions import do_action
from  Buisiness.BT.structure.nodes.StateType import StateType as State
import Buisiness.Coordinator.Coordinator as C
from Buisiness.BT.structure.nodes.properties import Properties as P

class InformationNode(ActionNode) :
	def __init__(self, id) -> None:
		super().__init__(id)

	def toString(self):
		return ( "message "+str(self.status) + " " + str(self.id) + " " + self.prop[P.MESSAGE])

	def tick(self):


		message = C.Coordinator.checkWorld(self.prop[P.MESSAGE])
		C.Coordinator.get().inform(message)

		#Here should be a verification that the message has been sent correctly
		self.status = State.SUCCESS
		
		return self.status
	
	def reset(self):
		if(self.status == State.SUCCESS):
			self.status = State.FAILURE


