"# line reader" 
import re

def lineReader(content):

	return lambda lineReaderConfig: list(filter(lambda line: line != None, map(lambda line: processLine(line, lineReaderConfig), content.splitlines())))

def processLine(line, lineReaderConfig):
	return (lambda result: result.groups()[lineReaderConfig.getGroupNumber()] \
	if result and lineReaderConfig.useItWhenTrue and lineReaderConfig.hasGroup \
	else result.groups()[0] if result and lineReaderConfig.useItWhenTrue \
	else line if not (result or lineReaderConfig.useItWhenTrue) \
	else None)(re.search(lineReaderConfig.rePattern, line))
