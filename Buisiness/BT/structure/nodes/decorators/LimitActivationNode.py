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
		kids =" ".join(str(elem) for elem in self.child)
		return ( "REP TILL SUCC "+str(self.status) + " " + str(self.id))

	def tick(self):

		if(self.timesActivated < self.limit):
			self.status = self.child.tick()
		else:
			self.status = State.SUCCESS

		return self.status



	def reset(self):
		self.status = State.FAILURE
		for child in self.children:
			child.reset()


