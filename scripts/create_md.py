# -*- coding: utf-8 -*-
import codecs
import re
import glob
import os
import sys

def create_md(book, filein):
	padaname = re.sub('^.*a([1-8]p[1-4])\.txt', '\g<1>', filein)
	dirname = '../' + book + '/md/pada-' + padaname.replace('p', '.')
	if not os.path.exists(dirname):
		os.mkdir(dirname)
	sutranum = '0.0.0'
	sutratext = ''
	sutra_commentary = ''
	# Read data
	fin = codecs.open(filein, 'r', 'utf-8')
	for line in fin:
		if book == 'nyasa':
			m = re.search('^[0-9]+[.](.*)\(([1-8][.][1-4][.][0-9]+)\)\r\n', line)
		if m:
			fout = codecs.open(dirname + '/' + sutranum + '.md', 'w', 'utf-8')
			fout.write('---\n')
			fout.write('index:  ' + sutranum + '\n')
			fout.write('sutra:  ' + sutratext + '\n')
			fout.write('vritti:  nyasa\n')
			fout.write('---\n\n')
			fout.write(sutra_commentary)
			sutranum = m.group(2)
			sutratext = m.group(1)
			sutratext = sutratext.strip()
			sutratext = sutratext.replace('।', '')
			print(sutranum)
			sutra_commentary = ''
		else:
			sutra_commentary += line
	fout = codecs.open(dirname + '/' + sutranum + '.md', 'w', 'utf-8')
	fout.write('---\n')
	fout.write('index:  ' + sutranum + '\n')
	fout.write('sutra:  ' + sutratext + '\n')
	fout.write('vritti:  nyasa\n')
	fout.write('---\n\n')
	fout.write(sutra_commentary)
	
if __name__ == "__main__":
	book = sys.argv[1]
	filenames = glob.glob('../' + book + '/postprocessed/*.txt')
	for filein in filenames:
		print(book, filein)
		create_md(book, filein)

		