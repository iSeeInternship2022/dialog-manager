

#will be replaced by a API query or else in near future




import Buisiness.Coordinator.Coordinator as C


def do_action(name):
	if(name == 'detect_intent'):
		detect_intent()
	else:
		print("ACTION NOT IMPLEMENTED")

		
def detect_intent():
	answer = C.Coordinator.checkWorld("user_answer")
	C.Coordinator.modifyWorld("intent_is_satisfaction", False)
	C.Coordinator.modifyWorld("intent_is_question", False)
	C.Coordinator.modifyWorld("intent_is_affirmation", False)
	C.Coordinator.modifyWorld("intent_is_argument", False)
	C.Coordinator.modifyWorld("intent_is_details", False)
	C.Coordinator.modifyWorld("intent_is_approval", False)
	C.Coordinator.modifyWorld("intent_is_refusal", False)

	if(answer == "Satisfied"):
		C.Coordinator.modifyWorld("intent_is_satisfaction", True)

	elif(answer == "Question"):
		C.Coordinator.modifyWorld("intent_is_question", True)

	elif(answer == "Affirm"):
		C.Coordinator.modifyWorld("intent_is_affirmation", True)

	elif(answer == "Argue"):
		C.Coordinator.modifyWorld("intent_is_argument", True)

	elif(answer == "Detail"):
		C.Coordinator.modifyWorld("intent_is_details", True)

	elif(answer == "Refusal"):
		C.Coordinator.modifyWorld("intent_is_refusal", True)

	elif(answer == "Approval"):
		C.Coordinator.modifyWorld("intent_is_approval", True)
	
