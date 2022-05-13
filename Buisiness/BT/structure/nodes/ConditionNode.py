from  Buisiness.BT.structure.nodes.Node import Node
import threading
import Buisiness.BT.BT as BT
from  Buisiness.BT.structure.nodes.StateType import StateType as State
from  Buisiness.BT.structure.reactions.Predicates import check_predicate

class ConditionNode(Node) :
	def __init__(self, id, label) -> None:
		super().__init__(id)
		self.predicate = label

	def toString(self):
		return ( "DECISION "+str(self.status) + " " + str(self.id) + " " + self.predicate)

	def tick(self, predecessor : "Node"):
		BT.BT.getBT().logger.log("open " + self.toString())

		bool = check_predicate(self.predicate)

		if(bool):
				self.status = State.SUCCESS
		else:
			self.status = State.FAILURE


		BT.BT.getBT().logger.log("closed " +self.toString())
		return self.status

	def reset(self):
		self.status = State.FAILURE