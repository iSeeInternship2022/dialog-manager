import structure.nodes.Node as Node



class PriorityNode(Node.Node) :
	def __init__(self, id) -> None:
		super().__init__(id)

	def toString(self):
		kids =" ".join(str(elem) for elem in self.children)
		return "Node : " + str(self.id) + " |  Type : priority" + " | children : " + kids

	def goToNext(self, predecessor : "Node"):

		#if we come from a child node
		if (predecessor.Node in self.children):

			#if this child is true, we can exit this node returning true
			if(predecessor.Node.status == 'True'):
				self.status = 'True'
				self.parent.goToNext(self)

			#else if this child is false and the last one, we exit the node returning false
			elif(self.children.index(predecessor.Node.id) == self.children.count()-1):
					self.status = 'False'
					self.parent.goToNext(self)

			#else if this child is false but not the last, we check its next sibling
			else:
				self.children[self.children.index(predecessor.Node.id)+1].goToNext(self)
				self.status = 'Running'
		
		else:

			#we check the first child (if it has one)
			if(self.children.count()>0):
				self.children[0].goToNext(self)
				self.statut = 'Running'

			else:
				self.parent.goToNext(self)
				self.statut = 'False'


