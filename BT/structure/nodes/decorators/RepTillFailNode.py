from structure.nodes.Node import Node



class RepTillFailNode(Node) :
	def __init__(self, id) -> None:
		super().__init__(id)

	def toString(self):
		kids =" ".join(str(elem) for elem in self.children)
		return "Node : " + str(self.id) + " |  Type : decorator" + " | children : " + kids

	def tick(self, predecessor : "Node"):
		print("Ticking : " + self.toString())

		#if we come from a child node
		if (predecessor.Node in self.children):

			#if this child is true, we re-execute the child
			if(predecessor.Node.status == 'True'):
				self.status = 'Running'
				self.parent.tick(self)

			#else if this child is false we exit
			elif(len(self.children) >= 1):
					self.status = 'True'
					self.children[0].tick(self)
		
		else:

			#we check the first child (if it has one)
			if(len(self.children)>0):
				self.children[0].tick(self)
				self.statut = 'Running'

			else:
				self.parent.tick(self)
				self.statut = 'False'


