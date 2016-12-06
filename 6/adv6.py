import string
from operator import itemgetter
from collections import OrderedDict
lines = []
with open("test.txt") as f:
	lines = f.readlines()

index_counts = [{} for i in range(len(lines[0]))]
print index_counts

for line in lines:
	for idx, letter in enumerate(line):
		if letter not in index_counts[idx]:
			index_counts[idx][letter]=1;
		else:
			index_counts[idx][letter]+=1;


decoded = ""

for di in index_counts:
	decoded = decoded + sorted(di.items(),key=lambda t: t[1], reverse=False)[0][0]

print decoded