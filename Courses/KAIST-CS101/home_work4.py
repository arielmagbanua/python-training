import csv
from typing import Optional, Union, List, Tuple

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
    stocks = []

    with open(data_dir, newline='') as csvfile:
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
        # get the starting index of the date
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
        # get the starting index of the date
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

        lowest_price = min(prices_between)
        return round(lowest_price, 2)

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
        # get the starting index of the date
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
        # get the starting index of the date
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
        volumes_between = []
        for i in reversed(range(price_start_index + 1)):
            if days > 260:
                # already exceeding 260 days so break the loop
                break

            volumes_between.append(self.prices[i].volume)
            days += 1

        avg = sum(volumes_between) / 260.0
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
        # get the starting index of the date
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
                # already exceeding 20 days so break the loop
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
        # get the starting index of the date
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
                # already exceeding 20 days so break the loop
                break

            prices_between.append(self.prices[i].price)
            days += 1

        n = len(prices_between)
        phat = self.get_moving_average(date)

        variance = sum([(x - phat) ** 2 for x in prices_between]) / (n - 1)
        std_dev = variance ** (1/2)

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


class Trader:
    """Trader class."""

    name: str
    balance: float
    holdings: Tuple[str, str, int, float]

    def __init__(self, name: str, balance: float):
        """
        Initialize new Trader

        Args:
            name (str): name of market
            balance (float): current cash the trader has
            holdings (Tuple[str, str, int, float]): tuple consists of
                Date: str,
                Ticker: str,
                the amount of the stock: int, and
                the price when you bought: float

        """
        self.holdings = tuple()
        self.name = name
        self.balance = balance

    def buy(self, ticker: str, price: float, date: str) -> None:
        """
        Update holdings and balance fields after buying.
        Details are in the document.
        
        Input arguments:
            ticker (str)
            price (float)
            date (str)
        Return:
            None
        """
        # check if there's current holding
        # if exist, buying additional stocks are not allowed
        if len(self.holdings) > 0 or self.balance < price:
            return

        # compute the maximum amount of stocks
        stock_amount = int(self.balance / price)

        # record the holding
        self.holdings = (date, ticker, stock_amount, price)

        # update the balance
        spent = stock_amount * price
        balance = self.balance - spent
        self.balance = round(balance, 2)

    def sell(self, ticker: str, price: float) -> None:
        """
        Update holdings and balance fields after selling.
        Details are in the document.
        
        Input arguments:
            ticker (str)
            price (float)
        Return:
            None
        """
        # check if there is holdings
        if len(self.holdings) == 0:
            return

        # unpack holding
        holdings_date, holdings_ticker, holdings_stock_amount, holdings_price = self.holdings

        if ticker == holdings_ticker:
            # calculate the total amount that can be sold
            sold = holdings_stock_amount * price

            # add the sold amount to the balance
            new_balance = self.balance + sold
            self.balance = round(new_balance, 2)

            # clean up holdings
            self.holdings = tuple()

    def check(self) -> Tuple[float, Tuple[str, str, int, float]]:
        """
        Return balance holdings fields.
        Details are in the document.
        
        Input arguments:
            None
        Return:
            Tuple[float, Tuple[str, str, int, float]]: tuple consists of
                balance (str), and
                holdings (Tuple[str, str, int, float])
        """
        return (self.balance, self.holdings)

    def simulate(self, markets: List[Market], ticker: str, date: str) -> Optional[str]:
        """
        Trading simulator with given date and ticker.
        Trading algorithm is as follows:
            1. You have to buy the stock when the price is lower than the lower band of the bollinger bands.
            2. You have to sell the stock when the price is higher than the upper band of the bollinger bands.
        Details are in the document.

        Input arguments:
            a list of parsed Market objects (List[Market])
            ticker (str)
            date (str)
        Return:
            None
            or error message (str)
        """
        # get the market and symbol from the ticker
        market = ""
        symbol = ""

        try:
            market, symbol = tuple(ticker.split(':'))
        except Exception:
            return "Please check the ticker."

        for market_obj in markets:
            if market_obj.name == market:
                for stock in market_obj.stocks:
                    if stock.symbol == symbol:
                        # get the starting index of the date
                        start_date_index = None
                        for i in range(len(stock.prices)):
                            if date == stock.prices[i].date:
                                start_date_index = i
                                break

                        if start_date_index == None:
                            return "Please check the date."

                        # simulate from the designated starting date up to the last date
                        for stock_price in stock.prices[start_date_index::]:
                            bollinger_result = stock.get_bollinger_bands(stock_price.date)

                            if isinstance(bollinger_result, str):
                                return bollinger_result

                            # get the bollinger bands
                            upper_band, lower_band = bollinger_result

                            # buy if stock price is lower than the lower bollinger band
                            if stock_price.price < lower_band:
                                self.buy(ticker, stock_price.price, stock_price.date)

                            # sell if price is higher than
                            if stock_price.price > upper_band:
                                self.sell(ticker, stock_price.price)

    def __repr__(self):
        return "<Trader %s>" % self.name


