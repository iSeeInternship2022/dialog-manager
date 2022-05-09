from structure.nodes.Node import Node
from structure.nodes.StateType import StateType as State
import BT

class RepTillSuccNode(Node) :
	def __init__(self, id) -> None:
		super().__init__(id)

	def toString(self):
		kids =" ".join(str(elem) for elem in self.children)
		return ( "REP TILL SUCC "+str(self.status) + " " + str(self.id))

	def tick(self, predecessor : "Node"):
		BT.BT.getBT().logger.log(self.toString())

		#if we come from a child node
		if (predecessor in self.children):

			#if this child is true, yay, we exit to the parent
			if(predecessor.status == State.SUCCESS):
				#print("success, yay!")
				self.status = State.RUNNING
				self.parent.tick(self)

			#else if this child is false re execute
			elif(len(self.children) >= 1):
					#print("failed : re-executing child")
					self.status = State.SUCCESS
					self.children[0].tick(self)
		
		else:

			#we check the first child (if it has one)
			if(len(self.children)>0):
				#print("go in first child")
				self.statut = State.RUNNING
				self.children[0].tick(self)
				

			else:
				#print("no child")
				self.statut = State.FAILURE
				self.parent.tick(self)
				


