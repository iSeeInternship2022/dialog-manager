from  Buisiness.BT.structure.nodes.Node import Node
from  Buisiness.BT.structure.nodes.StateType import StateType as State
import  Buisiness.BT.BT as BT

class RepTillSuccNode(Node) :
	def __init__(self, id) -> None:
		super().__init__(id)
		self.child = None

	def toString(self):
		return ( "REP TILL SUCC "+str(self.status) + " " + str(self.id))

	def tick(self, predecessor : "Node"):

		
		if (not (predecessor in self.child)):

			#we check the first child (if it has one)
			if(len(self.child)>0):
				#print("go in first child")
				self.statut = State.RUNNING
				self.child[0].tick()
				

			else:
				#print("no child")
				self.statut = State.FAILURE


		else:
			while(self.status == State.FAILURE):
				
				self.status = self.child[0].tick()

		return self.status


	def reset(self):
		self.status = State.FAILURE
		self.child.reset()


