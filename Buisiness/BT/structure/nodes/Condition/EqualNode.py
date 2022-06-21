
from  Buisiness.BT.structure.nodes.Node import Node
import threading
import Buisiness.BT.BT as BT
from  Buisiness.BT.structure.nodes.StateType import StateType as State
import Buisiness.Coordinator.Coordinator as C
from Buisiness.BT.structure.nodes.properties import Properties as P

class EqualNode(Node) :
	def __init__(self, id) -> None:
		super().__init__(id)

	def toString(self):
		return ( "EQUAL "+str(self.status) + " " + str(self.id) + " " + str(self.prop[P.DATA_IS_EQUAL.value]) + " " + str(self.prop[P.EQUAL_TO_VALUE.value]))

	def tick(self):

		data = C.Coordinator.get().checkWorld(self.prop[P.DATA_IS_EQUAL])
		if(data == self.prop[P.EQUAL_TO_VALUE]):
			print("equal")
			self.status = State.SUCCESS
			#print(str(self.data_slot) + " : " + str(data) + " = " + str(self.value))
		else:
			print("not equal")
			self.status = State.FAILURE
			#print(str(self.data_slot) + " : " + str(data) + " != " + str(self.value))

		return self.status

	def reset(self):
		self.status = State.FAILURE