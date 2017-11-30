# key builder
from autologging import logged

import re
def buildKey(line, keyBuilderConfigs):
	def getKeyVal(keyBuilderConfig):
		def getValueFromGroup(result):
			return result.groups()[keyBuilderConfig.groupNum]
		def getVal(result):
			return result.group()
		@logged
		def getResult():
			result = re.search(keyBuilderConfig.keyPattern, line)
			#getResult._log.info({"line":line, "result": result})
			return result
		return (lambda result: getValueFromGroup(result) if result and keyBuilderConfig.hasGroup \
		else getVal(result) if result \
		else "")(getResult())

	def buildDic(dic, name, val):
		dic[name] = val

	def processDic(dic):
		return dic if list(map(lambda keyBuilderConfig:buildDic(dic, keyBuilderConfig.keyName, getKeyVal(keyBuilderConfig)), keyBuilderConfigs)) else None

	return processDic({})
