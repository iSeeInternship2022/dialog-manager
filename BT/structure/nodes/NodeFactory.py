from regex import R
import structure.nodes.NodeType as nt
import structure.nodes.action.ActionNode as Action
import structure.nodes.ConditionNode as Decision
import structure.nodes.composite.PriorityNode as Priority
import structure.nodes.composite.SequenceNode as Sequence
import structure.nodes.Node as Node


def makeNode(type, id, label) :
	res = Node.Node(0)

	if type == "Succeeder":
		res = Action.ActionNode(id, label)
	elif type == "Evaluation Method":
		res = Decision.ConditioNode(id, label)
	elif type == "Priority":
		res = Priority.PriorityNode(id)
	elif type == "Sequence":
		res = Sequence.SequenceNode(id)
	else :
		print("no type")

	return res


	# switcher = {
    # 	nt.NodeType.action: Action.ActionNode.__init__(id, label),
    # 	nt.NodeType.decision: Decision.ConditionNode.__init__(id, label),
    # 	nt.NodeType.priority: Priority.PriorityNode.__init__(id),
	# 	nt.NodeType.sequence: Sequence.SequenceNode.__init__(id),
    # }
	# return switcher.get(type, "This type doesn't exist")

