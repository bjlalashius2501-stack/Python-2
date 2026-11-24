


class Numerology:
	def __init__(self, sName: str, sDOB: str):
		self.__sName = sName.lower()
		self.__sDOB = sDOB
		

		self.__iPersonalityNumber = 0
		self.__iPowerNameNumber = 0
		self.__iLifePathNumber = 0
		self.__iBirthDayNumber = 0
		self.__iAttitudeNumber = 0
		self.__iSoulNumber = 0

		self.__listDOB = list(self.__sDOB)
		self.__listName = list(self.__sName)


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



	def _CalculateAllNumbers(self):
		attitudeListBL = self.__listDOB.copy()
		birthDayListBL = self.__listDOB.copy()
		lifePathListBL = self.__listDOB.copy()

		listLettersInName = self.__listName.copy()

		allVowels = list('aeiou')

		iPersonalityNumber = 0
		iSoulNumber = 0

		del attitudeListBL[2], attitudeListBL[4:]
		del birthDayListBL[:3], birthDayListBL[2:]
		lifePathListBL = [i for i in lifePathListBL if i != '-' and i != '/']

		for key, value in self.__dictLetterConversions.items():
			for letter in listLettersInName:
				if letter in allVowels:
					if letter in value: iSoulNumber += key
				else:
					if letter in value: iPersonalityNumber += key

		iPersonalitySum = sum([int(d) for d in str(iPersonalityNumber)])
		iSoulSum = sum([int(d) for d in str(iSoulNumber)])


		self.__iAttitudeNumber = sum(int(i) for i in str(sum(map(int, attitudeListBL))))
		self.__iBirthDayNumber = sum(int(i) for i in str(sum(map(int, birthDayListBL))))
		self.__iLifePathNumber = sum(int(i) for i in str(sum(map(int, lifePathListBL))))
		self.__iPersonalityNumber = sum([int(d) for d in str(iPersonalitySum)])
		self.__iSoulNumber = sum([int(d) for d in str(iSoulSum)])
		self.__iPowerNameNumber = self.__iSoulNumber + self.__iPersonalityNumber

		return self.__iAttitudeNumber, self.__iBirthDayNumber, self.__iLifePathNumber, \
			self.__iPersonalityNumber, self.__iPowerNameNumber, self.__iSoulNumber




	def getName(self) -> str:
		return f'{self.__sName}'.title()


	def getBirthdate(self) -> str:
		return self.__sDOB


	def getAttitude(self) -> int:
		returnedSpecificNumber = self._CalculateAllNumbers()
		return returnedSpecificNumber[0]


	def getBirthDay(self) -> int:
		returnedSpecificNumber = self._CalculateAllNumbers()
		return returnedSpecificNumber[1]


	def getLifePath(self) -> int:
		returnedSpecificNumber = self._CalculateAllNumbers()
		return returnedSpecificNumber[2]


	def getPersonality(self) -> int:
		returnedSpecificNumber = self._CalculateAllNumbers()
		return returnedSpecificNumber[3]


	def getPowerName(self) -> int:
		returnedSpecificNumber = self._CalculateAllNumbers()
		return returnedSpecificNumber[4]
	

	def getSoul(self) -> int:
		returnedSpecificNumber = self._CalculateAllNumbers()
		return returnedSpecificNumber[5]

