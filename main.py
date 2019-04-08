import urllib.request

#dictionaries
ticker = {}
amount = {}
finalAmt = {}
finalTicker = {}
target = {}
SL = {}
correctFinalTicker = {} #used to make sure you arrived at the correct coin
multibagTotal = {}


Fin = open("bagsRaw.txt", "r")

#input should look like:
#bagnum, ticker, amount, target, SL, finalTicker
#or
#>(!)nextTicker, exchange, pFee, cFee (pFee and cFee are percent fee and constant fee) (exclamation point indicates that whatever is the base of the pair)



#algo 2:
#read in each line (for)
#		if line starts with anything thats not a >, 
#			parse out the bagnum, ticker, then the amount held
#			create a new array element with index bagnum, store ticker and amount
#			store original amount and ticker in final and finalticker
#			set currentBag to current bag
#		else 
#			find exchange rate for pair, use ! to indicate base of trading pair
#			multiply final by exchange rate, then by (1-pFee), then subtract cFee, then store in final
#			update finalTicker

numBagLines = int(input("How many bag lines are there?"))#23
numMultibags = int(input("How many multiBag lines are there?"))#2



bagNum = 1
for x in range(0, numBagLines):
		thisLine = Fin.readline()
		if(thisLine[0] != ">"):
				firstComma = thisLine.index(",")
				bagNum = int(thisLine[:firstComma])
				thisLine = thisLine[firstComma+1:]
				secondComma = thisLine.index(",")
				thisTicker = thisLine[:secondComma]
				thisLine = thisLine[secondComma+1:]
				thirdComma = thisLine.index(",")
				thisAmount = thisLine[:thirdComma]
				thisLine = thisLine[thirdComma+1:]
				fourthComma = thisLine.index(",")
				thisTarget = thisLine[:fourthComma]
				thisLine = thisLine[fourthComma+1:]
				fifthComma = thisLine.index(",")
				thisSL = thisLine[:fifthComma]
				thisTargetTicker = thisLine[fifthComma+1:len(thisLine)-1]

				ticker[bagNum] = thisTicker
				amount[bagNum] = float(thisAmount)
				finalAmt[bagNum] = float(thisAmount)
				finalTicker[bagNum] = thisTicker
				target[bagNum] = float(thisTarget)
				SL[bagNum] = float(thisSL)
				correctFinalTicker[bagNum] = thisTargetTicker


				
		else:
				if(thisLine[1] == "!"):
						firstComma = thisLine.index(",")
						pairTick = thisLine[2:firstComma]
						thisLine = thisLine[firstComma+1:]
						secondComma = thisLine.index(",")
						exchange = thisLine[:secondComma]
						thisLine = thisLine[secondComma+1:]
						thirdComma = thisLine.index(",")
						pFee = float(thisLine[:thirdComma])
						cFee = float(thisLine[thirdComma+1:len(thisLine)-1])

						url2open = ("https://min-api.cryptocompare.com/data/price?fsym=" + pairTick + "&tsyms=" + finalTicker[bagNum] + "&e=" + exchange)
						#print(url2open)
						contents = urllib.request.urlopen(url2open)
						

						data = str(contents.read())
						#print(data)
						colon = data.index(":")
						closeBracket = data.index("}")
						price = float(data[colon+1:closeBracket])

						finalAmt[bagNum] = finalAmt[bagNum] / price * (1-pFee) - cFee
						finalTicker[bagNum] = pairTick

				else:
						firstComma = thisLine.index(",")
						pairTick = thisLine[1:firstComma]
						thisLine = thisLine[firstComma+1:]
						secondComma = thisLine.index(",")
						exchange = thisLine[:secondComma]
						thisLine = thisLine[secondComma+1:]
						thirdComma = thisLine.index(",")
						pFee = float(thisLine[:thirdComma])
						cFee = float(thisLine[thirdComma+1:len(thisLine)-1])

						url2open = ("https://min-api.cryptocompare.com/data/price?fsym=" + finalTicker[bagNum] + "&tsyms=" + pairTick + "&e=" + exchange)
						#print(url2open)
						contents = urllib.request.urlopen(url2open)
						

						data = str(contents.read())
						#print(data)
						colon = data.index(":")
						closeBracket = data.index("}")
						price = float(data[colon+1:closeBracket])

						finalAmt[bagNum] = finalAmt[bagNum] * price * (1-pFee) - cFee
						finalTicker[bagNum] = pairTick


		#print(str(finalAmt[bagNum]) + " " + finalTicker[bagNum])
print("~~Finished totaling bags~~")


for i in range(1,bagNum+1):
		if(finalAmt[i] >= target[i]):
				print("Bag " + str(i) + " has hit target at " + str(finalAmt[i]))
		elif(finalAmt[i] <= SL[i]):
				print("Bag " + str(i) + " has hit SL at " + str(finalAmt[i]))

print("~~Finished checking bags~~")

for y in range(1,numMultibags+1):
		thisLine = Fin.readline()
		firstComma = thisLine.index(",")
		thisLine = thisLine[firstComma+1:]
		secondComma = thisLine.index(",")
		numBagsInMB = int(thisLine[:secondComma])
		thisLine = thisLine[secondComma+1:]

		multibagTotal[y] = 0

		for z in range(0,numBagsInMB):
				nextComma = thisLine.index(",")
				bagToAdd = int(thisLine[:nextComma])
				multibagTotal[y] += finalAmt[bagToAdd]
				thisLine = thisLine[nextComma+1:]

		nextComma = thisLine.index(",")
		thisTarget = float(thisLine[:nextComma])
		thisSL = float(thisLine[nextComma+1:])

		if(multibagTotal[y] >= thisTarget):
				print("Multibag M" + str(y) + " has hit target at " + str(multibagTotal[y]))
		elif(multibagTotal[y] <= thisSL):
				print("Multibag M" + str(y) + " has hit stoploss at " + str(multibagTotal[y]))


print("~~Finished checking Multibags~~")

Fin.close()

