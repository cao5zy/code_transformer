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
	assert_that(config.getGroup(0)).is_equal_to(None)
	assert_that(config.useItWhenTrue).is_equal_to(True)