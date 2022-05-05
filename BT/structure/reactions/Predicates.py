#Predicates used by decision nodes, will return true or false based on the BT state

def check_predicate(name):
    switch={
       'user_satisfied': user_satisfied(),
       'user_answered': user_answered(),
       'survey_completed': survey_completed(),
       'intent_is_approval': intent_is_approval(),
       'intent_is_refusal': intent_is_refusal(),
	   'intent_is_satisfaction': intent_is_satisfaction(),
	   'intent_is_wishing_to_end': intent_is_wishing_to_end(),
	   'intent_is_question': intent_is_question(),
	   'intent_is_affirmation': intent_is_affirmation(),
	   'intent_is_argument': intent_is_argument(),
	   'intent_is_details': intent_is_details(),
	   'answer_is_admissible': answer_is_admissible()
       }
    return switch.get(name,'condition not implemented')

def user_satisfied():
	pass

def user_answered():
	pass

def intent_is_approval():
	pass

def survey_completed():
	pass

def intent_is_approval():
	pass

def intent_is_refusal():
	pass

def intent_is_satisfaction():
	pass

def intent_is_wishing_to_end():
	pass

def intent_is_question():
	pass

def intent_is_affirmation():
	pass

def intent_is_argument():
	pass

def intent_is_details():
	pass

def answer_is_admissible():
	pass