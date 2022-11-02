from abc import abstractmethod
import threading
import Buisiness.BT.BT as BT
import Buisiness.BT.structure.nodes.Node as Node
from  Buisiness.BT.structure.reactions.Actions import do_action
from  Buisiness.BT.structure.nodes.StateType import StateType as State

class ActionNode(Node.Node) :
	def __init__(self, id) -> None:
		super().__init__(id)

	@abstractmethod
	def reset(self):
		pass


	@abstractmethod
	def tick(self):
		pass


	@abstractmethod
	def toString(self):
		pass
