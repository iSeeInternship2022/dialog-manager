from structure.nodes.Node import Node
import threading
import BT
from structure.nodes.StateType import StateType as State
from structure.reactions.Predicates import check_predicate

class ConditionNode(Node) :
	def __init__(self, id, label) -> None:
		super().__init__(id)
		self.predicate = label

	def toString(self):
		return ( "DECISION "+str(self.status) + " " + str(self.id) + " " + self.predicate)

	def tick(self, predecessor : "Node"):
		BT.BT.getBT().logger.log(self.toString())

		bool = check_predicate(self.predicate)

		if(bool):
				self.status = State.SUCCESS
		else:
			self.status = State.FAILURE

		self.parent.tick(self)