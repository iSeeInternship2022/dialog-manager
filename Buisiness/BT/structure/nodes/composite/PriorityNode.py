from typing import List
from  Buisiness.BT.structure.nodes.Node import Node
from  Buisiness.BT.structure.nodes.StateType import StateType as State
import Buisiness.BT.BT as BT

class PriorityNode(Node) :
	def __init__(self, id) -> None:
		super().__init__(id)
		self.children = []

	def toString(self):
		kids =" " + (str(len(self.children)))
		return ( "PRIORITY "+str(self.status) + " " + str(self.id))

	def tick(self):


		for child in self.children:
			if(child.tick() == State.SUCCESS):
				self.status = State.SUCCESS
				break

		return self.status
			#back to parents node
				

	def reset(self):
		self.status = State.FAILURE
		for child in self.children:
			child.reset()

