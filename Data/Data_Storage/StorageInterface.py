import abc

class StorageInterface( abc.ABC ) :

	@staticmethod
	@abc.abstractclassmethod
	def save(data):
		pass

	@staticmethod
	@abc.abstractclassmethod
	def load():
		pass
