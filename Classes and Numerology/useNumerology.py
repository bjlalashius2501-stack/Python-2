"""
	Name: Brandon Lalashius
	Assignment: Classes & Numerology
	Submitted on: 11-24-2026
	GITHUB: https://github.com/bjlalashius2501-stack/Python-2/

	REFLECTION:
		What I liked about the assignment was
		What I struggled with was
		A previous assignment I can rewrite to use classes would be
		Two things I learned from this assignment are:
			1. 
			2. 
"""


from numerology import Numerology


testPrivateAccessBL = False	#! USED FOR TESTING ACCESSING PRIVATE METHODS / VARIABLES


def testForPrivateAccess(instantiatedClass: Numerology):
	if testPrivateAccessBL:
		try:
			print(f"{instantiatedClass.__sName}")
			print(f"{instantiatedClass._CalculateAllNumbers()}")
			print(f"{instantiatedClass.__dictLetterConversions}")
			print(f"{instantiatedClass.__iAttitudeNumber}")
			print(f"{instantiatedClass.__iBirthDayNumber}")
			print(f"{instantiatedClass.__iLifePathNumber}")
			print(f"{instantiatedClass.__iPersonalityNumber}")
			print(f"{instantiatedClass.__iPowerNameNumber}")
			print(f"{instantiatedClass.__iSoulNumber}")
			print(f"{instantiatedClass.__listDOB}")
			print(f"{instantiatedClass.__sDOB}")
			
		except: print("CAN'T ACCESS HIDDEN VARIABLES!")


def main():
	while True:		#* Just enter a name, won't quit if it's blank
		sNameBL = input("Please enter your name >> ")
		if sNameBL == None: print("Please enter a valid name!")
		else: break


	while True:		#* Enter your DOB, check it qualifies, then calculate
		sDOBBL = input("Please enter your Date of Birth as so: xx-xx-xxxx. (Use either '-' or '/' as the separators) >> ")
		if sDOBBL == None: print("Please do not leave blank!")	

		lDOBListBL = list(sDOBBL)	#* create a list from the DOB
		listDOBBL = lDOBListBL.copy()	#* Copy it for manipulation
		listDOBBL = [i for i in listDOBBL if i != '-' and i != '/']	#* New list without '-' or '/'
		
		#* Print out if there is an issue, and continue the loop
		if len(listDOBBL) != 8: print("Please have the date as xx-xx-xxxx for a total of 8 numbers and 2 separators!")
		if '-' not in lDOBListBL and '/' not in lDOBListBL: print("Please use either '-' or '/' as the separators!")

		#* if the DOB has 8 numbers and separators, break the loop!
		if len(listDOBBL) == 8:
			if '-' in lDOBListBL or '/' in lDOBListBL:
				break


	#* This is the actual instant of the Numerology class. The type: ignore is for VSCode Intellisense
	clientNumerologyReportBL = Numerology(sNameBL, sDOBBL)	#! type: ignore


	print(f"Client Name: {clientNumerologyReportBL.getName()}")
	print(f"Client DOB: {clientNumerologyReportBL.getBirthdate()}")
	print(f"Client Life Path: {clientNumerologyReportBL.getLifePath()}")
	print(f"Client Birthday: {clientNumerologyReportBL.getBirthDay()}")
	print(f"Client Attitude: {clientNumerologyReportBL.getAttitude()}")
	print(f"Client Soul: {clientNumerologyReportBL.getSoul()}")
	print(f"Client Personality: {clientNumerologyReportBL.getPersonality()}")
	print(f"Client Power Name: {clientNumerologyReportBL.getPowerName()}")

	#!	THIS IS A TEST FUNCTION ONLY. IT'LL RUN ONLY IF
	#!	THE BOOLEAN IS SET TO TRUE
	testForPrivateAccess(clientNumerologyReportBL)
	


if __name__ == '__main__': main()
