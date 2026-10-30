"""
NAME: Brandon Lalashius
Code Started: 10-23-2026
Code Rewritten Count: 5
Code Submitted: 10-30-2026
ASSIGNMENT: Interplanetary weights Dictionary with pickling
GITHUB: https://github.com/bjlalashius2501-stack/Python-2/tree/main/Interplanetary%20Weights

REFLECTION:
	What I really enjoyed was being able to think outside the box and discover ways to more easily
	and more efficiently do parts of the assignment such as using the os library to help ease the
	creation process a lot, while opening doors to be more creative with problem solving.

	What I struggled with was appending the person's weight to the history dict and then 
	clearing the person weight dictionary before adding another persons weight again
	only for me to realise I didn't wrap dictPersonWeightsBL in a dict().

	I enjoyed working with the dictionary/pickling concepts since pickling was something I never heard of before, 
	and that made me actually learn what it does, how to use it, and the file extension the process uses. Nesting 
	dictionaries is something I've played around with, albeit unsuccessfully. The only time I ever witnessed it in 
	practice was in my High School Vex Robotics club where the co-mentor for programming built an autonomous routine
	record/play building system for actual competition use.

	Two things I learned were:
		1. How to properly implement the whole pickling process and be able to handle the EOFError, which 
			initially through me in for a loop since the error occured when file existed but was empty. I
			realised I never compensated for that and I added in the try/except for that part. 
		2. How to manage nesting dictionaries and clearing the values of the one being nested. That took an 
			amount of time I'm not going to expose here (it was too long).
"""

import pickle	# pickle
from os import path

plkFilePath = 'blPlanetaryWeights.plk'
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
	"PLUTO": 0.066		# PLUTO IS A PLANET!
}





def main():
	if path.exists(plkFilePath):	# The whole point OS is imported, makes checks much easier
		while True:	# This makes sure you input y/yes or n/no for the history check
			sShowHistory = input("Do you want to see the history? (y or n) >> ").lower()
			if sShowHistory == 'y' or sShowHistory == 'yes':
				try:
					with open(plkFilePath, 'rb') as plk: dictTempDictBL = dict(pickle.load(plk))
					for name, data in dictTempDictBL.items(): dictPlanetHistoryBL[name] = data

					# This whole try block just opens the pickle file (in Read-Binary mode), extracts the
					# data in a dictionary (unless there is 0 data)
					# then prints all of it neatly to the screen.
					for name, data in dictPlanetHistoryBL.items():
						print(f"{name}'s weight data:")
						for planet, weight in data.items():
							print(f"{planet} => {weight:.2f}")
						
						print("==========================================")

				except EOFError:	# End-Of-File error.
					print("There is no data in the file. Continuing onwards.")
					break
				
				break

			elif sShowHistory == 'n' or sShowHistory == 'no': break
			else: print("Please input y or n")




		

	with open(plkFilePath, 'wb') as plk:	# db is just the Database / Pickle file shortened down. Opened in Write-Binary mode
		while True:
			while True:	# Just makes sure you input a string
				sUniqueNameBL = input("Please enter a unique name (enter key to quit) >> ").lower().title()
				if sUniqueNameBL in dictPlanetHistoryBL: print("That name already exists")
				else: break

			if sUniqueNameBL is None or sUniqueNameBL == "": break
			while True:	# This makes sure that the weight you input is a valid int/float (and can be converted to a float)
				sInputWeight = input("Please enter a weight on Earth >> ")
				try: 
					fEarthWeightBL = float(sInputWeight)
					break

				except ValueError: print("Please input a valid number, such as 1 or 2.5")

			print(f"{sUniqueNameBL}, here are your weights on the Solar System's Planets.")
			for planet, weight in dictGravityFactorsBL.items():
				fNewWeightBL = fEarthWeightBL * weight

				# This part was easy to figure out, painful to fix.
				# Turns out that I built it right the first time
				
				print(f"Weight on {planet:<10}: {fNewWeightBL:>10.2f}")	# prints and formats it (:<10 is format left, :>10 is right)
				dictPersonWeightsBL[planet] = fNewWeightBL


			#!	DON'T CHANGE THIS LINE OR IT BREAKS		!#
			#!	WHY A DICT NEEDS TO BE CONVERTED		!#
			#!	TO A DICT IS BEYOND ME					!#
			dictPlanetHistoryBL[sUniqueNameBL] = dict(dictPersonWeightsBL)




		pickle.dump(dictPlanetHistoryBL, plk)	# pickle


	print(f"Data written to .plk file ({plkFilePath}). Thank you!")
if __name__ == '__main__': main()	# This makes sure that this file is NOT ran as an imported library / package / module
