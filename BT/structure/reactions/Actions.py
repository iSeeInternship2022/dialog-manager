import BT

def do_action(name):
	if(name == 'greet'):
		greet()
	elif(name == 'ask_to_take_survey'):
		ask_to_take_survey()
	elif(name == 'state_question'):
		state_question()
	elif(name == 'check_for_answer'):
		check_for_answer()
	elif(name == 'detect_intent'):
		detect_intent()
	elif(name == 'next_question'):
		next_question()
	elif(name == 'goodbye'):
		goodbye()
	elif(name == 'set_user_as_satisfied'):
		set_user_as_satisfied()
	elif(name == 'explain'):
		explain()
	elif(name == 'reset_user_answer'):
		reset_user_answer()
	elif(name == 'reset_users_intent'):
		reset_users_intent()
	elif(name == 'ask_more_details'):
		ask_more_details()
	elif(name == 'ask_if_clarification_wanted'):
		ask_if_clarification_wanted()
	elif(name == 'refuse_answer'):	
		refuse_answer()
	else:
		BT.BT.getBT().logger.log("ACTION NOT IMPLEMENTED")



def greet():
	BT.BT.getBT().send("Hello! May I help you?")
	BT.BT.getBT().user_greeted = True

def ask_to_take_survey():
	BT.BT.getBT().send("Would you like to helps us by answering a quick survey?")

def check_for_answer():
	last_answer = BT.BT.getBT().last_user_answer
	while(last_answer == BT.BT.getBT().last_user_answer):
		BT.BT.getBT().receive()
		
def detect_intent():
	if(BT.BT.getBT().last_user_answer == "Satisfied"):
		BT.BT.getBT().user_intent = 'Satisfaction'
		BT.BT.getBT().send("I understand that you are satisfied.")
		set_user_as_satisfied()

	elif(BT.BT.getBT().last_user_answer == "Question"):
		BT.BT.getBT().user_intent = 'Question'
		BT.BT.getBT().send("I understand that you asked a question")

	elif(BT.BT.getBT().last_user_answer == "Affirm"):
		BT.BT.getBT().user_intent = 'Affirm'
		BT.BT.getBT().send("I understand that you understand.")

	elif(BT.BT.getBT().last_user_answer == "Argue"):
		BT.BT.getBT().user_intent = 'Argue'
		BT.BT.getBT().send("I understand that you counter-argumented.")

	elif(BT.BT.getBT().last_user_answer == "Detail"):
		BT.BT.getBT().user_intent = 'Detail'
		BT.BT.getBT().send("I understand that you provided details.")

	elif(BT.BT.getBT().last_user_answer == "End"):
		BT.BT.getBT().user_intent = 'End'
		BT.BT.getBT().send("I understand that you wish to end")

	elif(BT.BT.getBT().last_user_answer == "Refusal"):
		BT.BT.getBT().user_intent = 'Refusal'
		BT.BT.getBT().send("I understand that you refused.")

	elif(BT.BT.getBT().last_user_answer == "Approval"):
		BT.BT.getBT().user_intent = 'Approval'
		BT.BT.getBT().send("I understand that you approved.")
	

def state_question():
	BT.BT.getBT().send("Are you satisfied with the answers I provided?")

def next_question():
	BT.BT.getBT().send("This is a new question")

def goodbye():
	BT.BT.getBT().send("Thank you! Good bye!")

def set_user_as_satisfied():
	BT.BT.getBT().user_satisfied = True
	BT.BT.getBT().send("Then we may end this conversation here.")

def explain():
	BT.BT.getBT().send("This is an explanation")

def reset_user_answer():
	BT.BT.getBT().last_user_answer = ''

def reset_users_intent():
	BT.BT.getBT().user_intent = 'None'
	pass

def ask_more_details():
	BT.BT.getBT().send("Could you provide a more details, please?")

def ask_if_clarification_wanted():
	BT.BT.getBT().send("Do you want me to clarify that?")

def refuse_answer():
	BT.BT.getBT().send("Sorry, I don't understand")