#!/usr/bin/python
import argparse

# stock_prices = [1370, 350, 900, 7000, 5800, 3500]
stock_prices = [10, 50, 20]

def find_max_profit(prices):
  
#first stock is bought at a price in the list, it cannot be the last price
#second stock is sold at a price in the list, it cannot be the first price
#also the second stock must be after the first stock in the list
#the list will remain in the order given
#we need to find the maximum difference between 2 of the numbers while adhereing to the rules above
#first starting with index of 1 subtract each following value from that at index of 0, keep the maximum number
  for i in range(0, len(prices)-1):
    current_buy = prices[i]
    for j in range(i+1, len(prices)):
      current_sell = prices[j]
      for k in range (i+2, len(prices)):
        next_sell = prices[k]
    current_profit = current_sell - current_buy
    next_profit = next_sell - current_buy
    if next_profit > current_profit:
      return next_profit
    else: 
      return current_profit

print(find_max_profit(stock_prices))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))