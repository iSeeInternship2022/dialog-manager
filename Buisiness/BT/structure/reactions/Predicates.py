from importlib_metadata import method_cache
from sqlalchemy import true
import  Buisiness.BT.BT as BT

#Depreciated
#Predicates used by decision nodes, will return true or false based on the BT state

def check_predicate(name):
	if(name == 'user_satisfied'):
		res = user_satisfied()
	elif(name == 'user_greeted'):
		res = user_greeted()
	elif(name == 'user_answered'):
		res = user_answered()
	elif(name == 'survey_completed'):
		res = survey_completed()
	elif(name == 'intent_is_approval'):
		res = intent_is_approval()
	elif(name == 'intent_is_refusal'):
		res = intent_is_refusal()
	elif(name == 'intent_is_satisfaction'):
		res = intent_is_satisfaction()
	elif(name == 'intent_is_wishing_to_end'):
		res = intent_is_wishing_to_end()
	elif(name == 'intent_is_question'):
		res = intent_is_question()
	elif(name == 'intent_is_affirmation'):
		res = intent_is_affirmation()
	elif(name == 'intent_is_argument'):
		res = intent_is_argument()
	elif(name == 'intent_is_details'):
		res = intent_is_details()
	elif(name == 'answer_is_admissible'):
		res = answer_is_admissible()
	else:
		BT.BT.getBT().logger.log("PREDICATE NOT IMPLEMENTED")
		res = False
	return res


def user_greeted():
	res = False
	if(BT.BT.getBT().user_greeted):
		res = True
	return res
	

def user_satisfied():
	res = False
	if (BT.BT.getBT().user_satisfied):
		res = True

	return res

def user_answered():
	res = False
	if (BT.BT.getBT().last_user_answer != None):
		
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