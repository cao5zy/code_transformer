# line reader
import re

def lineReader(content):

	return lambda lineReaderConfig: list(filter(lambda line: line != None, map(lambda line: processLine(line, lineReaderConfig), content.splitlines())))

def processLine(line, lineReaderConfig):
	def handleResultWhenHasNoGroup(result):
		return result.group()
	def handleResultWhenHasGroup(result):
		return result.groups()[lineReaderConfig.getGroupNumber()]

	return (lambda result: handleResultWhenHasGroup(result)  \
	if result and lineReaderConfig.useItWhenTrue and lineReaderConfig.hasGroup \
	else handleResultWhenHasNoGroup(result) if result and lineReaderConfig.useItWhenTrue \
	else line if not (result or lineReaderConfig.useItWhenTrue) \
	else None)(re.search(lineReaderConfig.rePattern, line))
