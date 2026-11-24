

#* All variables are private, the calculation function is also private.
class Numerology:
	def __init__(self, sName: str, sDOB: str):
		"""
		:param: sName >> String of the client name
		:param: sDOB >> String of the client date-of-birth, (mm-dd-yyyy or mm/dd/yyyy)
		"""
		self.__sName = sName.lower()			#* The .lower() is for letter verification
		self.__sDOB = sDOB

		self.__listDOB = list(self.__sDOB)		#* This list is copied via .copy() for individual manipulation
		self.__listName = list(self.__sName)	#* This list is copied via .copy() for individual manipulation

		self.__dictLetterConversions = {		#* Table for letter-to-number conversion.
			1: ['a', 'j', 's'],
			2: ['b', 'k', 't'],
			3: ['c', 'l', 'u'],
			4: ['d', 'm', 'v'],
			5: ['e', 'n', 'w'],
			6: ['f', 'o', 'x'],
			7: ['g', 'p', 'y'],
			8: ['h', 'q', 'z'],
			9: ['i', 'r']
		}

		#* All the above private variables are used to calculate the below
		#* Since self._CalculateAllNumbers() returns a tuple of 6 integers, 
		#* calling self.__returnedInteger[i], where i is the desired integer's index (0 - 5), sets
		#* one of the six values to the corresponding tuple element

		self.__returnedInteger = self._CalculateAllNumbers()	#! THIS WORKED! I DIDN'T THINK IT WOULD!

		self.__iAttitudeBL = self.__returnedInteger[0]
		self.__iBirthDayBL = self.__returnedInteger[1]
		self.__iLifePathBL = self.__returnedInteger[2]
		self.__iPersonalityBL = self.__returnedInteger[3]
		self.__iPowerNameBL = self.__returnedInteger[4]
		self.__iSoulBL = self.__returnedInteger[5]

		


	#! THIS IS A PRIVATE CLASS-ONLY FUNCTION. CAN'T BE CALLED OUTSIDE THE CLASS
	def _CalculateAllNumbers(self) -> tuple[int]:
		"""
		:returns: Tuple of six integers, each representing a unique 1-digit whole number
		"""

		attitudeListBL = self.__listDOB.copy()	# Copy the DOB list for individual manipulation
		birthDayListBL = self.__listDOB.copy()	# Copy the DOB list for individual manipulation
		lifePathListBL = self.__listDOB.copy()	# Copy the DOB list for individual manipulation
		listLettersInName = self.__listName.copy()

		allVowels = list('aeiou')	#* aeiou

		iPersonalityNumber = 0	
		iSoulNumber = 0		

		#! delete the desired element at the specific index, or before/after a desired index
		#! [4:] is all elements at index 4 and up. [:3] is deleting all elements at index 3 and below.
		del attitudeListBL[2], attitudeListBL[4:]	#* Execute the first del, then the second.
		del birthDayListBL[:3], birthDayListBL[2:]	#* Execute the first del, then the second.
		lifePathListBL = [i for i in lifePathListBL if i != '-' and i != '/']	#* A list of numbers only

		for key, value in self.__dictLetterConversions.items():
			for letter in listLettersInName:
				if letter in allVowels:
					if letter in value: iSoulNumber += key
					else: iSoulNumber += 0

				elif letter not in allVowels:
					if letter in value: iPersonalityNumber += key
					else: iPersonalityNumber += 0

				else: print("HOW DID YOU MANAGE A HIDDEN SYMBOL???")

		iPersonalitySum = sum([int(d) for d in str(iPersonalityNumber)])
		iSoulSum = sum([int(d) for d in str(iSoulNumber)])

		#! The map function allows the list of strings (attitudeListBL) 
		#! to convert all the elements directly into a list of integers
		#! Then sum the mapped list and sum all of the individual numbers making up the list
		iNumberAttitudeBL = sum(int(i) for i in str(sum(map(int, attitudeListBL))))
		iNumberBirthdayBL = sum(int(i) for i in str(sum(map(int, birthDayListBL))))
		iNumberLifepathBL = sum(int(i) for i in str(sum(map(int, lifePathListBL))))
		iNumberPersonalityBL = sum([int(d) for d in str(iPersonalitySum)])
		iNumberSoulBL = sum([int(d) for d in str(iSoulSum)])
		iNumberPowerNameBL = iNumberSoulBL + iNumberPersonalityBL

		#* Return the six integers in a tuple. the \ just breaks up the return into 2 lines for readability.
		return iNumberAttitudeBL, iNumberBirthdayBL, iNumberLifepathBL, \
			iNumberPersonalityBL, iNumberPowerNameBL, iNumberSoulBL



	#? All the getters. No setters or issers needed (is-ers? is-sers? idk)
	def getName(self) -> str: return f'{self.__sName}'.title()	#* Just return the name as a titled string
	def getBirthdate(self) -> str: return self.__sDOB
	def getAttitude(self) -> int: return self.__iAttitudeBL
	def getBirthDay(self) -> int: return self.__iBirthDayBL
	def getLifePath(self) -> int: return self.__iLifePathBL
	def getPersonality(self) -> int: return self.__iPersonalityBL
	def getPowerName(self) -> int: return self.__iPowerNameBL
	def getSoul(self) -> int: return self.__iSoulBL

