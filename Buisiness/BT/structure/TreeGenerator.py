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
		or parser.BT_nodes[n]["name"] == "RepeatUntilFailure"
		or parser.BT_nodes[n]["name"] == "Limit <maxLoop> Activations"):
			child = parser.BT_nodes[n]["child"]
			nodes.get(n).children.append(nodes.get(child))

		#For question nodes and nodes that checks the world, we need to assign its data slot (where it has to look for the data it needs)
		if(parser.BT_nodes[n]["name"] == "Evaluation Method"
		or parser.BT_nodes[n]["name"] == "Failer"):
			nodes.get(n).data_slot = parser.BT_nodes[n]["properties"]["data_slot"]

		#Question nodes also needs to have the text of the question, for now its raw text, but it could be a type used for a querry in the future
		if(parser.BT_nodes[n]["name"] == "Failer"
		or parser.BT_nodes[n]["name"] == "Succeeder"):
			nodes.get(n).message = parser.BT_nodes[n]["properties"]["message"]
	
		#For WorldModifiers nodes, we also need the value that will be asigned to the variable
		if(parser.BT_nodes[n]["name"] == "Explanation Method"):
			val = parser.BT_nodes[n]["properties"]["value"]

			#Changing string for boolean values
			if(val == "True" or val == "False"):
				val = bool(val)

			nodes.get(n).value = val

		if(parser.BT_nodes[n]["name"] == "Limit <maxLoop> Activations"):
			nodes.get(n).limit = parser.BT_nodes[n]["properties"]["message"]

	#make the root a RootNode and attach the first node
	root_id = parser.BT_root
	root = RootNode('0')
	root.children.append(nodes.get(root_id))

	return Tree.Tree(root, nodes)