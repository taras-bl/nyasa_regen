import codecs
import re
import glob
from indic_transliteration.sanscript import transliterate

array_one = ["$","&","*","£Ã", "%",

"+Éä","+Éè","+É","+",   '<È',   "<Ç","<",">","=","@","A",  "Bå",   "Bä", "‹ä", "B", "‹", "आå", "आé",   

"C","D","E","F","G","H","I","J","K","L","M","N","O",
"P","Q","R","S","T","U","V","W","X","Y","Z","[","\\","]","^","_",

"`","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
"p","q","r","s","t","u","v","w","x","y","z","{","|","}","~",

"¡","¢","£","¤","¥","¦","§","¨","©","ª","«","®","¯",  "¬",     
"°","±","²","³","´","µ","¶", "•", '·', "¸","¹","º","»",  

"À", "Á", "¾", "¿", "¼", "½",
"Â", "Ã", "Ä", "Æ", "Å",

"ä","è","Éä","Éè","É","Ò","Ö","×","Ù","Ú","Ý","Þ","ß","्ा",
"å","é","ì",

"ð","ñ","ò","ó","ô","õ","ö","÷","ø","ù","ú","û","ü","ý","þ",
"ाे","ाै","आॅ","ाॅ" ,  "\'", 'रू ' ]

array_two = ["ॐ","ः","।","फ़्र", "ऽ",

"ओ","औ","आ","अ",   "ईं",   "ई","इ","ऊ","उ","ऋ","ॠ",  'ऐं',  "ऐ", "ऐ", "ए", "ए", "ओं", "औं",

"क्","क़्","क","क़","क्र","क्त","क्ष्","ख्","ख़्","ख्र्","ग्","ग़्","ग्र्",
"घ्","घ्र्","ङ","च्","च्र्","छ","ज्","ज़्","ज्र्","ज्ञ्","झ्","झ्र्","ञ्","ट","ट्ट","ट्ठ",

"ठ","ठ्ठ","ड","ड़","ड्ड","ड्ढ","ढ","ढ़","ण्","त्","त्र्","त्त्","थ्","थ्र्","द","दृ",
"द्र","द्द" ,"द्ध","द्म","द्य","द्व","ध्","ध्र्","न्","न्र्","न्न्","प्","प्र्","फ्","फ़्",

"फ","फ़","फ्र","ब्","ब्र्","भ्","भ्र्","म्","म्र्","य्","य्र्","र","रु",   "्य",     
"रू","ल्","ळ्","ळ","व्","व्र्","श्", "श्व्", 'श्व्', "श्र्","ष्","स्","स्र्",

"ह्म", "ह्य", "हृ", "ह्र", "ह्", "ह",
"्", "़", "ँ", "ं", "्र",

"े","ै","ो","ौ","ा","ी","ु","ु","ु","ू","ू","ृ","ॄ","",
"ें","ैं","ॅ",

"","","","","","","","","","","","","","","",
"ो","ौ","ऑ","ॉ" ,  '\"', ' डिग्री ' ]

array_one_length = len(array_one)

deva_digits = ['०','१','२','३','४','५','६','७','८','९']
eng_digits = ['0','1','2','3','4','5','6','7','8','9']

def Replace_Symbols(text):
	text = re.sub('Â=', 'Â #=# ', text)
	text = re.sub('[ ]+=[ ]+', ' = ', text)
	for i in range(array_one_length):
		text = text.replace(array_one[i], array_two[i])
	# Special issues
	text = text.replace('È', 'Çं')
	text = text.replace('ç', 'Çें')
	text = text.replace('æ', 'Çे')
	text = text.replace('ë', 'Çैं')
	text = text.replace('ê', 'Çै')
	text = text.replace('Ô', 'Çी')
	text = text.replace('Ó', 'ीं')
	text = text.replace('Õ', 'Çीं')
	text = text.replace('Õ', 'Çीं')
	text = text.replace('Ì', 'र्Ê')
	text = text.replace('Î', 'Ê')
	text = transliterate(text, 'devanagari', 'slp1')
	text = re.sub('Ê([^a]+)a', '\g<1>i', text)
	text = re.sub("([^ aAiIuUfFxXeEoO\"'\n\-]+[aAiIuUfFxXeEoO])Ç", "r\g<1>", text)
	text = re.sub('Ë([^ aAiIuUfFxXeEoO]+)a', '\g<1>iM', text)
	text = re.sub('Ï([^ aAiIuUfFxXeEoO]+)a', '\g<1>iM', text)
	text = text.replace('Ae', 'o')
	text = text.replace('ae', 'e')
	text = text.replace('aI', 'I')
	text = text.replace('aE', 'E')
	text = text.replace('AE', 'O')
	text = transliterate(text, 'slp1', 'devanagari')
	text = text.replace('॥', '।।')
	text = text.replace(' #उ# ', ' = ')
	for x in range(len(deva_digits)):
		text = text.replace(deva_digits[x], eng_digits[x])
	splts = re.split('(\([^)]*\))', text)
	text = ''
	for x in range(len(splts)):
		if x % 2 == 0:
			text += splts[x]
		else:
			text = text + splts[x].replace('।', '.')
	text = re.sub('([1-8])।([1-4])।([0-9]+)', '\g<1>.\g<2>.\g<3>', text)
	text = re.sub('\n([0-9]+)।', '\n\g<1>.', text)
	return text

if __name__ == "__main__":
	filenames = glob.glob('../interim/*.txt')
	print('conversion started')
	for filein in filenames:
		print(filein)
		fileout = filein.replace('../interim', '../output')
		with codecs.open(filein, 'r', 'utf-8') as fin:
			data = fin.read()
			data = Replace_Symbols(data)
			with codecs.open(fileout, 'w', 'utf-8') as fout:
				fout.write(data)