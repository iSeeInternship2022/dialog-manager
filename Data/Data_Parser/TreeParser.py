import json


class TreeParser:
	def __init__(self, path):
		with open(path, 'r') as BT_file:
			self.BT_struct = json.load(BT_file)
			self.BT_nodes = self.BT_struct["nodes"]
			self.BT_root = self.BT_struct["root"]

			#print(json.dumps(self.BT_nodes))

	

		
	
	# def generateTree(self):
	# 	return Tree(**json.loads(self.BT_struct))


	# def getNodes(self):
	# 	return self.BT_nodes
