"# lineReaderConfig" 
class LineReaderConfig:
	def __init__(self, json):
		self.__json = json["lineReader"];

	@property
	def rePattern(self):
		return self.__json["pattern"]

	@property
	def hasGroup(self):
		return "groupNumber" in self.__json

	def getGroupNumber(self):
		return self.__json["groupNumber"] if self.hasGroup else None

	@property
	def useItWhenTrue(self):
		return True if (self.__json["useItWhenTrue"].lower() == "true" if "useItWhenTrue" in self.__json else True) else False
		
