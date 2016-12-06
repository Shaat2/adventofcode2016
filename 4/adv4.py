from operator import itemgetter
from collections import OrderedDict
import string
class Room(object):
	def __init__(self, name, id,checksum):
		super(Room, self).__init__()
		self.name = name
		self.checksum = checksum
		self.id = id

	def isValid(self):
		return self.checksum.strip() == self.generateChecksum().strip()

		
	def generateChecksum(self):
		letterCounts = {}
		name = self.name.replace("-", "")
		for letter in name:
			if letter not in letterCounts:
				letterCounts[letter] = 1
			else:
				letterCounts[letter] += 1

		return "".join(list(zip(*sorted(sorted(letterCounts.items(),key=lambda t: t[0]),key=lambda t: t[1], reverse=True)[0:5])[0]))


	def decodeChar(self, char):
		abc = string.ascii_lowercase
		if char not in abc:
			return ' '
		else:
			return abc[(int(self.id)%len(abc) + abc.index(char))% len(abc)]

	def decode(self):
		return "".join(list(self.decodeChar(c) for c in self.name))

		



rooms = []
with open("input.txt") as f:
	rooms = f.readlines()

# test 
# rooms = ["aaaaa-bbb-z-y-x-123[abxyz]", "a-b-c-d-e-f-g-h-987[abcde]", "not-a-real-room-404[oarel]", "totally-real-room-200[decoy]", "qzmt-zixmtkozy-ivhz-343[zimth]"]

idsum = 0

for rstring in rooms:
	parts =  rstring.split("[")
	name = "-".join(parts[0].split("-")[0:-1])
	id = parts[0].split("-")[-1]
	checksum = parts[1].replace("]", "")

	room = Room(name,id,checksum)

	if room.isValid():		
		if "object" in room.decode():
			print room.id + ": " + room.decode()

print idsum



