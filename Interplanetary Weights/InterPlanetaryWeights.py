"""
NAME: Brandon Lalashius
ASSIGNMENT: Inter-planetary weights Dictionary with pickling
GITHUB: https://github.com/bjlalashius2501-stack/Python-2/tree/main/Interplanetary%20Weights

REFLECTION:
	What I really enjoyed was being able to think outside the box and discover ways to more easily
	and more efficiently do parts of the assignment such as os.path.exists instead of the try/except
	for checking if the .db file exists!

	What I struggled with was checking whether the db file actually exists. I've ended up rewriting
	that part countless times (at least 5+) so I clearly struggled with it.

	Two things I learned were:
		1.
		2.
"""

import pickle, os


dictPlanetHistoryBL = {}
dictPersonWeightsBL = {}
dictGravityFactorsBL = {
	"MERCURY": 0.38,
	"VENUS": 0.91,
	"MOON": 0.165,
	"MARS": 0.38,
	"JUPITER": 2.34,
	"SATURN": 0.93,
	"URANUS": 0.92,
	"NEPTUNE": 1.12,
	"PLUTO": 0.066
}

dbPath = 'blPlanetaryWeights.db'
fEarthWeightBL = 0.0

def main():
	with open(dbPath, 'wb') as db:	#* a+ means I can read & append AND create the file if needed
		if os.path.exists(dbPath):

			while True:
				sShowHistory = input("Do you want to see the history? (y or n) >> ").lower()
				if sShowHistory == 'y' or sShowHistory == 'yes':
					dictPlanetHistoryBL = dict(pickle.load(db))
					break

				elif sShowHistory == 'n' or sShowHistory == 'no': break
				else: print("Please input y or n")


		while True:
			while True:
				sUniqueNameBL = input("Please enter a unique name (leave blank to exit) >> ")
				if sUniqueNameBL in dictPlanetHistoryBL: print("That name already exists")
				else: break

			if sUniqueNameBL is None or sUniqueNameBL == "": break
			fEarthWeightBL = float(input("Please enter a weight on Earth >> "))


			for planet, weight in dictGravityFactorsBL.items():
				fNewWeight = fEarthWeightBL * weight
				print(f"Weight on {planet:<10}: {fNewWeight:>10.2f}")
				dictPersonWeightsBL[planet] = fNewWeight



			dictPlanetHistoryBL[sUniqueNameBL] = dictPersonWeightsBL
			dictPersonWeightsBL.clear()


		pickle.dump(dictPlanetHistoryBL, db)
			
			
if __name__ == '__main__': main()
