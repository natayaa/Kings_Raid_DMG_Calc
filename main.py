import sys
import gamefunc as gf



def main():
	gf.animationLoading()
	print("\n")

	try:
		askHeroName = str(input("Who's the Hero: ").capitalize())
		askTotalAttack = int(input("Enter total Attack of {} have : ".format(askHeroName)))
		askCDMG = int(input("Enter total Critical Damage % of {} : ".format(askHeroName)))
		askCritRate = int(input("Enter Critical Rate {} have : ".format(askHeroName)))
		totalHitRate = int(input("Enter how much {} want to hit the boss : ".format(askHeroName)))
		gf.showDataBoss()
		askSelectBoss = int(input("Enter the number of boss you want to Fight with [0-11]: "))
		askPhase = int(input("Enter Phase[1-9] : "))
		gf.fightBoss(askHeroName, askTotalAttack, askCDMG, askCritRate, totalHitRate, askSelectBoss, askPhase)
	except Exception as e:
		print(e)
		sys.exit()

if __name__ == '__main__':
	main()