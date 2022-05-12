from abc import ABC, abstractmethod
from ast import List

from structure.nodes.StateType import StateType


class Node :
	def __init__(self, id) -> None:
		self.children = []
		self.parent = None
		self.id = id
		self.status = StateType.FAILURE



	@abstractmethod
	def tick(self, predecessor : "Node"):
		pass


	@abstractmethod
	def toString(self):
		pass