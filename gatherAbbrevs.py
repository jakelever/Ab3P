import argparse
import codecs
import re
from collections import Counter

if __name__ == '__main__':
	parser = argparse.ArgumentParser('Gather the abbreviations output by the Ab3P identify_abbr tool')
	parser.add_argument('--input',type=str,required=True,help='File to process')
	parser.add_argument('--output',type=str,required=True,help='File with abbrevation counts')
	parser.add_argument('--threshold',type=float,default=0.9,help='Threshold for selecting abbreviations')
	args = parser.parse_args()

	counter = Counter()
	#pattern = re.compile("^  [A-Za-z0-9]*\|.*\|[0-9\.]*$")
	pattern = re.compile("^\s*.*\|.*\|[0-9]+\.?[0-9\.]*$")
	with codecs.open(args.input,'r','utf-8') as inF, codecs.open(args.output,'w','utf-8') as outF:
		for line in inF:
			line = line.strip()
			if pattern.match(line):
				split = line.split('|')
				shortterm = split[0].strip()
				longterm = "|".join(split[1:-1]).strip()
				score = float(split[-1].strip())
				if score > args.threshold:
					counter[(shortterm,longterm)] += 1
				#outF.write(line+"\n")

	keys = sorted(counter.keys())
	with codecs.open(args.output,'w','utf-8') as outF:
		for shortterm,longterm in keys:
			count = counter[(shortterm,longterm)]
			line = "%s\t%s\t%d\n" % (shortterm,longterm,count)
			outF.write(line)

