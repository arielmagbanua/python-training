import csv
from typing import List, Tuple, Union

stocks_path = 'D:\Training\python-training\CS101\stock.csv'

#################################################
# Task 4.1 Codes
#################################################

def csv_load_example():
    with open(stocks_path, newline='') as csvfile:
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

    with open(stocks_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')

        # convert reader to list
        stocks_data = list(reader)

        # slice the real stocks data to exclude the header
        stocks_data = stocks_data[1::]
        
        # create and append the stock tuples
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
        # unpack and get all the field values
        date, market, company_name, symbol, price, volume = stock_market_record

        # create the price object
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
    csv_load_example()
    # test your implementation
    stock_tuples = make_stock_tuples(stocks_path)
    markets = convert_to_objects(stock_tuples)
    print(markets)


