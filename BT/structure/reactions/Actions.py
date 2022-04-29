from BT import BT

def do_action(name, answer=''):
    switch={
       'greet': greet(),
       'ask_to_take_survey': ask_to_take_survey(),
       'state_question': state_question(),
       'wait_for_answer': wait_for_answer(answer),
       'detect_intent': detect_intent(answer),
	   'next_question': next_question(),
	   'goodbye': goodbye(),
	   'set_user_as_satisfied': set_user_as_satisfied(),
	   'explain': explain(),
	   'reset_user_answer': reset_user_answer(),
	   'reset_users_intent': reset_users_intent(),
	   'ask_more_details': ask_more_details(),
	   'ask_if_clarification_wanted': ask_if_clarification_wanted(),
	   'refuse_answer': refuse_answer(),
       }
    return switch.get(name,'action not implemented')


def greet():
	return("Hello! May I help you?")

def ask_to_take_survey():
	return("Would you like to helps us by answering a quick survey?")

def wait_for_answer(answer):
	while(BT.getBT().last_user_answer == answer):
		#check for answer
		pass

	BT.getBT().last_user_answer = answer

def detect_intent(answer):
	
	return("I understand that you are satisfied.")

def state_question():
	return("Are you satisfied with the answers I provided?")

def next_question():
	return("This is a new question")

def goodbye():
	return("Thank you! Good bye!")

def set_user_as_satisfied():
	BT.getBT().user_satisfied = True
	return("Then we may end this conversation here.")

def explain():
	return("This is an explanation")

def reset_user_answer():
	BT.getBT().last_user_answer = ''

def reset_users_intent():
	BT.getBT().user_intent = 'None'
	pass

def ask_more_details():
	return("Could you provide a more details, please?")

def ask_if_clarification_wanted():
	return("Do you want me to clarify that?")

def refuse_answer():
	return("Sorry, I don't understand")