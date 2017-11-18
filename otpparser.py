# python3

import re

report = open("финансы 31.10.2017 по 20.11.2017", 'r')
lines = report.readlines()
foundHeader = False
cardName = ""
operationDateTime = ""
for line in lines:	
	if not foundHeader:
		if line.find('Фінансові трансакції за рахунком') != -1:
			foundHeader = True
	else:
		if line.find('Блокування по карті') != -1:
			foundHeader = False
		elif line.find("Ім'я на карті:") != -1:
			cardName = line[15:-1]
		else:
			ro = re.search("\d\d\.\d\d\.\d\d \d\d:\d\d", line)
			if ro:
				operationDateTime = ro.group(0);
			else:
				ro = re.search("(\d\d\d\d\d\d) +(.+) +(UAH) +(-*\d*,\d\d) +(UAH) +(-*\d*,\d\d)", line)
				if ro:
					operation = ro.group(2)
					summ = ro.group(4)
					separator = ';'
					print(operationDateTime[:8].replace('.', '/'), separator, summ, separator, cardName, separator, operation)




