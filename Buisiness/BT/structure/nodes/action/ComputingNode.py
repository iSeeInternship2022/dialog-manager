import Buisiness.BT.BT as BT
import Buisiness.BT.structure.nodes.Node as Node
from  Buisiness.BT.structure.nodes.StateType import StateType as State
import Buisiness.Coordinator.Coordinator as C

class ComputingNode(Node.Node) :
	def __init__(self, id) -> None:
		super().__init__(id)
		self.value = None
		self.data_slot = None

	def toString(self):
		return ( "message "+str(self.status) + " " + str(self.id))

	def tick(self):



		# if(self.status == State.RUNNING):
		# 	if(not self.thread.is_alive()):
		# 		self.status = State.SUCCESS
		# else:
			# self.status = State.RUNNING
			# self.thread = threading.Thread(target=do_action, args=("send_message", self.message,))
			# self.thread.start()

		C.Coordinator.get().modifyWorld(self.data_slot, self.value)
		self.status = State.SUCCESS

		return self.status
	
	def reset(self):
		if(self.status == State.SUCCESS):
			self.status = State.FAILURE


