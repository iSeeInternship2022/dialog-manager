
from  Buisiness.BT.structure.nodes.Node import Node
import threading
import Buisiness.BT.BT as BT
from  Buisiness.BT.structure.nodes.StateType import StateType as State
import Buisiness.Coordinator.Coordinator as C

class EqualNode(Node) :
	def __init__(self, id) -> None:
		super().__init__(id)
		self.data_slot = None
		self.value = None

	def toString(self):
		return ( "EQUAL "+str(self.status) + " " + str(self.id) + " " + str(self.data_slot) + " " + str(self.value))

	def tick(self):

		data = C.Coordinator.get().checkWorld(self.data_slot)
		if(data == self.value):
			self.status = State.SUCCESS
			#print(str(self.data_slot) + " : " + str(data) + " = " + str(self.value))
		else:
			self.status = State.FAILURE
			#print(str(self.data_slot) + " : " + str(data) + " != " + str(self.value))

		return self.status

	def reset(self):
		self.status = State.FAILURE