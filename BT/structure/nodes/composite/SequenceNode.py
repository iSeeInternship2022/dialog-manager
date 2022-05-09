from structure.nodes.Node import Node
from structure.nodes.StateType import StateType as State
import BT


class SequenceNode(Node) :
	def __init__(self, id) -> None:
		super().__init__(id)
		
	def toString(self):
		kids =" "+ (str(len(self.children)))
		return ("Node : " + str(self.id) + " |  Type : sequence" + " | children : " + kids)

	def tick(self, predecessor : "Node"):
		BT.BT.getBT().logger.log("Ticking : " + self.toString())

		#if we come from a child node

		if (predecessor.id in self.children):

			#if the child is true but has unchecked siblings
			if(predecessor.status == State.SUCCESS and self.children.index(predecessor.id) < self.children.count()-1):
				self.status = State.RUNNING
				self.children[self.children.index(predecessor.id)+1].tick(self)
				

			#if this child is true, and its the last child
			elif(predecessor.status == State.SUCCESS):
				self.status = State.SUCCESS
				self.parent.tick(self)

			#else if this child is false the sequence fails, we exit the node returning false
			else:
					self.status = State.FAILURE
					self.parent.tick(self)


		else:

			#we check the first child (if it has one)
			if(len(self.children)>0):
				self.status = State.RUNNING
				self.children[0].tick(self)
				

			else:
				#succeed when it has no child
				self.status = State.SUCCESS
				self.parent.tick(self)
				

