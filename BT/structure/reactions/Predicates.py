from sqlalchemy import true
import BT


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
	res = False
	if (BT.BT.getBT().user_satisfied):
		res = True

	return res

def user_answered():
	res = False
	if (BT.BT.getBT().last_user_answer != ''):
		res = True

	return res

def intent_is_approval():
	res = False
	if (BT.BT.getBT().user_intent == 'Approval'):
		res = True

	return res

def survey_completed():
	res = False
	if (BT.BT.getBT().survey_is_completed):
		res = True

	return res

def intent_is_refusal():
	res = False
	if (BT.BT.getBT().user_intent == 'Refusal'):
		res = True

	return res
def intent_is_satisfaction():
	res = False
	if (BT.BT.getBT().user_intent == 'Satisfaction'):
		res = True

	return res

def intent_is_wishing_to_end():
	res = False
	if (BT.BT.getBT().user_intent == 'End'):
		res = True

	return res

def intent_is_question():
	res = False
	if (BT.BT.getBT().user_intent == 'Question'):
		res = True

	return res

def intent_is_affirmation():
	res = False
	if (BT.BT.getBT().user_intent == 'Affirm'):
		res = True

	return res

def intent_is_argument():
	res = False
	if (BT.BT.getBT().user_intent == 'Argue'):
		res = True

	return res

def intent_is_details():
	res = False
	if (BT.BT.getBT().user_intent == 'Detail'):
		res = True

	return res

def answer_is_admissible():
	res = False
	if (BT.BT.getBT().last_user_answer != ''):
		res = True

	return res