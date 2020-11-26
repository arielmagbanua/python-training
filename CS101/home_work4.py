import csv
from typing import List, Tuple

def csv_load_example():
    with open('data/stock.csv', newline='') as csvfile:
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
    raise NotImplementedError

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
        raise NotImplementedError

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
        raise NotImplementedError

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
    raise NotImplementedError


if __name__ == "__main__":
    csv_load_example()
    # test your implementation
    stock_tuples = make_stock_tuples('dir/to/data.csv')
    markets = convert_to_objects(stock_tuples)
    pass
