# -*- coding: utf-8 -*-
import codecs
import re
import glob
import sys


def preprocess_book(book, filein, fileout):
	fin = codecs.open(filein, 'r', 'utf-8')
	data = fin.read()
	fin.close()
	# Special preprocessing for each book.
	if book in ['nyasa', 'padamanjari']:
		# Handle wrong data in input before pushing for transliteration.
		data = re.sub(u"(\W)`([^ö])", u"\g<1>'\g<2>", data)  # problem 1
		data = data.replace("ÂÂ", "Â")  # problem 2
		data = data.replace("%", "ऽ")  # Problem 3
		data = re.sub("Â[òù]Â", "Â", data)  # Problem 4
	fout = codecs.open(fileout, 'w', 'utf-8')
	fout.write(data)
	fout.close()


if __name__ == "__main__":
	book = sys.argv[1]
	filenames = glob.glob('../' + book + '/input/*.txt')
	print('preprocessing started')
	for filein in filenames:
		print(filein)
		fileinterim = filein.replace('input', 'interim')
		preprocess_book(book, filein, fileinterim)
