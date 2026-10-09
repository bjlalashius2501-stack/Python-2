"""
	Name: Brandon Lalashius
	Code Started: 09-25-2026
	Code Rewritten Count: 3
	Code Submitted: 10-##-2026
	Assignment: Password Validator

	NOTE: All comments with a ! or * in it were made with the VScode Better Comments Extension in mind

	Reflection:
		What I REALLY liked about this assignment was that it really made me stop
		and think about the whole process first and also break down each part step-by-step.
		That was in order to go through the steps and really figure out if 
		what I was doing was truly correct and efficient. 
		Plus it reinforces the use of comments (something I don't do enough in personal projects...) 

		
		I really struggled with not being able to utilize a lot of the various tricks I've learned
		through personal experimentation. Once I got used to using libraries like string or re
		I really had a hard time trying to figure out some of the steps for checking repeats especially!
		It did take some time, but I eventually got it! Also labeling my variables in a manner I'm not 
		used to did take a bit to remember to do throughout the program

		
		In order to increase efficiency while decreasing redundancy I had to make sure that whenever a loop was being
		executed, I was able to utilize it to check the password for specific conditions if possible. Sometimes
		however, I couldn't get away with that since the loops were checking very specific conditions. I also managed to fit
		all the checks into a single function solely to be able to return True or False based on the password validity. 


		Two things I genuinely learned were:
		1. The use of some built-in string methods like isdigit(). I never touched a lot of the 
			built-in string methods before this project, and was able to experiment with what 
			worked and what didn't in a genuine learning manner.
			
		2. I learned how to check for string duplication with sets. I've heard of sets, but never sat down and learned them.
			I've played around with dictionaries a bit (in Arduino, Robot-C [through VexRobotics], and Python)
			but I never used sets before. Now I know they are similar to lists but I never knew that sets were NON-DUPLICATING.
			(A dictionary of dictionaries of values is a nightmare to manage)
"""



