import threading
import Buisiness.BT.BT as BT
import Buisiness.BT.structure.nodes.Node as Node
from  Buisiness.BT.structure.reactions.Actions import do_action
from  Buisiness.BT.structure.nodes.StateType import StateType as State

class ActionNode(Node.Node) :
	def __init__(self, id, label) -> None:
		super().__init__(id)
		self.action = label
		self.thread = None

	def toString(self):
		return ( "ACTION "+str(self.status) + " " + str(self.id) + " " + self.action)

	def tick(self):



		if(self.status == State.RUNNING):
			if(not self.thread.is_alive()):
				self.status = State.SUCCESS
		else:
			self.status = State.RUNNING
			self.thread = threading.Thread(target=do_action, args=(self.action,))
			self.thread.start()
		
		return self.status
	
	def reset(self):
		if(self.status == State.SUCCESS):
			self.status = State.FAILURE
