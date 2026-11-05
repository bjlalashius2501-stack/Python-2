"""
	Name: Brandon Lalashius
	Assignment: Real Estate Analyzer with Lists & Files
	Code Submitted: 11-05-2026
	Code rewrite count: 2
	Github: https://github.com/bjlalashius2501-stack/Python-2/tree/main/Real%20Estate%20Analyzer%20with%20Files%20%26%20Lists
	
	REFLECTION:
		What I liked about this assignment is how I had to really think about the data handling and extracting the data for 
			later use and manipulation.

		What I struggled with was trying to figure out how to extract the data based off specific variables like city.
			Turns out all I had to do was extract the city, type, zip, and price of each section and append that value to the 
			appropriate key: value pair of the nested dictionary. Basically: I initially overcomplicated it (and it still is)

		The way I imported the data was using the CSV library and I chose it because csv has the DictReader method which 
			lets the data being extracted be iterated through for storing in dictionaries / lists / sets.

		The amount of dictionaries I used was 1, but since it was nested with three more, technically 4 total.

		Two things I learned were:
			1. Manipulating CSV data through the csv library. This proved to be a challenge when the ways I tried weren't
				quite the way I ended up doing the manipulations in the final submission.
			2. Fetching data through nested dictionaries in a for loop. This one wasn't as difficult as I thought.
"""

import csv, sys

listTotalPricesBL = []	# ALL the prices for math
dictAllPricesBL = {		# Nested Dictionary for the City, Property Type, and Zip Code prices
	"city": {},
	"type": {},
	"zip": {}
}

"""
Essentially, the nested dictionaries work like so:
dictAllPricesBL = {
	"city": {
		"SACRAMENTO": 682000.00,
		"ELK GROVE": 205000.00
	},
	"type": {
		"Residential": 2468000.72
	},
	"zip": {
		"01069": 329482.00
	}
}
It's just an easier way for the data to be stored
"""


def getMedian(dataList: list) -> float:
	"""
	:param dataList: This is the list of data used to calculate the median
	:return float: This is the return type, used for math for the median
	"""

	# The check below will get the data list, extract the median data, and return it as a float
	if len(dataList) % 2 == 0:	# IF AN EVEN NUMBER: GET THE 2 VALUES AND FIND THE AVERAGE BETWEEN THEM
		fEvenEntryOneBL = dataList[(len(dataList) // 2) - 1]
		fEvenEntryTwoBL = dataList[(len(dataList) // 2)]

		fMedianDataBL = (fEvenEntryOneBL + fEvenEntryTwoBL) / 2

	# IF AN ODD NUMBER: GET THE MIDDLE VALUE
	else: fMedianDataBL = dataList[len(dataList) // 2]


	return float(fMedianDataBL)




def getDataInput(sDataFilePath: str):
	"""
	:param sDataFilePath: This is the string file path for the CSV file
	"""
	try:	# ONLY WILL RUN THROUGH THE PROGRAM IF THE FILE PATH EXISTS
		with open(sDataFilePath, 'r', encoding="utf-8") as file:
			csvReaderBL = csv.DictReader(file)

			for row in csvReaderBL:
				listTotalPricesBL.append(float(row["price"]))

				# This below if/else checks were, for some reason, extremely difficult to figure out
				if row["city"] not in dictAllPricesBL["city"]: dictAllPricesBL["city"][row["city"]] = float(row["price"])
				else: dictAllPricesBL["city"][row["city"]] += float(row["price"])
				
				if row["type"] not in dictAllPricesBL["type"]: dictAllPricesBL["type"][row["type"]] = float(row["price"])
				else: dictAllPricesBL["type"][row["type"]] += float(row["price"])

				if row["zip"] not in dictAllPricesBL["zip"]: dictAllPricesBL["zip"][row["zip"]] = float(row["price"])
				else: dictAllPricesBL["zip"][row["zip"]] += float(row["price"])


	except FileNotFoundError:	# No file, alert and close
		print(f"An error has occured: THE FILE AT: {sDataFilePath} HAS NOT BEEN FOUND")
		print("EXITING PROGRAM")
		sys.exit()


			
	


def main():
	sFilePathBL = "RealEstateData.csv"

	getDataInput(sFilePathBL)	# if the file isn't found at the path above, it will close after declaring the error
	fMedianDataBL = getMedian(listTotalPricesBL)

	print("Summary by: PRICE")
	print(f"Minimum: ${min(listTotalPricesBL):,.2f}")
	print(f"Maximum: ${max(listTotalPricesBL):,.2f}")
	print(f"Sum: ${sum(listTotalPricesBL):,.2f}")
	print(f"Average: ${sum(listTotalPricesBL) / len(listTotalPricesBL):,.2f}")	# Average = sum of all / 2
	print(f"Median: ${fMedianDataBL:,.2f}")

	print("\nSummary by: CITY")
	for city, price in dictAllPricesBL["city"].items(): print(f"{city}: ${price:,.2f}")

	print("\nSummary by: PROPERTY TYPE")
	for property, price in dictAllPricesBL["type"].items(): print(f"{property}: ${price:,.2f}")

	print("\nSummary by: ZIP")
	for zip, price in dictAllPricesBL["zip"].items(): print(f"{zip}: ${price:,.2f}")


if __name__ == "__main__": main()
