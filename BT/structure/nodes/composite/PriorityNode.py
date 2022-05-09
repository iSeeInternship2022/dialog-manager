from structure.nodes.Node import Node
from structure.nodes.StateType import StateType as State
import BT

class PriorityNode(Node) :
	def __init__(self, id) -> None:
		super().__init__(id)

	def toString(self):
		kids =" " + (str(len(self.children)))
		return "Node : " + str(self.id) + " |  Type : priority" + " | children : " + kids

	def tick(self, predecessor : "Node"):
		BT.BT.getBT().logger.log("Ticking : " + self.toString())

		#if we come from a child node
		if (predecessor in self.children):

			#if this child is true, we can exit this node returning true
			if(predecessor.status == State.SUCCESS):
				self.status = State.SUCCESS
				self.parent.tick(self)

			#else if this child is false and the last one, we exit the node returning false
			elif(self.children.index(predecessor.id) == len(self.children)-1):
					self.status = State.FAILURE
					self.parent.tick(self)

			#else if this child is false but not the last, we check its next sibling
			else:
				self.children[self.children.index(predecessor.id)+1].tick(self)
				self.status = State.RUNNING
		
		else:

			#we check the first child (if it has one)
			if(len(self.children)>0):
				self.children[0].tick(self)
				self.status = State.RUNNING

			else:
				self.parent.tick(self)
				self.status = State.FAILURE


