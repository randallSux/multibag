# multibag
Easy-peasy portfolio tracker for crypto currencies. Allows you to track value in whatever currency you choose, as well as track the total value of multiple portfolios

# How to use
1)  Create a file called "bagsRaw.txt". This will be the file in which you put all the data you want the program to perform calculations on. You can use "bagsRawExample.txt" and simply change the name to see the program run.
2)  Inside bagsRaw, you'll need to put in lines for each "bag", and then each "multibag". Multibags simply sum ewach bag and have thier own targets and stoplosses. You can read more about how to format each line below.
3)  Run the program in a python environment. You can use python's IDLE. When you run the program, you'll have to say how many bag lines and how many multibag lines there are. Be aware that the number of bag lines is the number of bag declaration lines plus the number of bag transfer statements.

# Formatting bag lines
Each bag line has two parts. The first part is the **bag declaration**. This is only one line and tells the program what coin you're holding, how much of it you're holding, and some other stuff. The SECOND part is the **bag transfer statement(s)**. Notice that "statement(s)" means you can have one, or more than one, statement. These statements tell the program how you're going to get your actual holding into your currency of choice. They explain each trade or transfer you'll make, and on which exchanges, to allow the program to give you an actual result for how much your bag will be worth after all these trades are complete. This is great, because we all hate it when coinmarketcap says your holding is worth so many satoshis, but after trading fees you end up with a completely different number. So, lets get into it.

####Bag Declaration Lines
For **bag declarations** you'll format each line like this:
`<bag number>,<TKR>,<Amount>,<Target>,<Stoploss>,<Target TKR>`
**Be sure to separate each variable with commas, with no comma at the end of the line**

Here's what each part does:
- `<bag number>` is an integer that helps the program identify each bag. The bag numbers should start at `1` and increase from there, in order, without skipping any numbers.
- `<TKR>` is the ticker symbol of the coin you're holding. For Bitcoin it should be `BTC`.
- `<Amount>` is the amount of that coin you're holding. If you have half a bitcoin, it should be `0.5`. This number should be a floating point decimal value
- `<Target>` is the target value of your holdings (in terms of your `<Target TKR>`. Note that **this is the value of your entire holdings, NOT the value per coin**. If you're waiting for your holding of 10 ETH to reach a total value of 1 BTC, you should put `1` here and not `0.1`, which would be the cost per ETH in that case.
- `<Stoploss>` works the same way as `<Target>` except you'll only be alerted if your holdings fall below that amount
- `<Target TKR>` is the ticker symbol of whatever you want to turn your holdings into. So, if you're holding ETH, and you want to sell for BTC, then your `<Target TKR>` is `BTC`

Lets look at the first line in bagsRawExample.txt:
`1,BTC,0.00089606,9999,0,USDT`

This line means that you are holding 0.0089606 BTC, and you are waiting for it to surpass 9999 USDT in value. Your stoploss is at 0 USDT in value. You'll be alerted if your holding goes above the target of 9999 USDT or below the stoploss of 0 USDT.

####Bag Transfer Statements
For **bag transfer statements** you'll format each line like this:
`>,<toTKR>,<Exchange>,<pFee>,<cFee>`
Again, **be sure to separate each variable with commas, with no comma at the end of the line.**
Unlike with Bag Declaration lines, **be sure to include a `>` at the beginning of each bag transfer statement line**

Here's what each part does:
- `>` just needs to happen at the beginning of a bag transfer statement, to tell the program that's what it's doing
- `<toTKR>` is the ticker symbol of the first coin you'll trade the coin to. This command has alot going on, so read carefully here. If you're trading to a coin in which the base of the trading pair is NOT `<toTKR>`, you'll need to insert a `!` before `<toTKR>`. This can be seen in bagsRawExample.txt, line 5. The `<toTKR>` is `!GAS`, indicating that GAS is not the base of the trading pair, but rather that the program that the ticker specified on the line above is. If you aren't sure, take the price given on the exchange, and consider whether you'd need to multiply it with your original coin amount to get the accurate amount of the final coin, or divide your original coin by it. If you need to divide, then add a `!`.
- `<Exchange>` is simply the name of the exchange. If you're using Binance, then its `binance`. You don't need the ".com" on the end of exchanges. This code uses the CryptoCompare API, so it only supports exchanges that are supported there. AFAIK, Cryptobridge is the only major one that doesn't work.
- `<pFee>` is the percentage fee charged to perform that trade. This is expressed as a floating point decimal number. For 0.1%, use 0.001, not 0.1. The program will subtract this percentage from your holdings in its calculations
- `<cFee>` is the constant fee charged or associated with that trade. Typically this is ued for transfers between exchanges. `cFee` will be subtracted after the trade calculation is complete, so express it as the amount in `<toTKR>` that'll be subtracted. If you have to transfer from one exchange to another, you want to include your transfer fee on the last line associated with a trade on the first exchange, rather than on the first line associated with a trade on the second exchange.

####MultiBag Lines
Multibag lines describe your multibags, and are essentially portfolios. You can use Multibags to total up the value of multiple different bags, which are described above, and then set targets and stoplosses for the entire multibag. For instance, if you held BTC, ETH, and XMR, and wanted to get an alert whenever the USDT value of those holdings was above or below a certain value, you could create a bag for each holding, and then a multibag for all three together. Multibag lines are declared in bagsRaw.txt immediately after bag lines.

Multibag statements are formatted like so:
`M<Multibag number>,<num bags included>,<list of bags>,<target>,<stoploss>`

For each element in the multibag declaration...
- `M<Multibag number>` is the letter M, followed by the number of your multibag. These should start with `M1` and continue with `M2`, `M3`, etc.
- `<num bags included>` is an integer that says how many bags comprise this multibag. If your multibag contains BTC, ETH, and XMR, this field should be `3`
- `<list of bags>` is a comma separated list of the bag identifiers that are included. In the BTC/ETH/XMR bag mentioned above, if BTC's bag number is 2, ETH's bag number is 3, and XMR's bag number is 6, this field should be `2,3,6,`
- `<target>` is just the target total value for the multibag. This value should be in the currency that each bag is calculated for. 
- `<stoploss>` is similar to target, but its the stoploss for this multibag.
