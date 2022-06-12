from abc import abstractmethod
from  Buisiness.BT.structure.nodes.Node import Node
from  Buisiness.BT.structure.nodes.StateType import StateType as State
import  Buisiness.BT.BT as BT

class DecoratorNode(Node) :
	def __init__(self, id) -> None:
		super().__init__(id)
		self.child = None

	@abstractmethod
	def reset(self):
		pass


	@abstractmethod
	def tick(self):
		pass


	@abstractmethod
	def toString(self):
		pass

