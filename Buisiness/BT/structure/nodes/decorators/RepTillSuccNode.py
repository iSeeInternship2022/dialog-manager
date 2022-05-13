from  Buisiness.BT.structure.nodes.Node import Node
from  Buisiness.BT.structure.nodes.StateType import StateType as State
import  Buisiness.BT.BT as BT

class RepTillSuccNode(Node) :
	def __init__(self, id) -> None:
		super().__init__(id)

	def toString(self):
		kids =" ".join(str(elem) for elem in self.children)
		return ( "REP TILL SUCC "+str(self.status) + " " + str(self.id))

	def tick(self, predecessor : "Node"):
		BT.BT.getBT().logger.log("open " +self.toString())

		
		if (not (predecessor in self.children)):

			#we check the first child (if it has one)
			if(len(self.children)>0):
				#print("go in first child")
				self.statut = State.RUNNING
				self.children[0].tick(self)
				

			else:
				#print("no child")
				self.statut = State.FAILURE


		else:
			while(self.status == State.FAILURE):
				
				self.status = self.children[0].tick(self)

		BT.BT.getBT().logger.log("closed " +self.toString())
		return self.status


	def reset(self):
		self.status = State.FAILURE
		for child in self.children:
			child.reset()


