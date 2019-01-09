import codecs
import re
import glob
import sys


def postprocess_book(book, filein, fileout):
	# Read data
	fin = codecs.open(filein, 'r', 'utf-8')
	data = fin.read()
	fin.close()
	# Do book specific postprocessing.
	if book in ['nyasa', 'padamanjari']:
		data = data.replace('"', '`')
		data = data.replace('््', '्')
		data = data.replace(' उ ', ' = ')
		data = data.replace('इ = ण्', 'इ उ ण्')
		data = data.replace('= ऊ ', 'उ ऊ')
	# Write data
	fout = codecs.open(fileout, 'w', 'utf-8')
	fout.write(data)
	fout.close()

if __name__ == "__main__":
	book = sys.argv[1]
	filenames = glob.glob('../' + book + '/output/*.txt')
	for filein in filenames:
		print(filein)
		fileout = filein.replace('output', 'postprocessed')
		postprocess_book(book, filein, fileout)
	