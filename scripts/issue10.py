import codecs
import re
import glob


if __name__ == "__main__":
	filenames = glob.glob('../input/*.txt')
	for filename in filenames:
		# Read data
		fin = codecs.open(filename, 'r', 'utf-8')
		
		for line in fin:
			m = re.search('^([0-9]+)\..*\(([1-8]\.[1-4]\.[0-9]+)\)', line)
			if m:
				starter = m.group(1)
				full_num = m.group(2)
				if starter != full_num.split('.')[2]:
					print("{} != {}".format(full_num, starter))
			
		
	