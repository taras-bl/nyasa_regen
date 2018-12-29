import codecs
import os.path
import re

from splinter.browser import Browser


class DVTTVedicConverter(object):
    def __init__(self):
        # We presume that you've installed chrome driver as per https://splinter.readthedocs.io/en/latest/drivers/chrome.html .
        self.browser = Browser('chrome', headless=True)
        print(os.path.dirname(__file__))
        exit(0)
        self.browser.visit('file://' + os.path.join(os.path.dirname(__file__), "data", 'DV-TTVedicNormal ==_ यूनिकोड परिवर्तित्र.html'))
        
    def convert(self, text):
        input_box = self.browser.find_by_id("legacy_text")
        convert_button = self.browser.find_by_name("converter")
        print(input_box)
        input_box.fill(text)
        convert_button.click()
        output_box = self.browser.find_by_id("unicode_text").first
        return output_box.value


if __name__ == "__main__":
	fin = codecs.open('../input/a8p4.txt', 'r', 'utf-8')
	data = fin.read()
	fin.close()
	# Handle wrong data in input before pushing for transliteration.
	data = re.sub(u"(\W)`", u"\g<1>'", data) # problem 1
	data = data.replace("ÂÂ", "Â") # problem 2
	data = data.replace("Ë½þ", "हिं") # problem 3
	fout = codecs.open('../interim/a8p4_preprocessed.txt', 'w', 'utf-8')
	fout.write(data)
	fout.close()