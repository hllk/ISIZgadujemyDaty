# -*- coding: utf-8 -*-

import re, csv, codecs, unicodecsv

path = "retroc-train-cleaned-500w.xml"
inputfile = codecs.open(path, 'r', 'utf-8')
giantfile = inputfile.readlines()
inputfile.close()
years = []
contents = []

for i in range(len(giantfile)):
	line = giantfile[i]
	if "<date annee=" in line:
		xxx = re.search(r'\d\d\d\d', line).group(0)
		years.append(xxx)
		print 'a:' + str(i)
		for j in range(i, i + 5, 1):
			if "<texte>" in giantfile[j]:
				contents.append(giantfile[j+1])
				i = i+5
				break

#ngramy - liczenie
n = 4
kkk = 1
#ngramsGlobal = [] #lista slownikow ngramow
ngramlist = [] # lista ngramow, jakie w ogole wystepuja wszedzie, w calym wszechswiecie o tak
for l in range(len(contents[1:2000])):
	line = contents[l]
	print 'b:' + str(kkk)
	kkk += 1
	ngrams = dict()
	for i in range(len(line) -n + 1):
		gram = line[i:i+n].encode('utf-8')
		if " " not in gram:
			if gram in ngrams:
				ngrams[gram] += 1
			else:
				ngrams[gram] = 1
			if gram not in ngramlist:
				ngramlist.append(gram)
	output = open("ngrams/" + str(l) + ".txt", "w+")
	output.write(str(ngrams))
	output.close()
#	ngramsGlobal.append(ngrams)



#tu sie tworzy najwieksza tablica swiata, nawet w guglu takiej nie maja	
with open('ngramy-train.csv', 'w') as csvfile:
	ngramwriter = unicodecsv.writer(csvfile, delimiter=',')
	#ngramwriter.writerow(['Rok'] + [n.encode('utf-8') for n in ngramlist]);
	ngramwriter.writerow(['Rok'] + ngramlist)
	for i in range(len(years)):
		inp = open("ngrams/" + str(i) + ".txt")
		ngrams = eval(inp.read())
		inp.close()
		#ngrams = ngramsGlobal[i]
		row = []
		print 'c:' + str(i)
		for ngram in ngramlist:
			if ngram in ngrams:
				row.append(ngrams[ngram])
			else:
				row.append('0')
		ngramwriter.writerow([years[i]] + row)
		
print 'ngramow: ' + str(len(ngramlist))
print 'artykulow: ' + str(len(years))