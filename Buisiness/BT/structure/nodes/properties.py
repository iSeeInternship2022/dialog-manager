from enum import Enum

class Properties(str, Enum):
	#question node
	QUESTION = "question_slot",
	ANSWER = "answer_slot",

	#information node
	MESSAGE = "message_slot",

	#World modifier
	DATA_TO_MODIFY = "data_slot",
	VALUE = "value",

	#limit decorator
	LIMIT = "maxLoop",

	#API (Explanation experience)
	TYPE = "type",
	URL = "url",
	SAVE = "save_slot",

	#Equal
	DATA_IS_EQUAL = "data_equal",
	EQUAL_TO_VALUE = "is_equal_to",

	#Condition
	DATA_CONDITION = "data_slot"


