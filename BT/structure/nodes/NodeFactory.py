from ctypes import Structure
from regex import R
import structure.nodes.NodeType as nt
import structure.nodes.action.ActionNode as Action
import structure.nodes.action.Succeeder as Succeder
import structure.nodes.ConditionNode as Decision
import structure.nodes.composite.PriorityNode as Priority
import structure.nodes.composite.SequenceNode as Sequence
import structure.nodes.decorators.RepTillFailNode as TillFail
import structure.nodes.decorators.RepTillSuccNode as TillSucc
import structure.nodes.Node as Node


def makeNode(type, id, label) :  
	res = Node.Node(0)

	if type == "Succeeder":
		res = Succeder.Succeder(id)
	elif type == "Evaluation Method":
		res = Decision.ConditionNode(id, label)
	elif type == "Explanation Method":
		res = Action.ActionNode(id, label)
	elif type == "Priority":
		res = Priority.PriorityNode(id)
	elif type == "Sequence":
		res = Sequence.SequenceNode(id)
	elif type == "RepeatUntilFailure":
		res = TillFail.RepTillFailNode(id)
	elif type == "RepeatUntilSuccess":
		res = TillSucc.RepTillSuccNode(id)
			
	else :
		print("no type")

	return res



