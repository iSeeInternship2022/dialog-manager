from abc import ABC, abstractmethod
from ast import List


class Node :
	def __init__(self, id) -> None:
		self.children = [Node]
		self.parent = None
		self.id = id
		self.status = False



	@abstractmethod
	def goToNext(self, predecessor : "Node"):
		pass

	@abstractmethod
	def toString(self):
		pass