"""
NAME: Brandon Lalashius
ASSIGNMENT: Inter-planetary weights Dictionary with pickling
GITHUB: https://github.com/bjlalashius2501-stack/Python-2/tree/main/Interplanetary%20Weights

REFLECTION:
	What I really enjoyed was being able to think outside the box and discover ways to more easily
	and more efficiently do parts of the assignment such as os.path.exists instead of the try/except
	for checking if the .db file exists!

	What I struggled with was 

	Two things I learned were:
		1.
		2.
"""

import pickle, os

dictPlanetHistoryBL = {}
dictPersonWeightsBL = {}
dictWeightConversionsBL = {
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
	#** WAS TOLD THE IF/ELSE WAS OKAY TO REPLACE THE TRY/EXCEPT
	if os.path.exists(dbPath):
		with open(dbPath, 'r') as db:
			for key, value in db:
				dictPlanetHistoryBL[key] = value


			sAllowHistory = input("Do you want to see the history (y or n) >> ")
			if sAllowHistory.lower() == 'y':
				for line in dictPlanetHistoryBL:
					print(f"=> {line}")


			while True:
				sUniqueNameBL = input("Please enter a unique name (leave blank to exit) >> ")
				if sUniqueNameBL == None or sUniqueNameBL == "":
					break

				if sUniqueNameBL in dictPlanetHistoryBL:
					print(f"{sUniqueNameBL} already exists. Please enter another name.")

				else:
					while True:
						sWeightInputBL = input("Please enter a weight in lbs >> ")
						try:
							fEarthWeightBL = float(sWeightInputBL)
							break
						
						except ValueError:
							print("Please enter a valid weight!")

					for planet, weight in dictWeightConversionsBL.items():
						dictPersonWeightsBL[planet] = weight * fEarthWeightBL

					for key, value in dictPersonWeightsBL.items():
						print(f"PLANET: {key:<10}	|	WEIGHT: {value:<10.2f}lbs")
					
					break




	else:
		with open(dbPath, 'w') as db:
			pass

		





if __name__ == '__main__': main()
