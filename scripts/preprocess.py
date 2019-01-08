# -*- coding: utf-8 -*-
import codecs
import re
import glob
import sys


def preprocess_nyasa(filein, fileout):
	fin = codecs.open(filein, 'r', 'utf-8')
	data = fin.read()
	fin.close()
	# Handle wrong data in input before pushing for transliteration.
	data = re.sub(u"(\W)`([^ö])", u"\g<1>'\g<2>", data)  # problem 1
	data = data.replace("ÂÂ", "Â")  # problem 2
	data = data.replace("%", "ऽ")  # Problem 3
	data = re.sub("Â[òù]Â", "Â", data)  # Problem 4
	#data = re.sub(u"(\w)=(\w)", u"\g<1>-\g<2>", data) # problem 3
	fout = codecs.open(fileout, 'w', 'utf-8')
	fout.write(data)
	fout.close()


if __name__ == "__main__":
	filenames = glob.glob('../input/*.txt')
	print('preprocessing started')
	for filein in filenames:
		print(filein)
		fileinterim = filein.replace('../input', '../interim')
		preprocess_nyasa(filein, fileinterim)
