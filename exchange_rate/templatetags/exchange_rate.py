from django.template import Library, Node, TemplateSyntaxError
from exchange_rate.utils import get_exchange_currency

class ExchangeRateTag(Node):

    def __init__(self, currency_symbol, base_currency_symbol=None):
        self.currency_symbol = currency_symbol
        self.base_currency_symbol = base_currency_symbol

    def render(self, context):
        if self.base_currency_symbol:
            return get_exchange_currency(self.currency_symbol, self.base_currency_symbol)
        return get_exchange_currency(self.currency_symbol)

def get_exchange_rate(parser, token):
    bits = token.contents.split()
    if len(bits) <= 3:
        raise TemplateSyntaxError('please pass arguments to this tag, ie {% get_exchange_rate currency_symbol base_currency_symbol(optional) %}')
    if len(bits) == 3:
        return ExchangeRateTag(bits[1], bits[2])
    else:
        return ExchangeRateTag(bits[1])

class ConvertPriceTag(Node):

    def __init__(self, price, currency_symbol, base_currency_symbol=None):
        self.price = price
        self.currency_symbol = currency_symbol
        self.base_currency_symbol = base_currency_symbol
    
    def render(self, context):
        rate = None
        if self.base_currency_symbol:
            rate = get_exchange_currency(self.currency_symbol, self.base_currency_symbol)
        else:
            rate = get_exchange_currency(self.currency_symbol)
        return (self.price * rate)


def convert_price(parser, token):
    bits = token.contents.split()
    if len(bits) <= 4:
        raise TemplateSyntaxError('please pass arguments to this tag, ie {% get_exchange_rate price currency_symbol base_currency_symbol(optional) %}') 
    if len(bits) == 4:
        return ConvertPriceTag(bits[1], bits[2], bits[3])
    else:
        return ConvertPriceTag(bits[1], bits[2])

register = Library()
register.tag(get_exchange_rate)
register.tag(convert_price)
