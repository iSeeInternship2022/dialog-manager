class World:
	def __init__(self) -> None:
		self.last_user_answer = None
		self.user_intent = ''
		self.survey_is_completed = False
		self.user_greeted = False
		self.user_satisfied = False
		#self.save = JSONS
		self.storage = dict()

	#put or update a value in the storage dictionnary
	def store(self, answer_key, value):
		#this function will need to change when introducing dialog logs
			self.storage[answer_key] =  value
			print("		" + str(answer_key) + " = " + str(value))

	#returns the value of a given key (and create a new entry when doesn't exist)
	def get(self, data_key):
		res = self.storage.get(data_key, None)

		#If the variable doesn't exist in the storage, it is created and set as False
		if(res == None):
			self.storage[data_key] = False
			res = False
		
		return res