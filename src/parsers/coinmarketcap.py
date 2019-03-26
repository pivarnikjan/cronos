import json

from requests import Session, Timeout, TooManyRedirects

from src.settings import CMC_API_KEY


class CoinMarketCapParser:

    def __init__(self):
        self._portfolio_symbols = 'MIOTA,ADA,XRP,QTUM,AION,WAN,ICX,NEO,BNB,GAS,ETH,LTC,SC,TRX,XLM,BTC'
        self._converting_currency = 'USD'

    @property
    def portfolio_symbols(self):
        return self._portfolio_symbols

    @portfolio_symbols.setter
    def portfolio_symbols(self, value):
        self._portfolio_symbols = value

    @portfolio_symbols.deleter
    def portfolio_symbols(self):
        del self._portfolio_symbols

    @property
    def converting_currency(self):
        return self._converting_currency

    @converting_currency.setter
    def converting_currency(self, value):
        self._converting_currency = value

    @converting_currency.deleter
    def converting_currency(self):
        del self._converting_currency

    def quotes_latest(self):
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        parameters = {
            'symbol': self.portfolio_symbols,
            'convert': self.converting_currency,
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': CMC_API_KEY,
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            return data
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

    def parse_coins(self):
        return self.portfolio_symbols.split(',')

    def parse_prices(self):
        prices = {coin: quote['quote'][self.converting_currency]['price'] for coin, quote in self.quotes_latest()['data'].items()}
        return prices


def test():
    coin = CoinMarketCapParser()
    # tmp = coin.parse_coins()
    # tmp = coin.quotes_latest()
    tmp = coin.parse_prices()
    print(tmp)


if __name__ == '__main__':
    test()
