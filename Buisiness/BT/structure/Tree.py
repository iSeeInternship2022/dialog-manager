from typing import Dict
import Buisiness.BT.structure.nodes.Node as Node

class Tree :
	def __init__(self, root : Node, nodes : Dict[str, Node.Node]) -> None:
		self.root = root
		self.nodes = nodes
		self.currentNode = root


	def goToNextDepthFirst() :
		pass

def printTree(root, level=0):
	print(" - " * level, root.toString())
	for child in root.children:
		printTree(child, level + 1)