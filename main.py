# main.py
from jinja2 import Template
import demjson

def getParam(name)
	dic={
		"template":"t"
		,"defintion":"d"
		,"file":"f"
	}
	options, args = getopt.getopt(sys.argv[1:], "t:d:f:", [])
	return [(key, val) for (key, val) in options if key == '-%s' % dic[name]][0][1]

def getTemplate():
	with open(getParam('template'), 'r') as file:
		return file.read()

def getBindingVal():
	return list(map(lambda line: \
			buildKey(line, getKeyBuilderConfigs(demjson.decode_file(getParam('defintion')))), getContentLine()))

def getConentLine():
	with open(getParam('file'), 'r') as file:
		return lineReader(file.read())(LineReaderConfig(demjson.decode_file(getParam('defintion'))["lineReader"]))
	
def main():
	with open('output.txt', 'w') as file:
		file.write(Template(getTemplate()).render(objs=getBindingVal()))
