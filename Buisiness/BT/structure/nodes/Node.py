from abc import ABC, abstractmethod
from ast import List
import Buisiness.Coordinator as C

from Buisiness.BT.structure.nodes.StateType import StateType


class Node :
	def __init__(self, id) -> None:
		self.id = id
		self.status = StateType.FAILURE

	@abstractmethod
	def reset(self):
		pass


	@abstractmethod
	def tick(self):
		pass


	@abstractmethod
	def toString(self):
		pass

	def tick_keep_track(self):
		C.Coordinator.log("opened : " + self.__class__ + " " + self.id)

		self.tick()

		C.Coordinator.log("closed : " + self.__class__ + " " + self.id)
