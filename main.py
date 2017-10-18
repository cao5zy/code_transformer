# main.py
from jinja2 import Template
import demjson
import getopt
import sys
from lineReader import lineReader
from models.lineReaderConfig import LineReaderConfig
from keyBuilder import buildKey
from models.keyBuilderConfig import getKeyBuilderConfigs
import logging

logging.basicConfig(level=logging.INFO, stream=sys.stdout, format="%(levelname)s:%(name)s:%(funcName)s:%(message)s")

def getParam(name):
	options, args = getopt.getopt(sys.argv[1:], "t:d:f:", [])
	return (lambda dic:[(key, val) for (key, val) in options if key == '-%s' % dic[name]][0][1])({
		"template":"t"
		,"defintion":"d"
		,"file":"f"
	})

def getTemplate():
	with open(getParam('template'), 'r') as file:
		return file.read()

def getBindingVal():
	return list(map(lambda line: \
			buildKey(line, getKeyBuilderConfigs(demjson.decode_file(getParam('defintion')))), getContentLine()))

def getContentLine():
	with open(getParam('file'), 'r', encoding='utf-8') as file:
		def getlines():
			return lineReader(file.read())(LineReaderConfig(demjson.decode_file(getParam('defintion'))))
		return getlines()
	
def main():
	with open('output.txt', 'w', encoding='utf-8') as file:
		def getVal():
			return getBindingVal()
		file.write(Template(getTemplate()).render(objs=getVal()))

if __name__ == '__main__':
	main()

# python main.py -t sample.template -d sample.definition -f sample.file