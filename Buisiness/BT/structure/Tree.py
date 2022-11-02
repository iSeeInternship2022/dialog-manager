from typing import Dict

from yaml import SequenceNode
import Buisiness.BT.structure.nodes.Node as Node
from Buisiness.BT.structure.nodes.composite.PriorityNode import PriorityNode

class Tree :
	def __init__(self, root : Node, nodes : Dict[str, Node.Node]) -> None:
		self.root = root
		self.nodes = nodes
		
	def plug_in(self, plug_root, plug_in_node, subTree):

		socket_node = self.nodes.get(plug_in_node.id)
		info_parent = self.findParent(socket_node)
		socket_parent = info_parent[0]

		if(info_parent[1] == -1):
			socket_parent.child = plug_root
		else:
			pass
		
		#sub_root = SequenceNode(plug_root.id)
		#sub_root.children.append(subTree.nodes.get(root_id))

	def findParent(self, node):
		res = None
		for n in self.nodes:
			if(hasattr(self.nodes[n], "children")):
				for child in self.nodes[n].children :
					if(child == node):
						res = self.nodes[n]
			elif(hasattr(self.nodes[n], "child")):
				if(self.nodes[n].child == node):
					res = self.nodes[n]
		return res


	#replace a child of a given parent by a new child given with the same id
	def replaceChild(self, parent, new_child):
		if(hasattr(parent, "children")):
			index = 0
			for child in parent.children :
				if(child.id == new_child.id):
					parent.children[index] = new_child
				index += 1
		elif(hasattr(parent, "child")):
			parent.child = new_child




def printTree(root, level=0):
	print(" - " * level, root.toString())
	if(hasattr(root, "children")):
		for child in root.children:
			printTree(child, level + 1)
	elif(hasattr(root, "child")):
		printTree(root.child, level+1)

