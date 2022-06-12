from abc import abstractmethod
from typing import List
from  Buisiness.BT.structure.nodes.Node import Node
from  Buisiness.BT.structure.nodes.StateType import StateType as State
import Buisiness.BT.BT as BT

class CompositeNode(Node) :
	def __init__(self, id) -> None:
		super().__init__(id)
		self.children = []

	@abstractmethod
	def reset(self):
		pass


	@abstractmethod
	def tick(self):
		pass


	@abstractmethod
	def toString(self):
		pass

