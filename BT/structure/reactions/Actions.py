import BT

def do_action(name):
    switch={
       'greet': greet(),
       'ask_to_take_survey': ask_to_take_survey(),
       'state_question': state_question(),
       'wait_for_answer': wait_for_answer(),
       'detect_intent': detect_intent(),
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
	BT.BT.getBT().send("Hello! May I help you?")

def ask_to_take_survey():
	BT.BT.getBT().send("Would you like to helps us by answering a quick survey?")

def wait_for_answer():
	last_answer = BT.getBT().last_user_answer
	while(last_answer == BT.getBT().last_user_answer):
		BT.BT.receive()
		
def detect_intent():
	BT.BT.getBT().user_intent = 'Satisfaction'
	BT.BT.getBT().send("I understand that you are satisfied.")
	set_user_as_satisfied()

def state_question():
	BT.BT.getBT().send("Are you satisfied with the answers I provided?")

def next_question():
	BT.BT.getBT().send("This is a new question")

def goodbye():
	BT.BT.getBT().send("Thank you! Good bye!")

def set_user_as_satisfied():
	BT.getBT().user_satisfied = True
	BT.BT.getBT().send("Then we may end this conversation here.")

def explain():
	BT.BT.getBT().send("This is an explanation")

def reset_user_answer():
	BT.getBT().last_user_answer = ''

def reset_users_intent():
	BT.getBT().user_intent = 'None'
	pass

def ask_more_details():
	BT.BT.getBT().send("Could you provide a more details, please?")

def ask_if_clarification_wanted():
	BT.BT.getBT().send("Do you want me to clarify that?")

def refuse_answer():
	BT.BT.getBT().send("Sorry, I don't understand")