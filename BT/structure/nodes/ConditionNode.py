from structure.nodes.Node import Node
import threading
import BT

from structure.reactions.Predicates import check_predicate

class ConditionNode(Node) :
	def __init__(self, id, label) -> None:
		super().__init__(id)
		self.predicate = label

	def toString(self):
		return "Node : " + str(self.id) + " |  Type : desicion |  Label : " + self.predicate

	def tick(self, predecessor : "Node"):
		print("Ticking : " + self.toString())

		bool = check_predicate(self.predicate)

		if(bool):
				self.status = 'Success'
		else:
			self.status = 'Failure'

		self.parent.tick(self)