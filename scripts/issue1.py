import codecs
import re
import glob
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
	
if __name__ == "__main__":
	revertible = revert_correct()
	filenames = glob.glob('../postprocessed/*.txt')
	for filename in filenames:
		print(filename)
		fin = codecs.open(filename, 'r', 'utf-8')
		data = fin.read().split('\n')
		fin.close()
		fout = codecs.open(filename, 'w', 'utf-8')
		for line in data:
			words = line.split(' ')
			wordCorrected = []
			for word in words:
				if re.search('[^ -~उ]उ', word):
					rep = re.sub('([^ -~उ])उ', '\g<1>=', word)
					for (key, value) in revertible.items():
						rep = rep.replace(key, value)
					wordCorrected.append(rep)
				else:
					wordCorrected.append(word)
			
			line = ' '.join(wordCorrected)
			fout.write(line + '\n')
		fout.close()
			