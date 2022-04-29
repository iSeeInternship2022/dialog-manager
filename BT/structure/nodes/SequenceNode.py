import structure.nodes.Node as Node



class SequenceNode(Node.Node) :
	def __init__(self, id) -> None:
		super().__init__(id)
		
	def toString(self):
		kids =" ".join(str(elem) for elem in self.children)
		return ("Node : " + str(self.id) + " |  Type : sequence" + " | children : " + kids)

	def goToNext(self, predecessor : "Node"):

		#if we come from a child node
		if (predecessor.Node in self.children):

			#if the child is true but has unchecked siblings
			if(predecessor.Node.status == 'True' and self.children.index(predecessor.Node.id) < self.children.count()-1):
				self.children[self.children.index(predecessor.Node.id)+1].goToNext(self)
				self.status = 'Running'

			#if this child is true, and it's the last child
			elif(predecessor.Node.status == 'True'):
				self.status = 'True'
				self.parent.goToNext(self)

			#else if this child is false the sequence fails, we exit the node returning false
			else:
					self.status = 'False'
					self.parent.goToNext(self)


		else:

			#we check the first child (if it has one)
			if(self.children.count()>0):
				self.children[0].goToNext(self)
				self.statut = 'Running'

			else:
				self.parent.goToNext(self)
				self.statut = 'False'

