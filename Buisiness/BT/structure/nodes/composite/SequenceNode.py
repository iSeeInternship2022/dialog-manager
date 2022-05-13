from  Buisiness.BT.structure.nodes.Node import Node
from  Buisiness.BT.structure.nodes.StateType import StateType as State
import Buisiness.BT.BT as BT


class SequenceNode(Node) :
	def __init__(self, id) -> None:
		super().__init__(id)
		
	def toString(self):
		kids =" "+ (str(len(self.children)))
		return ( "SEQUENCE "+str(self.status) + " " + str(self.id))

	def tick(self, predecessor : "Node"):
		BT.BT.getBT().logger.log("open " +self.toString())

		
		self.status = State.SUCCESS
		for child in self.children:
			if(child.tick(self) == State.FAILURE):
				self.status = State.FAILURE
				break

		#back to parents node
		BT.BT.getBT().logger.log("closed " +self.toString())
		return self.status

	def reset(self):
		self.status = State.FAILURE
		for child in self.children:
			child.reset()

