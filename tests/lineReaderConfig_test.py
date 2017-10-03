"# lineReaderConfig_test" 
from models.lineReaderConfig import LineReaderConfig
import demjson
from assertpy import assert_that

def test_lineReaderConfig():
	json = demjson.decode('''{
		"lineReader":{
			"pattern": ".*",
		}
		} ''')

	config = LineReaderConfig(json)
	assert_that(config.rePattern).is_equal_to(".*")
	assert_that(config.hasGroup).is_equal_to(False)
	assert_that(config.getGroupNumber()).is_equal_to(None)
	assert_that(config.useItWhenTrue).is_equal_to(True)

def test_lineReaderConfig_group_number():
	json = demjson.decode('''{
			"lineReader":{
				"pattern": ".*",
				"groupNumber": 1
			}
			} ''')

	config = LineReaderConfig(json)
	assert_that(config.rePattern).is_equal_to(".*")
	assert_that(config.hasGroup).is_equal_to(True)
	assert_that(config.getGroupNumber()).is_equal_to(1)
	assert_that(config.useItWhenTrue).is_equal_to(True)

def test_lineReaderConfig_use_it_when_true_val_false():
	json = demjson.decode('''{
			"lineReader":{
				"pattern": ".*",
				"groupNumber": 1,
				"useItWhenTrue": "false"
			}
			} ''')

	config = LineReaderConfig(json)
	assert_that(config.rePattern).is_equal_to(".*")
	assert_that(config.hasGroup).is_equal_to(True)
	assert_that(config.getGroupNumber()).is_equal_to(1)
	assert_that(config.useItWhenTrue).is_equal_to(False)

def test_lineReaderConfig_use_it_when_true_val_true():
	json = demjson.decode('''{
			"lineReader":{
				"pattern": ".*",
				"groupNumber": 1,
				"useItWhenTrue": "true"
			}
			} ''')

	config = LineReaderConfig(json)
	assert_that(config.rePattern).is_equal_to(".*")
	assert_that(config.hasGroup).is_equal_to(True)
	assert_that(config.getGroupNumber()).is_equal_to(1)
	assert_that(config.useItWhenTrue).is_equal_to(True)
