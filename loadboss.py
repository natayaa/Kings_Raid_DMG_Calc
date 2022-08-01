import csv

class Boss:
	def __init__(self):
		self.LoadFile = open("Staged_Boss.csv","r")
		self.LoadBoss = csv.reader(self.LoadFile,delimiter=";")

	def ShowBoss(self):
		bossList = []
		for boss in self.LoadBoss:
			bossList.append(boss)

		return bossList