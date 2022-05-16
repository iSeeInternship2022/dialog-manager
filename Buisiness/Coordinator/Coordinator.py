
from ui.UiConsole import UiConsole
from Data.Data_Storage.World import World
from Buisiness.BT.BT import BT

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
		self.bt.coordinator = self

	def start(self):
		Coordinator.get().bt.run()

	#send a question to the user and waits for an answer
	@staticmethod 
	def ask(message, answer_slot):
		answer = Coordinator.get().interface.send_to_user_and_response(message)
		Coordinator.get().world.store(answer_slot, answer)

	#send a message to the user
	@staticmethod 
	def inform(message):
		Coordinator.get().interface.send_to_user(message)

	#modify the value of a given world variable
	@staticmethod 
	def modifyWorld(data_slot, value):
		Coordinator.get().world.store(data_slot, value)

	#check the value of a given world variable
	@staticmethod 
	def checkWorld(data_slot):
		return Coordinator.get().world.get(data_slot)
		