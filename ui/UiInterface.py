import abc

class UiInterface( abc.ABC ) :

	@staticmethod
	@abc.abstractclassmethod
	def send_to_user(message):
		pass

	@staticmethod
	@abc.abstractclassmethod
	def send_to_user_and_response(message):
		pass

	@staticmethod
	@abc.abstractclassmethod
	def get_response():
		pass