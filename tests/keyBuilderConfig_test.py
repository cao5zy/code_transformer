from models.keyBuilderConfig import KeyBuilderConfig
import demjson
from assertpy import assert_that

def test_KeyBuilderConfig():
	json = demjson.decode('''{
		"keyName": "test",
		"keyPattern": ".*"
		}''')

	config = KeyBuilderConfig(json)

	assert_that(config.keyName).is_equal_to("test")
	assert_that(config.keyPattern).is_equal_to(".*")
	assert_that(config.hasGroup).is_equal_to(False)
	assert_that(config.groupNum).is_equal_to(None)

def test_KeyBuilderConfig_has_group():
	json = demjson.decode('''{
		"keyName": "test",
		"keyPattern": ".*",
		"groupNum": 0
		}''')

	config = KeyBuilderConfig(json)

	assert_that(config.keyName).is_equal_to("test")
	assert_that(config.keyPattern).is_equal_to(".*")
	assert_that(config.hasGroup).is_equal_to(True)
	assert_that(config.groupNum).is_equal_to(0)

