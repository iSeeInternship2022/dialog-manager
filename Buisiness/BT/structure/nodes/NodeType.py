from enum import Enum

class NodeType(Enum):
	ACTION = 1
	CONDITION = 2
	PRIORITY = 3
	SEQUENCE = 4
	REPTILLFAIL = 5
	REPTILLSUCC = 6
	REPX = 7
	INVERTER = 8
	LIMITXACTIVATION = 9
	SUCCEEEDER = 10
	FAILER = 11
	EXPLANATIONEXP = 12