if __name__ == "__main__":
    # csv_load_example()
    # test your implementation
    stock_tuples = make_stock_tuples(stock_path)
    markets = convert_to_objects(stock_tuples)

    # for market_obj in markets:
    #     for stock in market_obj.stocks:
    #         print(stock.name, stock.symbol)
    #         for price in stock.prices:
    #             if price.date == '2019-02-04':
    #                 print(price.date, price.price)
    #                 break

    for market_obj in markets:
        if market_obj.name == "NASDAQ":
            for stock in market_obj.stocks:
                if stock.symbol == "AAPL":
                    print(stock.get_highest_price("2020-02-03"))
                    print(stock.get_lowest_price("2020-02-03"))
                    print(stock.get_average_price("2020-02-03"))
                    print(stock.get_average_volume("2020-02-03"))
                    print(stock.get_highest_price("2017-02-03"))

    # for market_obj in markets:
    #     if market_obj.name == "NASDAQ":
    #         for stock in market_obj.stocks:
    #             if stock.symbol == "AAPL":
    #                 print(stock.get_moving_average("2020-02-03"))
    #                 print(stock.get_bollinger_bands("2020-02-03"))
    #                 print(stock.get_moving_average("2017-02-03"))
    #                 print(stock.get_bollinger_bands("2017-02-03"))

    # t = Trader("Warren Buffet", 1000.)
    # t.simulate(markets, "NASDAQ:AAPL", "2019-02-01")
    # print(t.check())
    # t = Trader("Warren Buffet", 1000.)
    # t.simulate(markets, "NYSE:JNJ", "2019-02-01")
    # print(t.check())

    # insufficient balance test cases
    # t = Trader("Warren Buffet", 20.0)
    # t.simulate(markets, "NASDAQ:AAPL22", "2019-02-01")
    # print(t.check())
    # t = Trader("Warren Buffet", 20.0)
    # t.simulate(markets, "NYSE:JNJ22", "2019-02-01")
    # print(t.check())

    # wrong date test cases
    # t = Trader("Warren Buffet", 1000.)
    # result = t.simulate(markets, "NASDAQ:AAPL", "2019-01-03")
    # print(result)
    # print(t.check())
    # t = Trader("Warren Buffet", 1000.)
    # result = t.simulate(markets, "NASDAQ:AAPL", "2020-11-11")
    # print(result)
    # print(t.check())

    # wrong ticker
    # t = Trader("Warren Buffet", 1000.)
    # result = t.simulate(markets, "WARREN:BUFFET", "2019-01-03")
    # print(result)
    # print(t.check())

    # t = Trader("Warren Buffet", 1000.)
    # result = t.simulate(markets, "WARREN", "2019-01-03")
    # print(result)
    # print(t.check())
