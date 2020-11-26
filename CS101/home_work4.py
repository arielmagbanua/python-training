import csv
from typing import List, Tuple

stocks_path = 'D:\Training\python-training\CS101\stock.csv'

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
        raise NotImplementedError

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
    


if __name__ == "__main__":
    # csv_load_example()
    # test your implementation
    stock_tuples = make_stock_tuples(stocks_path)
    markets = convert_to_objects(stock_tuples)

