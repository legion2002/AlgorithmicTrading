# AlgorithmicTrading
In this project I explore paper algorithmic trading, using a simple moving averages strategy.

## Simple Moving Average Strategy
> 2 simple moving averages of different time periods are taken, I use SMA60 and SMA200.
> **Buy Signals** are generated when the shorter SMA crosses over the longer period SMA from below.
> **Sell Signals** are generated when the shorter SMA crosses below the longer period SMA from above.
> To read more about this strategy you can go to - [Investopedia Article](https://www.investopedia.com/articles/active-trading/052014/how-use-moving-average-buy-stocks.asp)

## Results
>Considering that this is a very basic strategy the results observed were pretty good. In falling stocks the loss was reduced and in rising stocks the profit was increased.
>Having said that the strategy is far from ready for daily use in trading, as can be seen through the graphs in the colab notebook, you can see that it has a decent inaccuracy
>rate.

## Instructions
+ Go to this colab noteboook - [AlgoTradingFinal Colab Link](https://colab.research.google.com/drive/1m5COVqdVOByWF9H8AFuR8MNlB7ovxR3A?usp=sharing)
+ Run the blocks according to instructions in the notebook, change the stock code in the first block of the notebook according to your preference
+ __Note:__ Only stock codes listed in NASDAQ exchange are available
+ __Note:__ Running the code multiple times might lead to expiration of alpha vantage API calls, so please try again later.
