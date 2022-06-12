from  Buisiness.BT.structure.nodes.Node import Node
from  Buisiness.BT.structure.nodes.StateType import StateType as State
import  Buisiness.BT.BT as BT
from Buisiness.BT.structure.nodes.decorators.DecoratorNode import DecoratorNode

class InverterNode(DecoratorNode) :
	def __init__(self, id) -> None:
		super().__init__(id)

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


