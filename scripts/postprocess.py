import codecs
import re
import glob
import sys

if __name__ == "__main__":
	filenames = glob.glob('../output/*.txt')
	for filename in filenames:
		print(filename)
		# Read data
		fin = codecs.open(filename, 'r', 'utf-8')
		data = fin.read()
		fin.close()
		# Manipulate data
		data = data.replace('"', '`')
		data = data.replace('््', '्')
		data = data.replace(' उ ', ' = ')
		data = data.replace('इ = ण्', 'इ उ ण्')
		data = data.replace('= ऊ ऊ3', 'उ ऊ ऊ3')
		# Write data
		fileout = filename.replace('../output', '../postprocessed')
		fout = codecs.open(fileout, 'w', 'utf-8')
		fout.write(data)
		fout.close()
	