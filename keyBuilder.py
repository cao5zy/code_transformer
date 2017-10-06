# key builder
import re
def buildKey(line, keyBuilderConfigs):
	def getKeyVal(keyBuilderConfig):
		return (lambda result:result.groups()[keyBuilderConfig.groupNum] if result and keyBuilderConfig.hasGroup \
		else result.group() if result \
		else "")(re.search(keyBuilderConfig.keyPattern, line))

	def buildDic(dic, name, val):
		dic[name] = val

	def processDic(dic):
		return dic if list(map(lambda keyBuilderConfig:buildDic(dic, keyBuilderConfig.keyName, getKeyVal(keyBuilderConfig)), keyBuilderConfigs)) else None

	return processDic({})
