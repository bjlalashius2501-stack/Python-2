


class Numerology:
	def __init__(self, sName: str, sDOB: str):
		self.__sName = sName
		self.__sDOB = sDOB

		self.__iPersonalityNumber = 0
		self.__iPowerNameNumber = 0
		self.__iLifePathNumber = 0
		self.__iBirthDayNumber = 0
		self.__iAttitudeNumber = 0
		self.__iSoulNumber = 0

		self.__listDOB = list(self.__sDOB)


		self.__dictLetterConversions = {
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

		

	def getName(self) -> str:
		return self.__sName


	def getBirthdate(self) -> str:
		return self.__sDOB


	def getAttitude(self):
		listDOBCopy = self.__listDOB.copy()
		listDOBCopy.pop(2)	# first '-' or '/'
		for _ in range(5): listDOBCopy.pop(4)

		self.__iAttitudeNumber = sum(int(d) for d in listDOBCopy)

		return self.__iAttitudeNumber


	def getBirthDay(self):
		listDOBCopy = self.__listDOB.copy()
		for _ in range(3): listDOBCopy.pop(0)
		for _ in range(5): listDOBCopy.pop(2)

		iTempSum = listDOBCopy[0] + listDOBCopy[1]
		self.__iBirthDayNumber = sum([int(n) for n in str(iTempSum)])

		return self.__iBirthDayNumber




	def getLifePath(self):
			__listDOB = []

			#* technically, doing:
			#* listDOB = [int(occ) for occ in list(self.sDOB) if occ != '-' and occ != '/']
			#* works, since its the same for loop as below, but on 1 line
			for occ in list(self.__sDOB):
				if str(occ) != '-' and occ != '/':
					__listDOB.append(int(occ))

			self.__iLifePathNumber = sum([int(d) for d in str(sum(__listDOB))])
			return self.__iLifePathNumber


	def getPersonality(self):
		allVowels = list('aeiou')
		listLettersInName = list(self.__sName.lower())
		iComputedNonVowels = 0
		for key, value in self.__dictLetterConversions.items():
			for letter in listLettersInName:
				if letter not in allVowels:
					if letter in value: iComputedNonVowels += int(key)

		iTempNonVowelSum = sum([int(d) for d in str(iComputedNonVowels)])
		self.__iPersonalityNumber = sum([int(d) for d in str(iTempNonVowelSum)])
		return self.__iPersonalityNumber




	def getPowerName(self):
		allVowels = list('aeiou')
		listLettersInName = list(self.__sName.lower())
		iComputedNonVowels = 0
		iComputedVowels = 0


		for key, value in self.__dictLetterConversions.items():
			for letter in listLettersInName:
				if letter not in allVowels:
					if letter in value: iComputedNonVowels += int(key)
				else: 
					if letter in value: iComputedVowels += int(key)


		iTempVowelSum = sum([int(d) for d in str(iComputedVowels)])
		iTempNonVowelSum = sum([int(d) for d in str(iComputedNonVowels)])

		self.__iSoulNumber = sum([int(d) for d in str(iTempVowelSum)])
		self.__iPersonalityNumber = sum([int(d) for d in str(iTempNonVowelSum)])
		self.__iPowerNameNumber = self.__iSoulNumber + self.__iPersonalityNumber

		return self.__iPowerNameNumber
	

	def getSoul(self):
			allVowels = list('aeiou')
			listLettersInName = list(self.__sName.lower())
			iComputedVowels = 0

			for key, value in self.__dictLetterConversions.items():
				for letter in listLettersInName:
					if letter in allVowels:
						if letter in value: iComputedVowels += int(key)

			iTempVowelSum = sum([int(d) for d in str(iComputedVowels)])
			self.__iSoulNumber = sum([int(d) for d in str(iTempVowelSum)])
			return self.__iSoulNumber

