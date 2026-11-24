"""
	Name: Brandon Lalashius
	Assignment: Classes & Numerology
	Submitted on: 11-24-2026
	GITHUB: https://github.com/bjlalashius2501-stack/Python-2/

	NOTE: I USED PYTHON 3.14 FOR THIS
	NOTE: I USE VSCODE BETTER COMMENTS EXTENSION. THATS WHY COMMENTS HAVE EITHER A '!', '*', OR '?'
			ALLOWS FOR THE COMMENTS TO BE COLORED

	REFLECTION:
		What I liked about the assignment was how I had to really think about how I was going to build 
			the various parts at once, without relying on a bunch of for-loops. Being able to use del and map really
			helped. The for-loops in if-statements are nicer since they are in a single line

		What I struggled with was trying to only let the getters return a value and not actually compute. The __init__ of 
			the class running the function really did make it easier, but only after I realized I could do it.

		A previous assignment I can rewrite to use classes would be the Interplanetary Weights. Having a dataclass 
			for the gravity factor, instead of a dictionary, would be better. Then having a class for converting where
			each planet is just the class being instantiated.

		Two things I learned from this assignment are:
			1. Allowing for a class __init__ to run class-specific functions. I just tried it and it worked!
			2. The ability and usage of setting class variables and functions as private.
"""


from numerology import Numerology


PRIVATE_ACCESS_TESTING_BOOLEAN_BL = False	#! USED FOR TESTING ACCESSING PRIVATE METHODS / VARIABLES

#! THIS FUNCTION IS WHAT TESTS FOR ACCESSING ANY PRIVATE CLASS FUNCTIONS
def testForPrivateAccess(instantiatedClass: Numerology):
	if PRIVATE_ACCESS_TESTING_BOOLEAN_BL:	#? Will only print when in 'testing' mode
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
			
		except: print("[!] ERROR: CAN'T ACCESS CLASS-ONLY PRIVATE VARIABLES! [!]")


def main():
	while True:		#* Just enter a name, won't quit if it's blank
		sNameBL = input("Please enter your name >> ")
		if sNameBL == None or sNameBL == '': print("Please enter a valid name!")
		elif not all(letter.isalpha() for letter in sNameBL.replace(' ', '')): print("Please enter a valid name!")
		else: break

	while True:		#* Enter your DOB, check it qualifies, then calculate
		sDOBBL = input("Please enter your Date of Birth as so: mm-dd-yyyy or mm/dd/yyy >> ")
		if sDOBBL == None or sDOBBL == '': print("Please do not leave blank!")	

		lDOBListBL = list(sDOBBL)
		listDOBBL = [i for i in lDOBListBL if i != '-' and i != '/']


		
		#* Print out alerts if there is an issue, and continue the loop
		if len(listDOBBL) != 8: print("Please have the date as mm-dd-yyyy or mm/dd/yyyy for a total of 8 numbers and 2 separators!")
		if not all(element.isdigit() for element in listDOBBL): print("Please only use whole numbers for the month, day, year!")
		if '-' not in lDOBListBL and '/' not in lDOBListBL: print("Please use either '-' or '/' as the separators!")



		#* if the DOB has 8 valid numbers and valid separators then break the loop!
		if len(listDOBBL) == 8:
			if '-' in lDOBListBL or '/' in lDOBListBL:
				if all(element.isdigit() for element in listDOBBL):
					break

	#* instantiate the Numerology class as clientNumerologyReportBL
	clientNumerologyReportBL = Numerology(sNameBL, sDOBBL)

	
	print(f"===== CLIENT DATA =====\n{clientNumerologyReportBL}")

	#!	THIS IS A TEST FUNCTION ONLY. IT'LL RUN ONLY IF
	#!	THE BOOLEAN IS SET TO TRUE
	testForPrivateAccess(clientNumerologyReportBL)
	

#? Just making sure the main function isn't ran as an imported function instead of
#? being ran as the primary main file (such as 'main.py')
if __name__ == '__main__': main()
