

from Data.Data_Storage.World import World
from Buisiness.BT.BT import BT
from network.API_Network import api_request
from ui.Logger import Logger
from ui.UiConsole import UiConsole

class Coordinator:

	__instance = None

	@staticmethod 
	def get():
		if Coordinator.__instance == None:
			Coordinator()
		return Coordinator.__instance

	def __init__(self) -> None:

		#private constructor
		if Coordinator.__instance != None:
			raise Exception("This is a singleton")
		else:
			Coordinator.__instance = self

		self.interface = UiConsole()
		self.world = World()
		self.bt = BT()
		self.logger = Logger()
		self.bt.coordinator = self


	@staticmethod 
	def start():
		Coordinator.get().bt.run()

	#send a question to the user and waits for an answer
	@staticmethod 
	def ask(message, answer_slot):
		Coordinator.get().log("CHATBOT : " + message)
		answer = Coordinator.get().interface.send_to_user_and_response(message)

		Coordinator.get().log("USER : " + answer)
		Coordinator.get().world.store(answer_slot, answer)

	#send a message to the user
	@staticmethod 
	def inform(message):
		Coordinator.get().log("CHATBOT : " + message)
		Coordinator.get().interface.send_to_user(message)

	#modify the value of a given world variable
	@staticmethod 
	def modifyWorld(data_slot, value):
		Coordinator.get().world.store(data_slot, value)

	#check the value of a given world variable
	@staticmethod 
	def checkWorld(data_slot):
		return Coordinator.get().world.get(data_slot)
		
	@staticmethod
	def log(message):
		Coordinator.get().logger.log(message)

	def API_querry(url):
		return api_request(url)