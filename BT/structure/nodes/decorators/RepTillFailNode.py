from structure.nodes.Node import Node
from structure.nodes.StateType import StateType as State
import BT

class RepTillFailNode(Node) :
	def __init__(self, id) -> None:
		super().__init__(id)

	def toString(self):
		kids =" ".join(str(elem) for elem in self.children)
		return ( "REP TILL FAIL "+str(self.status) + " " + str(self.id))

	def tick(self, predecessor : "Node"):
		BT.BT.getBT().logger.log(self.toString())

		#if we come from a child node
		if (predecessor in self.children):

			#if this child is true, we re-execute the child
			if(predecessor.status == State.SUCCESS):
				self.status = State.RUNNING
				self.parent.tick(self)

			#else if this child is false we exit
			elif(len(self.children) >= 1):
					self.status = State.SUCCESS
					self.children[0].tick(self)
		
		else:

			#we check the first child (if it has one)
			if(len(self.children)>0):
				self.statut = State.RUNNING
				self.children[0].tick(self)
				

			else:
				self.statut = State.FAILURE
				self.parent.tick(self)
				


