from structure.nodes.Node import Node
from structure.nodes.StateType import StateType as State
import BT

class RepTillFailNode(Node) :
	def __init__(self, id) -> None:
		super().__init__(id)

	def toString(self):
		kids =" ".join(str(elem) for elem in self.children)
		return "Node : " + str(self.id) + " |  Type : decorator" + " | children : " + kids

	def tick(self, predecessor : "Node"):
		BT.BT.getBT().logger.log("Ticking : " + self.toString())

		#if we come from a child node
		if (predecessor.Node in self.children):

			#if this child is true, we re-execute the child
			if(predecessor.Node.status == State.SUCCESS):
				self.status = State.RUNNING
				self.parent.tick(self)

			#else if this child is false we exit
			elif(len(self.children) >= 1):
					self.status = State.SUCCESS
					self.children[0].tick(self)
		
		else:

			#we check the first child (if it has one)
			if(len(self.children)>0):
				self.children[0].tick(self)
				self.statut = State.RUNNING

			else:
				self.parent.tick(self)
				self.statut = State.FAILURE


