import json


class TreeParser_str:

	def __init__(self, rawjson) :
		self.BT_struct = json.loads(rawjson)
		self.BT_nodes = self.BT_struct["nodes"]
		self.BT_root = self.BT_struct["root"]

			#print(json.dumps(self.BT_nodes))

	

		
	
	# def generateTree(self):
	# 	return Tree(**json.loads(self.BT_struct))


	# def getNodes(self):
	# 	return self.BT_nodes
