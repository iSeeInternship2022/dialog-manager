from cProfile import label
import threading
import Buisiness.BT.BT as BT
import Buisiness.BT.structure.nodes.Node as Node
from  Buisiness.BT.structure.reactions.Actions import do_action
from  Buisiness.BT.structure.nodes.StateType import StateType as State
import Buisiness.Coordinator.Coordinator as C

class InformationNode(Node.Node) :
	def __init__(self, id) -> None:
		super().__init__(id)
		self.message = None

	def toString(self):
		return ( "message "+str(self.status) + " " + str(self.id) + " " + self.message)

	def tick(self, predecessor : "Node"):

		BT.BT.getBT().logger.log("open " +self.toString())

		# if(self.status == State.RUNNING):
		# 	if(not self.thread.is_alive()):
		# 		self.status = State.SUCCESS
		# else:
			# self.status = State.RUNNING
			# self.thread = threading.Thread(target=do_action, args=("send_message", self.message,))
			# self.thread.start()
			
		C.Coordinator.get().inform(self.message)
		self.status = State.SUCCESS
		BT.BT.getBT().logger.log("closed " +self.toString())
		return self.status
	
	def reset(self):
		if(self.status == State.SUCCESS):
			self.status = State.FAILURE


