Fout = open("bagsRawGen.txt", "w")

inputtingBags = True
inputtingMBags = True
bagNumber = 1
MbagNumber = 1

while inputtingBags:

		fromTicker = input("What coin are you holding?")
		amount = input("How much of this coin are you holding?")
		finalTicker = input("What coin are you planning to trade this to? (Examples: USDT, BTC, ETH):")
		target = input("What's your target value for this holding? Please enter the total value of your holding in " + finalTicker + ":")
		SL = input("What's your stoploss value for this holding? Please enter the total value of your holding in " + finalTicker + ":")

		Fout.write(str(bagNumber) + "," + fromTicker + "," + amount + "," + target + "," + SL + "," + finalTicker + "\n")
		bagNumber = bagNumber + 1

		enteringTrades = True
		firstTrade = True


		while enteringTrades:

				if firstTrade:
						toTicker = input("What coin will you trade this holding to first?")
				else:
						toTicker = input("What coin will you trade this holding to next?")

				exchange = input("What exchange will this trade happen on?")
				isBase = input("Is the price on this exchange expressed as " + toTicker + "/" + fromTicker + "? (enter ""y"" or ""n""): ")

				if isBase == "n":
						toTicker = str("!" + str(toTicker))

				pFee = input("Are there any percentage based fees? If so, enter them as a percent. For 0.1%, enter 0.1:")
				pFee = str(float(pFee)*0.01)
				cFee = input("Are there any flat fees associated with this trade? For instance, a fee to transfer your coins to this exchange? Enter them as thier cost in " + fromTicker + ":")

				Fout.write(">" + toTicker + "," + exchange + "," + pFee + "," + cFee + "\n")

				moreTradesAnswer = input("Are more trades needed to get this holding into " + finalTicker + "? (enter ""y"" or ""n""):")

				fromTicker = toTicker

				firstTrade = False

				if moreTradesAnswer == "n":
						enteringTrades = False

		moreBagsAnswer = input("Are there any other bags you'd like to enter? (y/n):")

		if moreBagsAnswer == "n":
				inputtingBags = False

Fout.close();
dummy = input("Awesome! All Done :) Please press enter")

