from regex import R
import structure.nodes.NodeType as nt
import structure.nodes.ActionNode as Action
import structure.nodes.DecisionNode as Decision
import structure.nodes.PriorityNode as Priority
import structure.nodes.SequenceNode as Sequence
import structure.nodes.Node as Node


def makeNode(type, id, label) :
	res = Node.Node(0)

	if type == "Succeeder":
		res = Action.ActionNode(id, label)
	elif type == "Evaluation Method":
		res = Decision.DecisionNode(id, label)
	elif type == "Priority":
		res = Priority.PriorityNode(id)
	elif type == "Sequence":
		res = Sequence.SequenceNode(id)
	else :
		print("no type")

	return res


	# switcher = {
    # 	nt.NodeType.action: Action.ActionNode.__init__(id, label),
    # 	nt.NodeType.decision: Decision.DecisionNode.__init__(id, label),
    # 	nt.NodeType.priority: Priority.PriorityNode.__init__(id),
	# 	nt.NodeType.sequence: Sequence.SequenceNode.__init__(id),
    # }
	# return switcher.get(type, "This type doesn't exist")

