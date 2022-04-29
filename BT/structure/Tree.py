from typing import Dict
import structure.nodes.Node as Node

class Tree :
	def __init__(self, root : Node, nodes : Dict[str, Node.Node]) -> None:
		self.root = root
		self.nodes = nodes
		self.currentNode = root


	def goToNextDepthFirst() :
		pass

	def print_tree(self):
		node_str = ""
		i = 0

		for k in self.nodes.keys():
			print("\rNode " + str(i) + ":" + self.nodes.get(k).toString())
			i += 1
