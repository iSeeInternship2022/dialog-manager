import json
from typing import Dict

from yaml import SequenceNode
from Buisiness.BT.structure.nodes.Condition.ConditionNode import ConditionNode
from Buisiness.BT.structure.nodes.Condition.EqualNode import EqualNode
from Buisiness.BT.structure.nodes.action.ExplanationExpType import ExplanationExp
from Buisiness.BT.structure.nodes.action.ExplanationExperienceNode import ExplanationExperienceNode
from Buisiness.BT.structure.nodes.action.InformationNode import InformationNode
from Buisiness.BT.structure.nodes.action.QuestionNode import QuestionNode
from Buisiness.BT.structure.nodes.action.WorldModifierNode import WorldModifierNode
from Buisiness.BT.structure.nodes.composite.PriorityNode import PriorityNode
from Buisiness.BT.structure.nodes.decorators.InverterNode import InverterNode
from Buisiness.BT.structure.nodes.decorators.LimitActivationNode import LimitActivationNode
from Buisiness.BT.structure.nodes.decorators.RepTillFailNode import RepTillFailNode
from Buisiness.BT.structure.nodes.decorators.RepTillSuccNode import RepTillSuccNode
import Data.Data_Parser.TreeParser as TreeParser
from Buisiness.BT.structure.nodes.Node import Node
from Buisiness.BT.structure.nodes.RootNode import RootNode
import Buisiness.BT.structure.nodes.NodeFactory as maker
import Buisiness.BT.structure.nodes.NodeType as nt
import Buisiness.BT.structure.Tree as Tree 

#To assign properties of PRIORITY or SEQUENCE nodes
def makeCompositeNode(node, parsed_tree, node_list):
		for child_id in parsed_tree.BT_nodes[node.id]["children"]:
				node.children.append(node_list.get(child_id))

#To assign properties of INVERTER or REPEATER nodes
def makeSimpleDecorator(node, parsed_tree, node_list):
	child_id = parsed_tree.BT_nodes[node.id]["child"]
	node.child = node_list.get(child_id)

#To assign properties of Limit activations nodes
def makeLimitActivation(node, parsed_tree, node_list):
	child_id = parsed_tree.BT_nodes[node.id]["child"]
	node.child = node_list.get(child_id)

	node.limit = getProperty("maxloop", node, parsed_tree)

#To assign properties of Equal nodes
def makeEqualNode(node, parsed_tree):
	node.data_slot = getProperty("dataslot", node, parsed_tree)
	val = getProperty("value", node, parsed_tree)
	node.value = toBool(val)

#To assign properties of Condition nodes
def makeConditionNode(node, parsed_tree):
	node.data_slot = getProperty("dataslot", node, parsed_tree)

#To assign properties of Explanation Experience nodes
def makeExplanationExperienceNode(node, parsed_tree):
	node.url = getProperty("url", node, parsed_tree)
	node.data_slot = getProperty("data_slot", node, parsed_tree)

	if(getProperty("type", node, parsed_tree) == "tree plug-in"):
		node.type = ExplanationExp.TREE
	else :
		node.type = ExplanationExp.EXPLANATION

#To assign properties of Information nodes
def makeInformationNode(node, parsed_tree):
	node.message_slot = getProperty("message_slot", node, parsed_tree)

#To assign properties of Question nodes
def makeQuestionNode(node, parsed_tree):
	node.question_slot = getProperty("question_slot", node, parsed_tree)
	node.answer_slot = getProperty("answer_slot", node, parsed_tree)

#To assign properties of World Modifier nodes
def makeWorldModifierNode(node, parsed_tree):
	node.data_slot = getProperty("dataslot", node, parsed_tree)
	val = getProperty("value", node, parsed_tree)
	node.value = toBool(val)

#get a node property for the parsed_tree
def getProperty(prop_name, node, parsed_tree):
	return parsed_tree.BT_nodes[node.id]["properties"][prop_name]

#Turns a boolean string to a true boolean
def toBool(val):
	if(val == "True" or val == "False"):
		val = bool(val)
	return val


#generates all the tree nodes (given in the parsed tree) of the right type, but empty (no children or properties)
def generateNodes(parsed_tree, nodes):
		#For each node in the JSON
	for node_id in parsed_tree.BT_nodes:

		#print(json.dumps(parsed_tree.BT_nodes[node_id]["name"]))
		type = parsed_tree.BT_nodes[node_id]["name"]
		id = parsed_tree.BT_nodes[node_id]["id"]
		label = parsed_tree.BT_nodes[node_id]["title"]

		#create Node according to its type with factory
		currentNode = maker.makeNode(type, id)
		nodes[node_id] = currentNode


#give the nodes their missing properties and children
def giveNodesProperties(parsed_tree, nodes):
	for n in nodes:

		#====== COMPOSITE ======
		if(type(n) is SequenceNode 
		or type(n) is PriorityNode):
			makeCompositeNode(n, parsed_tree, nodes)


		#====== DECORATOR ======
		elif(type(n) is RepTillFailNode
		or type(n) is RepTillSuccNode
		or type(n) is InverterNode):
			makeSimpleDecorator(n, parsed_tree, nodes)

		elif(type(n) is LimitActivationNode):
			makeLimitActivation(n, parsed_tree, nodes)


		#====== CONDITION ======
		elif(type(n) is EqualNode):
			makeEqualNode(n, parsed_tree)

		elif(type(n) is ConditionNode):
			makeConditionNode(n, parsed_tree)


		#====== ACTION ======
		elif(type(n) is ExplanationExperienceNode):
			makeExplanationExperienceNode(n, parsed_tree)

		elif(type(n) is InformationNode):
			makeInformationNode(n, parsed_tree)

		elif(type(n) is QuestionNode):
			makeQuestionNode(n, parsed_tree)

		elif(type(n) is WorldModifierNode):
			makeWorldModifierNode(n, parsed_tree)

def generateTree(path) :

	parsed_tree = TreeParser.TreeParser(path)
	nodes : Dict[str, Node] = {}

	generateNodes(parsed_tree, nodes)

	#Do a second round to add the children and the properties now that every node is created
	giveNodesProperties(parsed_tree, nodes)
	
	#make the root a RootNode and attach the first node
	root_id = parsed_tree.BT_root
	root = RootNode('0')
	root.children.append(nodes.get(root_id))

	return Tree.Tree(root, nodes)

def generateSubTree(tree, root, path, plug_in_node):
	parsed_tree = TreeParser.TreeParser(path)
	nodes : Dict[str, Node] = {}

	generateNodes(parsed_tree, nodes)

	#Do a second round to add the children and the properties now that every node is created
	giveNodesProperties(parsed_tree, nodes)

	subTree = Tree.Tree(root, nodes)

	tree.plug_in(root, plug_in_node, subTree)