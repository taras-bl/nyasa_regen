import codecs
import re
import glob
import sys

from splinter.browser import Browser


class DVTTSurekhConverter(object):
    def __init__(self):
        # We presume that you've installed chrome driver as per https://splinter.readthedocs.io/en/latest/drivers/chrome.html .
        self.browser = Browser('chrome', headless=True)
        self.browser.visit("file:///F:/c_drive/xampp/htdocs/nyasa_correction/scripts/data/DV-TTSurekhEN_to_Unicode_Converter_08.htm")

    def convert(self, text):
        input_box = self.browser.find_by_id("legacy_text")
        convert_button = self.browser.find_by_name("converter")
        print(input_box)
        input_box.fill(text)
        convert_button.click()
        output_box = self.browser.find_by_id("unicode_text").first
        return output_box.value


def preprocess_nyasa(filein, fileout):
    fin = codecs.open(filein, 'r', 'utf-8')
    data = fin.read()
    fin.close()
    # Handle wrong data in input before pushing for transliteration.
    data = re.sub(u"(\W)`", u"\g<1>'", data)  # problem 1
    data = data.replace("ÂÂ", "Â")  # problem 2
    data = data.replace("%", "ऽ")  # Problem 3
    data = re.sub("Â[òù]Â", "Â", data)  # Problem 4
    #data = re.sub(u"(\w)=(\w)", u"\g<1>-\g<2>", data) # problem 3
    fout = codecs.open(fileout, 'w', 'utf-8')
    fout.write(data)
    fout.close()


def convert_nyasa(filein, fileout):
    fin1 = codecs.open(filein, 'r', 'utf-8')
    data1 = fin1.read()
    fin1.close()
    fout1 = codecs.open(fileout, 'w', 'utf-8')
    print(len(data1))
    convertor = DVTTSurekhConverter()
    data1 = convertor.convert(data1)
    print(len(data1))
    fout1.write(data1)
    fout1.close()


if __name__ == "__main__":
    filenames = glob.glob('../input/*.txt')
    if sys.argv[1] == 'preprocess':
        print('preprocessing started')
        for filein in filenames:
            print(filein)
            fileinterim = filein.replace('../input', '../interim')
            preprocess_nyasa(filein, fileinterim)
    if sys.argv[1] == 'convert':
        print('conversion started')
        for filein in filenames:
            fileinterim = filein.replace('../input', '../interim')
            print(fileinterim)
            fileout = filein.replace('../input', '../output')
            convert_nyasa(fileinterim, fileout)
