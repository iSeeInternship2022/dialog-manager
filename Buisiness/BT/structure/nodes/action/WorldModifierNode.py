from cProfile import label
import threading
import Buisiness.BT.BT as BT
import Buisiness.BT.structure.nodes.Node as Node
from  Buisiness.BT.structure.reactions.Actions import do_action
from  Buisiness.BT.structure.nodes.StateType import StateType as State
import Buisiness.Coordinator.Coordinator as C

class WorldModifierNode(Node.Node) :
	def __init__(self, id) -> None:
		super().__init__(id)
		self.value = None
		self.data_slot = None

	def toString(self):
		return ( "message "+str(self.status) + " " + str(self.id))

	def tick(self):

		C.Coordinator.get().modifyWorld(self.data_slot, self.value)
		self.status = State.SUCCESS

		return self.status
	
	def reset(self):
		if(self.status == State.SUCCESS):
			self.status = State.FAILURE


