# keyBuilderConfig

class KeyBuilderConfig:
	def __init__(self, json):
		self.__json = json

	@property
	def keyName(self):
		return self.__json["keyName"]

	@property
	def keyPattern(self):
		return self.__json["keyPattern"]

	@property
	def hasGroup(self):
		return True if "groupNum" in self.__json.keys() \
		else False

	@property
	def groupNum(self):
		return self.__json["groupNum"] if "groupNum" in self.__json.keys() \
		else None


def getKeyBuilderConfigs(json):
	return list(map(lambda n:KeyBuilderConfig(n), json["keyBuilder"]))		