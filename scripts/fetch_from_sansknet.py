import requests
import os
import sys
import re
import codecs
from bs4 import BeautifulSoup


commdict = {'kashika': 'kasikavritti', 'nyasa': 'kasikavritti/nyasa', 'padamanjari': 'kasikavritti/padamanjari'}
def fetch_pada(commentary, adhyaya, pada):
	baseurl = 'http://www.wilbourhall.org/sansknet/vyakaranam/'
	adhyaya = str(adhyaya)
	pada = str(pada)
	url = baseurl + commdict[commentary] + '/a' + adhyaya + 'p' + pada + '.htm'
	r = requests.get(url)
	return r.text

def cleanhtml(raw_html):
	soup = BeautifulSoup(raw_html, 'html.parser')
	cleantext = soup.get_text()
	return cleantext

def get_full_data(commentary):
	for a in range(1,9):
		for p in range(1,5):
			print(a, p)
			html_data = fetch_pada(commentary, a, p)
			html_data = html_data.replace('<BR>', '\n')
			text_data = cleanhtml(html_data)
			fileout = '../' + commentary + '/orig/a' + str(a) + 'p' + str(p) + '.txt'
			fout = codecs.open(fileout, 'w', 'utf-8')
			fout.write(text_data)
			fout.close()
			
if __name__ == "__main__":
	commentary = sys.argv[1]
	get_full_data(commentary)