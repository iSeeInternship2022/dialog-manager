import json
from typing import Dict
import Data.Data_Parser.TreeParser as TreeParser
from Buisiness.BT.structure.nodes.Node import Node
from Buisiness.BT.structure.nodes.RootNode import RootNode
import Buisiness.BT.structure.nodes.NodeFactory as maker
import Buisiness.BT.structure.nodes.NodeType as nt
import Buisiness.BT.structure.Tree as Tree 


def generateTree(path) :

	parser = TreeParser.TreeParser(path)
	nodes : Dict[str, Node] = {}

	#For each node in the JSON
	for node_id in parser.BT_nodes:

		#print(json.dumps(parser.BT_nodes[node_id]["name"]))
		type = parser.BT_nodes[node_id]["name"]
		id = parser.BT_nodes[node_id]["id"]
		label = parser.BT_nodes[node_id]["title"]

		#create Node according to its type with factory
		currentNode = maker.makeNode(type, id, label)
		nodes[node_id] = currentNode

	
	#Do a second round to add the children now that every node is created
	for n in parser.BT_nodes:

		#Only add child to nodes that have children
		if(parser.BT_nodes[n]["name"] == "Priority" 
		or parser.BT_nodes[n]["name"] == "Sequence"):
			for i in parser.BT_nodes[n]["children"]:
				nodes.get(n).children.append(nodes.get(i))

		if(parser.BT_nodes[n]["name"] == "RepeatUntilSuccess"
		or parser.BT_nodes[n]["name"] == "RepeatUntilFailure"):
			child = parser.BT_nodes[n]["child"]
			nodes.get(n).children.append(nodes.get(child))
	

	#make the root a RootNode and attach the first node
	root_id = parser.BT_root
	root = RootNode('0')
	root.children.append(nodes.get(root_id))
	nodes.get(root_id).parent = root


	for n in nodes.values():
		for c in n.children:
			c.parent = n

	# for n in nodes:
	# 	print(n.toString())

	return Tree.Tree(root, nodes)