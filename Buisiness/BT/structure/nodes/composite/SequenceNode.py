from typing import List
from  Buisiness.BT.structure.nodes.Node import Node
from  Buisiness.BT.structure.nodes.StateType import StateType as State
import Buisiness.BT.BT as BT
from Buisiness.BT.structure.nodes.composite.CompositeNode import CompositeNode


class SequenceNode(CompositeNode) :
	def __init__(self, id) -> None:
		super().__init__(id)
		
	def toString(self):
		kids =" "+ (str(len(self.children)))
		return ( "SEQUENCE "+str(self.status) + " " + str(self.id))

	def tick(self):
		self.status = State.SUCCESS

		for child in self.children:
			if(child.tick() == State.FAILURE):
				self.status = State.FAILURE
				break

		#back to parents node
		return self.status

	def reset(self):
		self.status = State.FAILURE
		for child in self.children:
			child.reset()

