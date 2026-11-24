from numerology import Numerology


def main():
	bDOBCheck = True


	while True:
		sName = input("Please enter your name >> ")
		if sName == None: print("Please enter a valid name!")
		else: break


	while bDOBCheck:
		sDOB = input("Please enter your Date of Birth as so: xx-xx-xxxx. (Use either '-' or '/' as the separators) >> ")
		if sDOB == None: print("Please do not leave blank!")
		for i in sDOB:
			if i != '-' and i != '/': bDOBCheck = False

		if bDOBCheck: print("Please use either - or / as the separators!")


	myNumerology = Numerology(sName, sDOB)	#type: ignore
	print(f'Life Path Number: {myNumerology.getLifePath()}')
	print(f'Birth Day Number: {myNumerology.getBirthDay()}')
	print(f'Attitude Number: {myNumerology.getAttitude()}')
	print(f'Soul Number: {myNumerology.getSoul()}')
	print(f'Personality Number: {myNumerology.getPersonality()}')
	print(f'Power Name Number: {myNumerology.getPowerName()}')


if __name__ == '__main__': main()