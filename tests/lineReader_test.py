"# test line reader" 
from lineReader import processLine
from flexmock import flexmock
from assertpy import assert_that

def test_processLine():
	lineReaderConfig = flexmock(
		rePattern=".*",
		hasGroup=False,
		getGroupNumber = lambda:None,
		useItWhenTrue=True
		)
	line = "hello world"
	result = processLine(line, lineReaderConfig)

	assert_that(result).is_equal_to(line)

def test_processLine_has_group():
	lineReaderConfig = flexmock(
		rePattern="(world)",
		hasGroup=True,
		getGroupNumber = lambda:0,
		useItWhenTrue=True
		)
	line = "hello world"
	result = processLine(line, lineReaderConfig)

	assert_that(result).is_equal_to('world')

def test_processLine_no_match():
	lineReaderConfig = flexmock(
		rePattern="(world)",
		hasGroup=True,
		getGroupNumber = lambda:0,
		useItWhenTrue=True
		)
	line = "hello"
	result = processLine(line, lineReaderConfig)

	assert_that(result).is_equal_to(None)

def test_processLine_reverse():
	lineReaderConfig = flexmock(
		rePattern="(world)",
		hasGroup=True,
		getGroupNumber = lambda:0,
		useItWhenTrue=False
		)
	line = "hello"
	result = processLine(line, lineReaderConfig)

	assert_that(result).is_equal_to('hello')



