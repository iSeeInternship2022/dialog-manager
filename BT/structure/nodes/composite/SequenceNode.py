from turtle import st
from structure.nodes.Node import Node
from structure.nodes.StateType import StateType as State
import BT


class SequenceNode(Node) :
	def __init__(self, id) -> None:
		super().__init__(id)
		
	def toString(self):
		kids =" "+ (str(len(self.children)))
		return ( "SEQUENCE "+str(self.status) + " " + str(self.id))

	def tick(self, predecessor : "Node"):
		BT.BT.getBT().logger.log("open " +self.toString())

		#if we come from a child node

		if (not(predecessor in self.children)):

			#we check the first child (if it has one)
			if(len(self.children)>0):
				#print("we check the first child (if it has one)")
				self.status = State.RUNNING
				self.children[0].tick(self)
				

			else:
				#succeed when it has no child
				#print("succeed when it has no child")
				self.status = State.SUCCESS
			



		self.status = State.SUCCESS
		for child in self.children:
			if(child.tick(self) == State.FAILURE):
				self.status = State.FAILURE
				break

		#back to parents node
		BT.BT.getBT().logger.log("closed " +self.toString())
		return self.status

				

