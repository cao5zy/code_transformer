"# test" 
from jinja2 import Template
from assertpy import assert_that

def test_using_template_simple_dic():
	dic = {"name": "alan"};
	temp = Template('''{{ col.name }}''')

	assert_that(temp.render(col = dic)).is_equal_to('alan')

def test_using_template_with_list():
	dic = {"list": [{"name": "alan"}, {"name": "tracy"}]}
	temp = Template('''{% for n  in obj.list %}
		{{ n.name}};
		{% endfor %}''')

	assert_that(temp.render(obj = dic)).contains('alan;')
	assert_that(temp.render(obj = dic)).contains('tracy;')
		
