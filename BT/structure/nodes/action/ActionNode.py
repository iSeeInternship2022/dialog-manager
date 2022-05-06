from cProfile import label
import threading
import BT
import structure.nodes.Node as Node
from structure.reactions.Actions import do_action

class ActionNode(Node.Node) :
	def __init__(self, id, label) -> None:
		super().__init__(id)
		self.action = label
		self.thread = None

	def toString(self):
		return ("Node : " + str(self.id) + " |  Type : action |  Label : " + self.action)

	def tick(self, predecessor : "Node"):
		print("Ticking : " + self.toString())


		if(self.status == 'Running'):
			if(self.thread.is_alive()):
				BT.getBT().tree.root.tick(self)
			else:
				self.status = 'Success'
				self.parent.tick(self)

		else:
			self.thread = threading.Thread(target=do_action, args=(self.action,))
			self.thread.start()
			self.status = 'Running'
			BT.getBT().tree.root.tick(self)
