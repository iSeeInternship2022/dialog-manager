from structure.nodes.Node import Node
import threading
from BT.BT import BT
from structure.reactions.Predicates import check_predicate

class ConditioNode(Node) :
	def __init__(self, id, label) -> None:
		super().__init__(id)
		self.predicate = label

	def toString(self):
		return "Node : " + str(self.id) + " |  Type : desicion |  Label : " + self.predicate

	def tick(self, predecessor : "Node"):
		t = threading.Thread(target=check_predicate, args=(self.predicate,))
		t.start()
		t.join()

		if("""Predicate"""):
				self.status = 'Success'
		else:
			self.status = 'Failure'

		self.parent.tick(self)