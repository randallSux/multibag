# multibag
Easy-peasy portfolio tracker for crypto currencies. Allows you to track value in whatever currency you choose, as well as track the total value of multiple portfolios

# How to use
1)  Create a file called "bagsRaw.txt". This will be the file in which you put all the data you want the program to perform calculations on. You can use "bagsRawExample.txt" and simply change the name to see the program run.
2)  Inside bagsRaw, you'll need to put in lines for each "bag", and then each "multibag". Multibags simply sum ewach bag and have thier own targets and stoplosses. You can read more about how to format each line below.

# Formatting bag lines
Each bag line has two parts. The first part is the bag declaration. This is only one line and tells the program what coin you're holding, how much of it you're holding, and some other stuff. The SECOND part is the bag transfer statement(s). Notice that "statement(s)" means you can have one, or more than one, statement. These statements tell the program how you're going to get your actual holding into your currency of choice. They explain each trade or transfer you'll make, and on which exchanges, to allow the program to give you an actual result for how much your bag will be worth after all these trades are complete. This is great, because we all hate it when coinmarketcap says your holding is worth so many satoshis, but after trading fees you end up with a completely different number. So, lets get into it.

For bag declarations, AKA part 1, you'll need to declare
