import random
import pandas as pd
import sys
import time

from loadboss import Boss


def CritChances(chanceRate):
	return random.random() < chanceRate

def NumericGrouping(Num):
	variable_1 = "{}".format(Num)
	Grouping = []
	while variable_1 and variable_1[-1].isdigit():
		Grouping.append(variable_1[-3:])
		variable_1 = variable_1[:-3]

	return variable_1 + ",".join(reversed(Grouping))

def animationLoading():
	print("Initializing ...")
	animations = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

	for i in range(len(animations)):
		time.sleep(0.3)
		sys.stdout.write("\r" + animations[i % len(animations)])
		sys.stdout.flush()


def showDataBoss():
	fBs = Boss()
	detailedBoss = fBs.ShowBoss()
	detailedBoss.pop(0)

	for boss in detailedBoss:
		print(boss[1])


def fightBoss(askHeroName, askTotalAttack, askCDMG, askCritRate, totalHitRate, askSelectBoss, askPhase):
	fBoss = Boss()
	LoadBossInformation = fBoss.ShowBoss()
	LoadBossInformation.pop(0)
	BOUNDARY_LOOP = len(LoadBossInformation)

	try:
		if LoadBossInformation[askSelectBoss] in LoadBossInformation:
			# selecting boss phase to select HP for that BOSS
			_HPBossphase = LoadBossInformation[askSelectBoss][2:11]		# Boss HP each Phase
			totalCDMG = 0
			totalNormalAttk = 0
			combinedAtk = totalCDMG + totalNormalAttk
			BossHPSelectedPhase = int(_HPBossphase[askPhase])

			while totalHitRate > 0:
				totalHitRate -= 1
				time.sleep(0.2)
				if CritChances(askCritRate/100):
					OutputCritDMG = round(askTotalAttack + (askTotalAttack * (askCDMG/100)))
					totalCDMG += OutputCritDMG
					print("\t\t{} land CRITICAL DAMAGE with {}".format(askHeroName, NumericGrouping(OutputCritDMG)))
				else:
					# Normal Hit
					NonCrit = askTotalAttack + askTotalAttack
					totalNormalAttk += NonCrit
					print("\t\t{} land NORMAL HIT with {}".format(askHeroName, NumericGrouping(NonCrit)))

			print("\nTotal Crit Damage is {}".format(NumericGrouping(totalCDMG)))
			print("Total Normal Damage is {}".format(NumericGrouping(totalNormalAttk)))

		else:
			print("None")
	except Exception as e:
		print(e)

def test(hitcount):
	fBoss = Boss()
	LoadBossInformation = fBoss.ShowBoss()
	LoadBossInformation.pop(0)

	hpBoss = int(LoadBossInformation[1][5])
	atkhero = int(12321232 * hitcount)
	print(NumericGrouping(hpBoss))
	while hitcount > 0 :
		hitcount -= 1
		hpBoss -= atkhero
		print(NumericGrouping(hpBoss))
		if hitcount == 0:
			print("Reached")

	sadf = hpBoss / atkhero
	print(NumericGrouping(round(sadf)))
