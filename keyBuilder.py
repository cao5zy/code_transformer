# key builder
import re
def buildKey(line, keyBuilderConfig):
	def getKeyVal():
		return (lambda result:result.groups()[keyBuilderConfig.groupNum] if result and keyBuilderConfig.hasGroup \
		else result.group() if result \
		else "")(re.search(keyBuilderConfig.keyPattern, line))
	return {
	keyBuilderConfig.keyName: getKeyVal()
	}