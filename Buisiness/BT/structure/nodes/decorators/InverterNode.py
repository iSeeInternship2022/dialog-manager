from  Buisiness.BT.structure.nodes.Node import Node
from  Buisiness.BT.structure.nodes.StateType import StateType as State
import  Buisiness.BT.BT as BT

class InverterNode(Node) :
	def __init__(self, id) -> None:
		super().__init__(id)
		self.child = None

	def toString(self):
		
		return ( "LIMIT "+str(self.status) + " " + str(self.id))

	def tick(self):

		if(self.child.tick()):
			self.status = State.FAILURE
		else:
			self.status = State.SUCCESS
		
		return self.status



	def reset(self):
		self.status = State.FAILURE
		self.child.reset()


