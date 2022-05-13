from  Buisiness.BT.structure.nodes.Node import Node
from  Buisiness.BT.structure.nodes.StateType import StateType as State
import Buisiness.BT.BT as BT

class PriorityNode(Node) :
	def __init__(self, id) -> None:
		super().__init__(id)

	def toString(self):
		kids =" " + (str(len(self.children)))
		return ( "PRIORITY "+str(self.status) + " " + str(self.id))

	def tick(self, predecessor : "Node"):
		BT.BT.getBT().logger.log("open " +self.toString())



		for child in self.children:
			if(child.tick(self) == State.SUCCESS):
				self.status = State.SUCCESS
				break


		BT.BT.getBT().logger.log("closed " +self.toString())
		return self.status
			#back to parents node
				

	def reset(self):
		self.status = State.FAILURE
		for child in self.children:
			child.reset()

