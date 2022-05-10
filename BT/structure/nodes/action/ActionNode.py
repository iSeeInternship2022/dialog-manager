from cProfile import label
import threading
import BT
import structure.nodes.Node as Node
from structure.reactions.Actions import do_action
from structure.nodes.StateType import StateType as State

class ActionNode(Node.Node) :
	def __init__(self, id, label) -> None:
		super().__init__(id)
		self.action = label
		self.thread = None

	def toString(self):
		return ( "ACTION "+str(self.status) + " " + str(self.id) + " " + self.action)

	def tick(self, predecessor : "Node"):

		BT.BT.getBT().logger.log("open " +self.toString())


		if(self.status == State.RUNNING):
			if(not self.thread.is_alive()):
				self.status = State.SUCCESS

		else:
			self.status = State.RUNNING
			self.thread = threading.Thread(target=do_action, args=(self.action,))
			self.thread.start()
		
		BT.BT.getBT().logger.log("closed " +self.toString())
		return self.status
			
