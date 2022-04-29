from ui.UiInterface import UiInterface

class UiConsole(UiInterface):

	@staticmethod
	def send_to_user(message):
		print(message)

	@staticmethod
	def send_to_user_and_response(message):
		print(message)
		return input()

	@staticmethod
	def get_response():
		return input()