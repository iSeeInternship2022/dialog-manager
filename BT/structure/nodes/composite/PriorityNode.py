from structure.nodes.Node import Node
from structure.nodes.StateType import StateType as State
import BT

class PriorityNode(Node) :
	def __init__(self, id) -> None:
		super().__init__(id)

	def toString(self):
		kids =" " + (str(len(self.children)))
		return ( "PRIORITY "+str(self.status) + " " + str(self.id))

	def tick(self, predecessor : "Node"):
		BT.BT.getBT().logger.log(self.toString())

		#if we come from a child node
		if (predecessor in self.children):

			#if this child is true, we can exit this node returning true
			if(predecessor.status == State.SUCCESS):
				self.status = State.SUCCESS
				self.parent.tick(self)

			#else if this child is false and the last one, we exit the node returning false
			elif(self.children.index(predecessor) == len(self.children)-1):
					self.status = State.FAILURE
					self.parent.tick(self)

			#else if this child is false but not the last, we check its next sibling
			else:
				self.status = State.RUNNING
				self.children[self.children.index(predecessor)+1].tick(self)
				
		
		else:

			#we check the first child (if it has one)
			if(len(self.children)>0):
				self.status = State.RUNNING
				self.children[0].tick(self)
				

			else:
				self.status = State.FAILURE
				self.parent.tick(self)
				


