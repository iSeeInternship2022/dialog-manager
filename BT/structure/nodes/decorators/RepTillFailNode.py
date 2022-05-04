from structure.nodes.Node import Node



class RepTillFailNode(Node) :
	def __init__(self, id) -> None:
		super().__init__(id)

	def toString(self):
		kids =" ".join(str(elem) for elem in self.children)
		return "Node : " + str(self.id) + " |  Type : priority" + " | children : " + kids

	def goToNext(self, predecessor : "Node"):

		#if we come from a child node
		if (predecessor.Node in self.children):

			#if this child is true, we re-execute the child
			if(predecessor.Node.status == 'True'):
				self.status = 'Running'
				self.parent.goToNext(self)

			#else if this child is false we exit
			elif(self.children.count() >= 1):
					self.status = 'True'
					self.children[0].goToNext(self)
		
		else:

			#we check the first child (if it has one)
			if(self.children.count()>0):
				self.children[0].goToNext(self)
				self.statut = 'Running'

			else:
				self.parent.goToNext(self)
				self.statut = 'False'


