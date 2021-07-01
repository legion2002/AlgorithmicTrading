import time
import xlsxwriter

from datetime import datetime

money = 10000
stocks = {}
net = 10000
watchlist = ["INFY", "RELIANCE", "MRF"]
row = 0
workbook = xlsxwriter.Workbook('orderbook.xlsx')
worksheet = workbook.add_worksheet()
def buysignal():
    pass

def sellsignal(stock, quantity):
    pass

def buy(stock, quantity):
    global row
    print("entered")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    worksheet.write(row,0,current_time)
    worksheet.write(row,1,"BUY")
    worksheet.write(row,2,stock)
    worksheet.write(row, 3, quantity)

    row += 1



def sell(stock, quantity):
    global row
    print("entered")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    workbook = xlsxwriter.Workbook('orderbook.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(row, 0, current_time)
    worksheet.write(row, 1, "SELL")
    worksheet.write(row, 2, stock)
    worksheet.write(row, 3, quantity)

    row += 1



if __name__ == "__main__":
    buy("a",100)
    sell("a", 50)



