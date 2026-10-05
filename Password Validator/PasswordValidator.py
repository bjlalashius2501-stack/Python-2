"""
	Name: Brandon Lalashius
	Code Started: 09-25-2026
	Code Finished: 09-25-2026
	Code Submitted: ??-??-2026
	Assignment: Password Validator

	Reflection:
		What I REALLY liked about this assignment was that it really made me stop
		and think about the whole process first. That was in order to go through 
		the steps and really figure out if what I was doing was truly correct and efficient. 
		Plus it reinforces the use of comments (something I don't do enough in personal projects...) 

		I really struggled with not being able to utilize a lot of the various tricks I've learned
		through personal experimentation. Once I got used to using libraries like math, random, and string
		I really had a hard time trying to figure out some of the steps for checking repeats especially!
		It did take some time, but I eventually got it!

		Two things I genuinely learned were:
		1. The use of some built-in methods like isalpha(). I never touched it before this project,
			and was able to experiment with what worked and what didn't in a genuine learning moment.
		
			
		2. I learned about the proper use of sets. I've heard of them, but never sat down and learned them.
			I've played around with dictionaries a lot (in Arduino, Robot-C [through VexRobotics], and Python)
			but I never used sets before. Now I know they are similar to lists, but they are declared by the 
			curly brackets {} similarly to a dict, but I never knew that these were NON-DUPLICATING.
"""



#########################################################################################################################
#TODO:																													#
#TODO: 		1. Create loop for full name verification (make sure it is both first & last)								#
#TODO: 		2. Create password boolean while loop and test that it works												#
#TODO:		3. Split the full name string into 2 strings, .title() them, and separate out all lowercase					#
#TODO: 			letters, leaving the 2 initals that are joined into a single string										#
#TODO: 		4. Create the function for checking the characters in the password (letters, numbers, & special characters)	#
#TODO: 		5. Create the function for checking specific conditions, those being password length, checking for			#
#TODO:		user initials, and checking if the starting 4 characters spell 'pass'										#
#TODO: 		6. Create the final function for checking if there are any repeats											#
#TODO:		7. Verify that all 3 functions work, and return either True or False based on conditions					#
#TODO: 		8. Exit the while loop when all 3 functions return True, ending the program									#
#TODO:																													#
#########################################################################################################################


def check_characters(sParamPasswordBL):
	ACCEPTABLE_LETTERS = list("abcdefghijklmnopqrstuvwxyz")
	ACCEPTABLE_NUMBERS = list("0123456789")
	ACCEPTABLE_CHARACTERS = list("!@#$%^")

	sCharListBL = list(sParamPasswordBL)
	sAllowedCharactersListBL = []

	###	the 3 acceptable lists never change >> constants
	### split the password into a list of each character
	### have a separate list for validation




	## VERIFY PASSWORD CONTAINS ACTUAL CONTAINS A LETTER
	if not any(char.isalpha() for char in sParamPasswordBL):
		print("PASSWORD MUST CONTAIN AT LEAST 1 LETTER")
		return False


	# the .isalpha() checks to see if the string contains a valid letter
	# the whole check is done character by character via a for loop!


	# VERIFY PASSWORD CONTAINS AT LEAST:
	# 1 UPPERCASE LETTER
	# 1 LOWERCASE LETTER 
	# 1 SPECIAL CHARACTER (! @ # $ % ^)
	# 1 NUMBER


	# Since the 4 checks are the (almost) exact same, it does the following:
	# 1. clear the list for checking validation
	# 2. get each character in the CONSTANTS lists
	# 3. check if the character appears in the password via the split list
	# 4. if the character DOES appear, append it into the list
	# 5. print a warning and return False ONLY if the list is empty
	# 6. if the list DOES contain at least 1 value if each of the 4 checks >> return True


	###### LOWERCASE LETTERS ######
	sAllowedCharactersListBL.clear()
	for char in ACCEPTABLE_LETTERS:
		if char in sCharListBL:
			sAllowedCharactersListBL.append(char)

	if len(sAllowedCharactersListBL) == 0:
		print("PASSWORD MUST CONTAIN AT LEAST 1 LOWERCASE LETTER")
		return False


	###### NUMBERS ######
	sAllowedCharactersListBL.clear()
	for char in ACCEPTABLE_NUMBERS:
		if char in sCharListBL:
			sAllowedCharactersListBL.append(char)

	if len(sAllowedCharactersListBL) == 0:
		print("PASSWORD MUST CONTAIN AT LEAST 1 NUMBER")
		return False


	###### UPPERCASE LETTERS ######
	sAllowedCharactersListBL.clear()
	for char in ACCEPTABLE_LETTERS:
		if char.upper() in sCharListBL:
			sAllowedCharactersListBL.append(char)

	if len(sAllowedCharactersListBL) == 0:
		print("PASSWORD MUST CONTAIN AT LEAST 1 UPPERCASE LETTER")
		return False


	###### SPECIAL CHARACTERS ######
	sAllowedCharactersListBL.clear()
	for char in ACCEPTABLE_CHARACTERS:
		if char in sCharListBL:
			sAllowedCharactersListBL.append(char)

	if len(sAllowedCharactersListBL) == 0: 
		print("PASSWORD MUST CONTAIN AT LEAST 1 OF THESE SPECIAL CHARACTERS: ! @ # $ % ^")
		return False

	# RETURNS TRUE IF ALL CHECKS ABOVE PASS
	return True





