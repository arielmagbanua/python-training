"""Task 4.1.

Complete two functions: make_stock_tuples, convert_to_objects
Complete three class implementations: Price, Stock, Market
(DO NOT TOUCH ATTRIBUTES OF EACH CLASS)
CAUTION: You CANNOT import any kind of module.

Use csv library to read and parse CSV format.
https://docs.python.org/3/library/csv.html

"""

import csv
from typing import Union, List, Tuple

stock_path = 'D:\Training\python-training\CS101\stock.csv'

def csv_load_example():
    with open(stock_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            print(row)


def make_stock_tuples(data_dir: str) -> List[Tuple[str, str, str, str, float, int]]:
    """

    Read the rows (exclude header) of the CSV and return them via tuple given data_dir.

    Args:
        data_dir (str)

    Returns:
        Tuple[str, str, str, str, float, int]: tuple consists of
        Date: str,
        Market: str,
        Company Name: str,
        Symbol: str,
        Price: float, and
        Volume: int

    """
    #################################################
    # YOUR CODE HERE
    #################################################
    stocks = []

    with open(data_dir, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')

        # convert reader to list
        stocks_data = list(reader)

        # slice the real stocks to exclude the header
        stocks_data = stocks_data[1::]

        # creae and append the sock tuples
        for stock in stocks_data:
            stock_tup = (str(stock[0]), str(stock[1]), str(stock[2]), str(stock[3]), float(stock[4]), int(stock[5]))
            stocks.append(stock_tup)
    
    return stocks


class Price:
    """Price class."""

    date: str
    price: float
    volume: int

    def __init__(self, date: str, price: float, volume: int):
        """
        Initialize new Price

        Args:
            date (str): date of price
            price (float): price for the date
            volume (int): volume of trading for the date

        """
        #################################################
        # YOUR CODE HERE
        #################################################
        self.date = date
        self.price = price
        self.volume = volume

    def __repr__(self):
        return "<Price %s>" % self.date


class Stock:
    """Stock class."""

    name: str
    symbol: str
    prices: List[Price]

    def __init__(self, name: str, symbol: str, prices: List[Price]):
        """
        Initialize new Stock

        Args:
            name (str): name of stock
            prices (List[Price]): list of price objects for the stock

        """
        #################################################
        # YOUR CODE HERE
        #################################################
        self.name = name
        self.symbol = symbol
        self.prices = prices    

    def __repr__(self):
        return "<Stock %s (%s)>" % (self.name, self.symbol)

    def get_highest_price(self, date: str) -> Union[float, str]:
        """
        Return a highest price between the given date and the previous 260 days of the given date.
        Details are in the document.
        
        Input arguments:
            date (str)
        Return:
            highest price (float)
            or error message (str)
        """
        #################################################
        # YOUR CODE HERE
        #################################################
        price_start_index = None
        for i in range(len(self.prices)):
            price_date = self.prices[i].date
            if date == price_date:
                price_start_index = i
                break
        
        if price_start_index == None or price_start_index < 259:
            return "Please check the date."

        # loop from the starting index to previous 260 records
        days = 1
        prices_between = []
        for i in reversed(range(price_start_index + 1)):
            if days > 260:
                # already exceeding 260 days so break the loop
                break
            
            prices_between.append(self.prices[i].price)
            days += 1

        highest_price = max(prices_between)
        return round(highest_price, 2)

    def get_lowest_price(self, date: str) -> Union[float, str]:
        """
        Return a lowest price between the given date and the previous 260 days of the given date.
        Details are in the document.
        
        Input arguments:
            date (str)
        Return:
            lowest price (float)
            or error message (str)
        """
        #################################################
        # YOUR CODE HERE
        #################################################
        price_start_index = None
        for i in range(len(self.prices)):
            price_date = self.prices[i].date
            if date == price_date:
                price_start_index = i
                break
        
        if price_start_index == None or price_start_index < 259:
            return "Please check the date."

        # loop from the starting index to previous 260 records
        days = 1
        prices_between = []
        for i in reversed(range(price_start_index + 1)):
            if days > 260:
                # already exceeding 260 days so break the loop
                break
            
            prices_between.append(self.prices[i].price)
            days += 1

        highest_price = min(prices_between)
        return round(highest_price, 2)

    def get_average_price(self, date: str) -> Union[float, str]:
        """
        Return an average price between the given date and the previous 260 days of the given date.
        Details are in the document.
        
        Input arguments:
            date (str)
        Return:
            agerage price (float, rounded to two decimal places)
            or error message (str)
        """
        #################################################
        # YOUR CODE HERE
        #################################################
        price_start_index = None
        for i in range(len(self.prices)):
            price_date = self.prices[i].date
            if date == price_date:
                price_start_index = i
                break
        
        if price_start_index == None or price_start_index < 259:
            return "Please check the date."

        # loop from the starting index to previous 260 records
        days = 1
        prices_between = []
        for i in reversed(range(price_start_index + 1)):
            if days > 260:
                # already exceeding 260 days so break the loop
                break
            
            prices_between.append(self.prices[i].price)
            days += 1
        
        avg = sum(prices_between) / 260.0
        return round(avg, 2)

    def get_average_volume(self, date: str) -> Union[float, str]:
        """
        Return an average volume between the given date and the previous 260 days of the given date.
        Details are in the document.
        
        Input arguments:
            year (int)
            month (int)
            day (int)
        Return:
            agerage volume (float, rounded to two decimal places)
            or error message (str)
        """
        #################################################
        # YOUR CODE HERE
        #################################################
        price_start_index = None
        for i in range(len(self.prices)):
            price_date = self.prices[i].date
            if date == price_date:
                price_start_index = i
                break
        
        if price_start_index == None or price_start_index < 259:
            return "Please check the date."

        # loop from the starting index to previous 260 records
        days = 1
        volumnes_between = []
        for i in reversed(range(price_start_index + 1)):
            if days > 260:
                # already exceeding 260 days so break the loop
                break

            volumnes_between.append(self.prices[i].volume)
            days += 1

        avg = sum(volumnes_between) / 260.0
        return round(avg, 2)

    def get_moving_average(self, date: str) -> Union[float, str]:
        """
        Return a moving average price between the given date and the previous 20 days of the given date.
        Details are in the document.
        
        Input arguments:
            date (str)
        Return:
            moving agerage price (float, rounded to two decimal places) 
            or error message (str)
        """
        #################################################
        # YOUR CODE HERE
        #################################################
        price_start_index = None
        for i in range(len(self.prices)):
            price_date = self.prices[i].date
            if date == price_date:
                price_start_index = i
                break
        
        if price_start_index == None or price_start_index < 19:
            return "Please check the date."

        # loop from the starting index to previous 260 records
        days = 1
        prices_between = []
        for i in reversed(range(price_start_index + 1)):
            if days > 20:
                # already exceeding 260 days so break the loop
                break

            prices_between.append(self.prices[i].price)
            days += 1
        
        avg = sum(prices_between) / 20.0
        return round(avg, 2)
    
    def get_bollinger_bands(self, date: str) -> Union[Tuple[float, float], str]:
        """
        Return a tuple of the upper band and lower band of bollinger band between the given date and
        the previous 20 days of the given date.
        Details are in the document.
        
        Input arguments:
            date(str)
        Return:
            bollinger band (Tuple[float, float], rounded to two decimal places)
            or error message (str)
        """
        #################################################
        # YOUR CODE HERE
        #################################################
        price_start_index = None
        for i in range(len(self.prices)):
            price_date = self.prices[i].date
            if date == price_date:
                price_start_index = i
                break
        
        if price_start_index == None or price_start_index < 19:
            return "Please check the date."
        

        # loop from the starting index to previous 260 records
        days = 1
        prices_between = []
        for i in reversed(range(price_start_index + 1)):
            if days > 20:
                # already exceeding 260 days so break the loop
                break

            prices_between.append(self.prices[i].price)
            days += 1
        
        n = len(prices_between)
        phat = self.get_moving_average(date)

        variance = sum([(p - phat) ** 2 for p in prices_between]) / (n - 1)
        std_dev = variance ** (1 / 2)

        upper = phat + (2 * std_dev)
        upper = round(upper, 2)
        lower = phat - (2 * std_dev)
        lower = round(lower, 2)

        return (upper, lower)

class Market:
    """Market class."""

    name: str
    stocks: List[Stock]

    def __init__(self, name: str, stocks: List[Stock]):
        """
        Initialize new Market

        Args:
            name (str): name of market
            stocks (List[Stock]): list of stock objects that belong to the market

        """
        #################################################
        # YOUR CODE HERE
        #################################################
        self.name = name
        self.stocks = stocks

    def __repr__(self):
        return "<Market %s>" % self.name


def convert_to_objects(stock_prices: List[Tuple[str, str, str, str, float, int]]) -> List[Market]:
    """

    Read the CSV file given stock_prices (output of make_stock_tuples function) and return list of 
    parsed Market objects.

    Args:
        stock_prices (Tuple[str, str, str, str, float, int]): output of make_stock_tuples function

    Returns:
        List[Market]: a list of parsed Market objects

    """
    #################################################
    # YOUR CODE HERE
    #################################################
    markets = []
    for stock_market_record in stock_prices:
        # unpack the stock_market_record
        date, market, company_name, symbol, price, volume = stock_market_record

        # creae the price object
        price = Price(date, price, volume)

        # check if market already created
        market_index = None
        for i in range(len(markets)):
            if markets[i].name == market:
                market_index = i
                break

        if market_index == None:
            # create the market object and add it to the market list
            new_market = Market(market, [])
            markets.append(new_market)
            market_index = -1

        # check if stock already created from the stock list of the current market
        stock_index = None
        for i in range(len(markets[market_index].stocks)):
            if markets[market_index].stocks[i].symbol == symbol:
                stock_index = i
                break

        if stock_index == None:
            # create the stock object with initial empty price list
            new_stock = Stock(company_name, symbol, [])
            # append the stock to the current market's stocks list
            markets[market_index].stocks.append(new_stock)
            stock_index = -1

        # add the price to the stock that belongs to the current market
        markets[market_index].stocks[stock_index].prices.append(price)

    return markets



if __name__ == "__main__":
    # csv_load_example()
    # test your implementation
    stock_tuples = make_stock_tuples(stock_path)
    markets = convert_to_objects(stock_tuples)
    # pass

    # for market_obj in markets:
    #     for stock in market_obj.stocks:
    #         print(stock.name, stock.symbol)
    #         for price in stock.prices:
    #             if price.date == '2019-02-04':
    #                 print(price.date, price.price)
    #                 break

    # for market_obj in markets:
    #     if market_obj.name == "NASDAQ":
    #         for stock in market_obj.stocks:
    #             if stock.symbol == "AAPL":
    #                 print(stock.get_highest_price("2020-02-03"))
    #                 print(stock.get_lowest_price("2020-02-03"))
    #                 print(stock.get_average_price("2020-02-03"))
    #                 print(stock.get_average_volume("2020-02-03"))
    #                 print(stock.get_highest_price("2017-02-03"))

    for market_obj in markets:
        if market_obj.name == "NASDAQ":
            for stock in market_obj.stocks:
                if stock.symbol == "AAPL":
                    print(stock.get_moving_average("2020-02-03"))
                    print(stock.get_bollinger_bands("2020-02-03"))
                    print(stock.get_moving_average("2017-02-03"))
                    print(stock.get_bollinger_bands("2017-02-03"))
