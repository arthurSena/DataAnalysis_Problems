import codecs
import unicodedata


def remove_accents(input_str):
    nkfd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nkfd_form.encode('ASCII', 'ignore')
    return only_ascii

programacao = codecs.open('test_first_round_kaggle.csv',encoding='latin1')

for lines in programacao:
	print remove_accents(lines.strip())


