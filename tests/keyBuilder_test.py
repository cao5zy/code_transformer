# key builder test
from flexmock import flexmock
from keyBuilder import buildKey
from assertpy import assert_that

def test_buildKey():
	config = flexmock(keyName="test",
		keyPattern=".*",
		hasGroup=False,
		groupNum=None)

	assert_that(buildKey("alan", [config])).is_equal_to({"test":"alan"})

def test_buildKey_two_elements():
	config = flexmock(keyName="test",
		keyPattern=".*",
		hasGroup=False,
		groupNum=None)

	config1 = flexmock(keyName="test1",
		keyPattern=".*",
		hasGroup=False,
		groupNum=None)

	assert_that(buildKey("alan", [config, config1])).is_equal_to({"test":"alan", "test1":"alan"})

def test_buildKey_has_group():
	config = flexmock(keyName="test",
		keyPattern="\w+:(\w+)",
		hasGroup=True,
		groupNum=0)

	assert_that(buildKey("name:string", [config])).is_equal_to({"test":"string"})
