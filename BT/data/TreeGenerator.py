import json
from typing import Dict
import data.TreeParser as TreeParser
from structure.nodes.Node import Node
from structure.nodes.RootNode import RootNode
import structure.nodes.NodeFactory as maker
import structure.nodes.NodeType as nt
import structure.Tree as Tree 

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

		#Only add child to priority and sequence nodes
		if(parser.BT_nodes[n]["name"] == "Priority" or parser.BT_nodes[n]["name"] == "Sequence"):
			for i in parser.BT_nodes[n]["children"]:
				nodes.get(n).children.append(nodes.get(i))
	

	#make the root a RootNode and attach the first node
	root_id = parser.BT_root
	root = RootNode('0')
	root.children[0] = nodes.get(root_id)


	for n in nodes.values():
		for c in n.children:
			c.parent = n

	# for n in nodes:
	# 	print(n.toString())

	return Tree.Tree(root, nodes)