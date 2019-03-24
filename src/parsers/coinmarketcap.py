import json

from requests import Session, Timeout, TooManyRedirects

from src.settings import API_KEY


class CoinMarketCapParser:

    def portfolio_symbols(self):
        return 'MIOTA,ADA,XRP,QTUM,AION,WAN,ICX,NEO,BNB,GAS,ETH,LTC,SC,TRX,XLM,BTC'

    def convert_value_to(self):
        return 'USD'

    def quotes_latest(self):
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        parameters = {
            'symbol': self.portfolio_symbols(),
            'convert': self.convert_value_to(),
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': API_KEY,
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
        return self.portfolio_symbols().split(',')

    def parse_prices(self):
        prices = {coin: quote['quote'][self.convert_value_to()]['price'] for coin, quote in self.quotes_latest()['data'].items()}
        return prices


def test():
    coin = CoinMarketCapParser()
    # tmp = coin.parse_coins()
    # tmp = coin.quotes_latest()
    tmp = coin.parse_prices()
    print(tmp)


if __name__ == '__main__':
    test()
