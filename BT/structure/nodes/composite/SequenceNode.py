from structure.nodes.Node import Node



class SequenceNode(Node) :
	def __init__(self, id) -> None:
		super().__init__(id)
		
	def toString(self):
		kids =" ".join(str(elem) for elem in self.children)
		return ("Node : " + str(self.id) + " |  Type : sequence" + " | children : " + kids)

	def tick(self, predecessor : "Node"):
		print("Ticking : " + self.toString())

		#if we come from a child node
		if(predecessor != None):	#this line should be useless
			if (predecessor in self.children):

				#if the child is true but has unchecked siblings
				if(predecessor.status == 'True' and self.children.index(predecessor.id) < self.children.count()-1):
					self.status = 'Running'
					self.children[self.children.index(predecessor.id)+1].tick(self)
					

				#if this child is true, and it's the last child
				elif(predecessor.status == 'True'):
					self.status = 'True'
					self.parent.tick(self)

				#else if this child is false the sequence fails, we exit the node returning false
				else:
						self.status = 'False'
						self.parent.tick(self)


		else:

			#we check the first child (if it has one)
			if(len(self.children)>0):
				self.status = 'Running'
				self.children[0].tick(self)
				

			else:
				self.status = 'False'
				self.parent.tick(self)
				

