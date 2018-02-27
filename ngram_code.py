import codecs
from collections import defaultdict

#------------------------#
def read_corpus(file):

	with codecs.open(file, "r", encoding = "utf-8") as fo:
	
		for line in fo:
			yield line

#------------------------#
def tokenize(line_in):

	punctuation = ['"', ".", ",", "?", "!", "-", ")", "(", ":", ";"]
	line_in = line_in.strip().lower()
	line_out = ""
	
	for char in line_in:
		if char not in punctuation:
			line_out += char
	
	return line_out
	
#------------------------#
def get_bigrams(line):

	bigrams = []
	
	for i in range(1, len(line)):
		yield (line[i-1], line[i])

#------------------------#
def count_bigrams(filename):

	corpus = read_corpus(filename)
	bigram_count = defaultdict(int)
	
	for line in corpus:
		
		line = tokenize(line)
		line = line.split(" ")
		
		for bigram in get_bigrams(line):
			bigram_count[bigram] += 1
			
	return bigram_count
	
#------------------------#
bigram_count = count_bigrams("./corpora/eng.Europarl.txt")
top_bigrams = sorted(bigram_count, key = bigram_count.get, reverse = True)

for i in range(10):
	print(top_bigrams[i], bigram_count[top_bigrams[i]])