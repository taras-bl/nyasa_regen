import codecs
import re
import glob
import sys
import os

def revert_correct():
	excpfile = codecs.open('issue1_corrected.txt', 'r', 'utf-8')
	excps = excpfile.read().split()
	excps = [member.rstrip() for member in excps]
	result = {}
	for word in excps:
		rep = re.sub('([^ -~उ])उ', '\g<1>=', word)
		result[rep] = word
	return result

def correct_issue1(book, filein):
	# Read data
	fin = codecs.open(filein, 'r', 'utf-8')
	data = fin.read().split('\n')
	fin.close()
	# Manipulate data
	data1 = ''
	for line in data:
		words = line.split(' ')
		wordCorrected = []
		for word in words:
			if book == 'nyasa' and re.search('[^ -~उ]उ', word):
				rep = re.sub('([^ -~उ])उ', '\g<1>=', word)
				for (key, value) in revertible.items():
					rep = rep.replace(key, value)
				wordCorrected.append(rep)
			else:
				wordCorrected.append(word)
		
		line = ' '.join(wordCorrected)
		data1 = data1 + line + '\n'
	data1 = data1.rstrip()
	# Write data
	fout = codecs.open(filein, 'w', 'utf-8')
	fout.write(data1)
	fout.close()
	
	
if __name__ == "__main__":
	book = sys.argv[1]
	revertible = revert_correct()
	filenames = glob.glob('../' + book + '/postprocessed/*.txt')
	for filein in filenames:
		print(filein)
		correct_issue1(book, filein)