def check_special_conditions(sParamPasswordBL, sParamInitialsBL):
	sCharListBL = list(sParamPasswordBL)
	sAllowedCharactersListBL = []
	# create a list of the password split into each individual character
	# create an EMPTY list for validation checking


	###### CHECK PASSWORD LENGTH ######
	if len(sParamPasswordBL) < 8 or len(sParamPasswordBL) > 12:
		print("PASSWORD MUST BE BETWEEN 8 AND 12 CHARACTERS")
		return False


	###### CHECK IF PASSWORD CONTAINS USER'S INITIALS ######
	if sParamInitialsBL.lower() in sParamPasswordBL or sParamInitialsBL in sParamPasswordBL:
		print("PASSWORD MUST NOT CONTAIN USER INITIALS")
		return False


	###### CHECK IF THE PASSWORD STARTS WITH THE WORD 'pass' ######
	# this check is done very specifically:
	# 1. since the word 'pass' has 4 letters, iterate through a for loop 4 times
	# 2. append the first 4 characters of the password into the validation list
	#	 ONLY if the first 4 are the word PASS
	# 3. Return False only if the validation list contains exactly 4 characters

	for i in range(4):
		if sCharListBL[i].lower() in list("pass"): sAllowedCharactersListBL.append(i)

	if len(sAllowedCharactersListBL) == 4:
		print("PASSWORD MUST NOT START WITH THE WORD PASS")
		return False


	# RETURNS TRUE IF ALL CHECKS ABOVE PASS
	return True






def check_character_repeats(sParamPasswordBL):
	sCharListBL = list(sParamPasswordBL)
	seenSetBL = set()
	dupesSetBL = set()
	# create the list containing each password character individually
	# create two sets, one for the seen elements and one for the duplicates


	# 1. if the length of the list is not equal (since sets can NOT have duplicates)
	# 2. notify user that the error has occurred
	# 3. iterate through the list of characters and add the character into the duplicate
	#	 set only if it already appears in the set of seen elements
	#	 otherwise add the character into the seen list, since it is not already there
	# 4. print the duplicated character & the amount of duplicates in the inital password
	# 5. return False

	if len(sCharListBL) != len(set(sCharListBL)):
		print("THESE CHARACTERS APPEAR MORE THAN ONCE:")
		for char in sCharListBL:
			if char in seenSetBL: dupesSetBL.add(char)
			else: seenSetBL.add(char)

		for dupe in list(dupesSetBL):
			print(f"{dupe}: {sCharListBL.count(dupe)} TIMES")

		return False



	# RETURNS TRUE IF ALL CHECKS ABOVE PASS
	else: return True	





def main():
	bIsNotValidBL = True	# Only used to exit the password loop (technically, a break works >> easier to understand)


	###### GET USER'S FULL NAME & CHECK IT IS A VALID FIRST + LAST NAME ######
	while True:
		sNameBL = input("Please enter your first and last name (EX: John Smith) >> ")
		if len(sNameBL.strip().split()) != 2: print("PLEASE ENTER ONLY A FIRST NAME AND A LAST NAME SEPARATED BY A SPACE")
		else: break
		##	GOTTA HAVE A VALID NAME!

	###### GET AND VERIFY USER PASSWORD ######
	while bIsNotValidBL:
		sPasswordBL = input("Enter new password >> ")

		######	Get User Initials	######
		sFormattedNameBL = sNameBL.lower().title()	## Set the name to all lowercase, then title the first initials
		sInitialsBL = "".join([sLetterBL[0] for sLetterBL in sFormattedNameBL.split(' ')])
		#	The above code joins the initials into 1 string by:
		#	take the full name, format it into lowercase letters, then uppercase
		#	only the starting letter of each name (first & last)
		#	splitting the initial string into 2 strings, then getting each letter
		# 	(which is in index 0 of the "name list")
		#	and join them into a single string



		# These next 3 are separate functions (for ease of checking true vs false)
		# 1. check for special conditions (length, contains initials, starts with 'pass')
		# 2. check if the password contains at least 1 of the following:
		#	 at least 1 uppercase letter
		#	 at least 1 lowercase letter
		#	 at least 1 special character: ! @ # $ % ^
		#	 at least 1 number
		# 3. check for any character repetition

		bPassedSpecialBL = check_special_conditions(sPasswordBL, sInitialsBL)
		bPassedLettersBL = check_characters(sPasswordBL)
		bPassedRepeatsBL = check_character_repeats(sPasswordBL)

		# assuming that ALL the 3 above checks are true:
		# set the isNotValid boolean to False (meaning the password IS valid) and exit the loop
		# ** the built-in 'all' method checks if booleans in a list passed to it are all True **
		bIsNotValidBL = False if all([bPassedSpecialBL, bPassedLettersBL, bPassedRepeatsBL]) else True

	# notify user the password is valid and okay to use!
	else: print("PASSWORD IS VALID AND OK TO USE!")




main()
