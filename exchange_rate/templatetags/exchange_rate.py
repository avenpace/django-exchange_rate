from django.template import Library, Node, TemplateSyntaxError
from exchange_rate.utils import get_exchange_currency

class ExchangeRateTag(Node):

    def __init__(self, currency_symbol, base_currency_symbol):
        self.currency_symbol = currency_symbol
        self.base_currency_symbol = base_currency_symbol

    def render(self, context):
        return get_exchange_currency(self.currency_symbol, self.base_currency_symbol)

def get_exchange_rate(parser, token):
    bits = token.contents.split()
    if len(bits) != 3:
        raise TemplateSyntaxError(('please pass two arguments to this tag, currency_symbol and base_currency_symbol'))
    return ExchangeRateTag(bits[1], bits[2])

register = Library()
register.tag(get_exchange_rate)
