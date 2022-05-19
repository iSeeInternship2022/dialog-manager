from  Buisiness.BT.structure.nodes.Node import Node
from  Buisiness.BT.structure.nodes.StateType import StateType as State
import  Buisiness.BT.BT as BT

class LimitActivationNode(Node) :
	def __init__(self, id) -> None:
		super().__init__(id)
		self.timesActivated = 0
		self.limit = None
		self.child = None

	def toString(self):
		
		return ( "LIMIT "+str(self.status) + " " + str(self.id))

	def tick(self):

		if(self.timesActivated < self.limit):
			self.timesActivated += 1
			self.status = self.child.tick()
		else:
			self.status = State.SUCCESS

		return self.status



	def reset(self):
		self.status = State.FAILURE
		self.child.reset()


