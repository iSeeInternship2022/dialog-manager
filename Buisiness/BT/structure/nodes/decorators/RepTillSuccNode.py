from  Buisiness.BT.structure.nodes.Node import Node
from  Buisiness.BT.structure.nodes.StateType import StateType as State
import  Buisiness.BT.BT as BT
from Buisiness.BT.structure.nodes.decorators.DecoratorNode import DecoratorNode

class RepTillSuccNode(DecoratorNode) :
	def __init__(self, id) -> None:
		super().__init__(id)

	def toString(self):
		return ( "REP TILL SUCC "+str(self.status) + " " + str(self.id))

	def tick(self):
		
		self.status = State.SUCCESS
		child_status = State.FAILURE
		while(child_status !=State.SUCCESS):
			child_status = self.child.tick()
		

		self.status = State.SUCCESS

		return self.status


	def reset(self):
		self.status = State.FAILURE
		self.child.reset()


