from operator import itemgetter
from collections import OrderedDict

class Room(object):
	def __init__(self, name, id,checksum):
		super(Room, self).__init__()
		self.name = name
		self.checksum = checksum
		self.id = id

	def isValid(self):
		return self.checksum.strip() == self.generateChecksum().strip()

		# return self.generateChecksum() == self.checksum 


	def generateChecksum(self):
		letterCounts = {}
		for letter in self.name:
			if letter not in letterCounts:
				letterCounts[letter] = 1
			else:
				letterCounts[letter] += 1
		return "".join(list(
						zip(*sorted(
								sorted(letterCounts.items(),key=lambda t: t[0]),
								key=lambda t: t[1], reverse=True)[0:5]
							)[0]))


rooms = []
with open("input.txt") as f:
	rooms = f.readlines()

# test 
# rooms = ["aaaaa-bbb-z-y-x-123[abxyz]", "a-b-c-d-e-f-g-h-987[abcde]", "not-a-real-room-404[oarel]", "totally-real-room-200[decoy]"]

idsum = 0

for rstring in rooms:
	parts =  rstring.split("[")
	name = "".join(parts[0].split("-")[0:-1])
	id = parts[0].split("-")[-1]
	checksum = parts[1].replace("]", "")
	
	room = Room(name,id,checksum)
	if room.isValid():
		idsum+=int(room.id)
	# room = Room()


print idsum



