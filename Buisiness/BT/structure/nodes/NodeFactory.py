
from Buisiness.BT.structure.nodes.Condition.EqualNode import EqualNode
import Buisiness.BT.structure.nodes.action.ActionNode as Action
import Buisiness.BT.structure.nodes.Condition.ConditionNode as Decision
from Buisiness.BT.structure.nodes.action.ComputingNode import ComputingNode
from Buisiness.BT.structure.nodes.action.InformationNode import InformationNode
from Buisiness.BT.structure.nodes.action.QuestionNode import QuestionNode
from Buisiness.BT.structure.nodes.action.Succeeder import Succeder
from Buisiness.BT.structure.nodes.action.WorldModifierNode import WorldModifierNode
import Buisiness.BT.structure.nodes.composite.PriorityNode as Priority
import Buisiness.BT.structure.nodes.composite.SequenceNode as Sequence
from Buisiness.BT.structure.nodes.decorators.LimitActivationNode import LimitActivationNode
import Buisiness.BT.structure.nodes.decorators.RepTillFailNode as TillFail
import Buisiness.BT.structure.nodes.decorators.RepTillSuccNode as TillSucc
import Buisiness.BT.structure.nodes.Node as Node


def makeNode(type, id, label) :
	res = Node.Node(0)

	#Should have their own node type, using available types as a replacement for now
	if type == "Explanation Method":
		res = WorldModifierNode(id)

	elif type == "Failer":
		res = QuestionNode(id)

	elif type == "Succeeder":
		res = InformationNode(id)

	elif type == "Inverter":
		res = Action.ActionNode(id, label)

	elif type == "Repeater":
		res = EqualNode(id)

	elif type == "Evaluation Method":
		res = Decision.ConditionNode(id)
	elif type == "Priority":
		res = Priority.PriorityNode(id)
	elif type == "Sequence":
		res = Sequence.SequenceNode(id)
	elif type == "RepeatUntilFailure":
		res = TillFail.RepTillFailNode(id)
	elif type == "RepeatUntilSuccess":
		res = TillSucc.RepTillSuccNode(id)
	elif type == "Limiter":
		res = LimitActivationNode(id)
			
	else :
		print("no type")

	return res



