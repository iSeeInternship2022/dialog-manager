from cProfile import label
import threading
import Buisiness.BT.BT as BT
import Buisiness.BT.structure.nodes.Node as Node
from  Buisiness.BT.structure.reactions.Actions import do_action
from  Buisiness.BT.structure.nodes.StateType import StateType as State
import Buisiness.Coordinator.Coordinator as C

class InformationNode(Node.Node) :
	def __init__(self, id) -> None:
		super().__init__(id)
		self.message_slot = None

	def toString(self):
		return ( "message "+str(self.status) + " " + str(self.id) + " " + self.message)

	def tick(self):


		message = C.Coordinator.checkWorld(self.message_slot)
		C.Coordinator.get().inform(message)
		self.status = State.SUCCESS
		return self.status
	
	def reset(self):
		if(self.status == State.SUCCESS):
			self.status = State.FAILURE


