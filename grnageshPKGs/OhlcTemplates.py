import datetime
import backtrader.feeds as btfeeds

class CommodityOHLC(btfeeds.GenericCSVData):

    params = (
        ('fromdate', datetime.datetime(2008, 1, 1)),
        ('todate', datetime.datetime(2015, 12, 31)),
        ('nullvalue', 0.0),
        ('dtformat', ('%m/%d/%Y')),
        ('datetime', 0),
        ('high', 4),
        ('low', 5),
        ('open', 3),
        ('close', 6),
        ('volume', 8),
        ('openinterest', 11)
    )

    def __init__(self):
        super(CommodityOHLC, self).__init__()

class EquityOHLC(btfeeds.GenericCSVData):

    params = (
        ('fromdate', datetime.datetime(2008, 1, 1)),
        ('todate', datetime.datetime(2015, 12, 31)),
        ('nullvalue', 0.0),
        ('dtformat', ('%d-%b-%y')),
        ('datetime', 2),
        ('high', 5),
        ('low', 6),
        ('open', 4),
        ('close', 8),
        ('volume', 10),
    )

    def __init__(self):
        super(EquityOHLC, self).__init__()

class CurrencyOHLC(btfeeds.GenericCSVData):

    params = (
        ('fromdate', datetime.datetime(2016, 12, 14)),
        ('todate', datetime.datetime(2017, 3, 9)),
        ('nullvalue', 0.0),
        ('dtformat', ('%d-%b-%y')),
        ('datetime', 0),
        ('high', 2),
        ('low', 3),
        ('open', 1),
        ('close', 4),
        ('volume', 7),
        ('openinterest', 8),
    )

    def __init__(self):
        super(CurrencyOHLC, self).__init__()
