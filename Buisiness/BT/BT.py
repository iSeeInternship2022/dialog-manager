from os import removedirs
from Buisiness.BT.structure.Tree import printTree
from Data.Data_Parser.TreeParser_str import TreeParser_str
from ui.Logger import Logger
import Buisiness.BT.structure.TreeGenerator as tg



class BT:

	def __init__(self):

		self.tree = tg.generateTree("Data\Data_Parser\dialog-BT.JSON")
		printTree(self.tree.root)

		#self.currentState = self.tree.root
		
		self.logger = Logger()
		self.coordinator = None
		self.removed_nodes = []


	def run(self):
		
		while(True):
			self.tree.root.tick()
		
	def restart(self):
		pass

	def plug_subtree(self, calling_node, rawjson):

		#generate subtree
		subtree = TreeParser_str.generateSubTree(rawjson)

		#keep old calling node stored in case we need to get it back (keeping the same id for both, so we know which node goes where)
		removed_node = self.tree.nodes[calling_node.id]
		self.removed_nodes.append(removed_node)
		subtree.root.id = calling_node.id 
		self.tree.nodes[calling_node.id] = subtree.root
		
		parent = self.tree.findParent(removed_node)
		self.tree.replaceChild(parent, subtree.root)

		
		
#WIP main