def validatePassword(sParamPasswordBL, sParamInitialsBL):
	bIsValidPasswordBL = True	# This is to verify the password IS/ISN'T valid

	# These booleans just verify that each character required is present in the password
	# When these are True, thats 1 step closer to a valid password
	bIsLowerBL = False
	bIsUpperBL = False
	bIsSpecialBL = False
	bIsNumberBL = False

	# Break the password into a list, and set each letter to lowercase
	# This is used to check for duplication and if it starts with PASS
	lPasswordListBL = list(sParamPasswordBL.lower())
	lPassCheckBL = []	# Used to verify the password doesn't start with the word PASS




	# Check length of password (8 - 12 characters)
	if 12 < len(sParamPasswordBL) or len(sParamPasswordBL) < 8:
		print("Please enter a password between 8 and 12 characters!")
		bIsValidPasswordBL = False



	# Verify the characters are acceptable
	for sChar in sParamPasswordBL:
		if sChar.isupper(): bIsUpperBL = True
		elif sChar.islower(): bIsLowerBL = True
		elif sChar.isdigit(): bIsNumberBL = True
		elif sChar in list("!@#$%^"): bIsSpecialBL = True
		if all([bIsUpperBL, bIsLowerBL, bIsNumberBL, bIsSpecialBL]): break
	###### ^^^ ALL IS USED TO CHECK IF A LIST OF BOOLEANS RETURN TRUE/FALSE ######

	# Print the proper response if any of the above booleans are False
	if not bIsUpperBL: print("Your password must have at least 1 UPPERCASE letter")
	if not bIsLowerBL: print("Your password must have at least 1 LOWERCASE letter")
	if not bIsNumberBL: print("Your password must have at least 1 NUMBER")
	if not bIsSpecialBL: print("Your password must have at least 1 of the following SPECIAL CHARACTERS: ( ! @ # $ % ^ )")
	if not all([bIsUpperBL, bIsLowerBL, bIsNumberBL, bIsSpecialBL]): bIsValidPasswordBL = False
	###### ^^^ ALL IS USED TO CHECK IF A LIST OF BOOLEANS RETURN TRUE/FALSE ######
	# In this case, if all the booleans are NOT true (even if 1 is False), then the password is NOT valid
		


	# Check if password contains the word PASS
	# Iterate through the password 4 times, checking if the first 4 letters make up the word 'PASS'
	# The list of characters making up the password
	# are all set to lowercase for ease of checking.
	for iChar in range(4):
		if lPasswordListBL[iChar] == list("pass")[iChar]: lPassCheckBL.append(iChar)
			#* index 0 != p	*#
			#* index 1 != a	*#
			#* index 2 != s	*#
			#* index 3 != s	*#

	#! if lPassCheckBL == 4			<<< THATS WRONG	!#
	#! if len(lPassCheckBL) == 4	<<< THATS RIGHT	!#
	if len(lPassCheckBL) == 4:
		print("Your password cannot have the word 'PASS' in it!")

		bIsValidPasswordBL = False
		lPassCheckBL.clear()	# CLEAR FOR THE NEXT TEST


	# Check if password contains user's initials
	if sParamInitialsBL in sParamPasswordBL:
		print("Your password cannot contain your initials!")
		bIsValidPasswordBL = False


	
	# The below duplication validation code works like so:
	# 1. if the length of the list is not equal to the length of the list when converted to a 
	# 	 set (since sets can NOT have duplicates), then execute the count
	# 2. notify user that the issue has occurred
	# 3. iterate through the list of characters set to lowercase and add the character(s) into the duplicate
	#	 set ONLY if it already appears in the set of seen elements
	#	 otherwise add the character into the seen list, since it is not already there
	# 4. print the duplicated character & the amount of times it duplicates in the inital password
	# 5. set the bIsValidPasswordBL to False, signifying that the password failed this portion of the 
	# 	 validation process.

	setSeenCharsBL = set()	# Set to identify which characters have been seen
	setDuplicateCharsBL = set()	# Set to identify duplicate characters
	if len(lPasswordListBL) != len(set(lPasswordListBL)):
		print("THESE CHARACTERS APPEAR MORE THAN ONCE:")
		for char in lPasswordListBL:
			if char in setSeenCharsBL: setDuplicateCharsBL.add(char)
			else: setSeenCharsBL.add(char)

		for dupe in list(setDuplicateCharsBL):
			print(f"{dupe}: {lPasswordListBL.count(dupe)} Times")

		bIsValidPasswordBL = False
		setSeenCharsBL.clear()			# CLEAR FOR THE NEXT TEST
		setDuplicateCharsBL.clear()		# CLEAR FOR THE NEXT TEST

		

	# RETURNS TRUE IF ALL CHECKS ABOVE PASS
	return bIsValidPasswordBL




def main():
	bIsNotValidBL = True	# Only used to exit the password loop (technically, a break works >> easier to understand)
	while True:
		sNameBL = input("Please enter your first and last name (EX: John Smith) >> ")
		if len(sNameBL.strip().split()) != 2: print("Please enter a first & last name separated by a space!")
		else: break
		
	while bIsNotValidBL:
		sPasswordBL = str(input("Enter new password >> "))

		sFormattedNameBL = sNameBL.lower().title()	## Set the name to all lowercase, then title the first initials
		sInitialsBL = "".join([sLetterBL[0] for sLetterBL in sFormattedNameBL.split(' ')])
		# Split the full name string into 2 strings, and create a new string containing ONLY the letter
		# at index 0 of the two separate strings

		isValidPassword = validatePassword(sPasswordBL, sInitialsBL) # Have a boolean that is the return value of the function
		bIsNotValidBL = False if isValidPassword else True	# Kill the loop only if the isNotValid boolean is False


	# notify user the password is valid and okay to use!
	else: print("PASSWORD IS VALID AND OK TO USE!")





#! This is used to run the main function when this file !#
#! runs as a script and not when imported as a module !#
if __name__ == "__main__":
	main()
