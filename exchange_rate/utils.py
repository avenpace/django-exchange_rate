from django.conf import settings
import feedparser
from exchange_rate.models import ExchangeRate

CURRENCY_FEED_LINK = 'http://themoneyconverter.com/%s/rss.xml' % settings.BASE_CURRENCY

def get_exchange_currency(currency_symbol, base_currency=None):
    
    '''
    We are grabbing latest exchange currency rate from themoneyconverter.com
    Please change BASE_CURRENCY accordingly
    params :- currency_symbol, 3 chars currency symbol base from ISO-4217
                please see http://fx.sauder.ubc.ca/currency_table.html
            - base_currency, currency symbor ISO-4217 that you want to base to for calculation
    return : decimal currency rate
    '''
    #if USE_CURRENCY_CACHE are true, then find exchange rate from model that was pulled before
    if settings.USE_CURRENCY_CACHE:
        if base_currency:
            er = ExchangeRate.objects.get(other_currency=currency_symbol, base_currency=base_currency)
        else:
            er = ExchangeRate.objects.get(other_currency=currency_symbol, base_currency=settings.BASE_CURRENCY)
        return er.exchange_rate
    feed_exchange = feedparser.parse(CURRENCY_FEED_LINK)
    if base_currency:
        feed_exchange = feedparser.parse('http://themoneyconverter.com/%s/rss.xml' % base_currency)
    for raw in feed_exchange['entries']:
        if currency_symbol == raw['title_detail']['value'].split('/')[0]:
            _raw = raw['summary'].split('=')[1]
            return _raw.split(' ')[1]

def get_exchange_currency_entries(base_currency=None):
    '''
    We are grabbing latest exchange currency entries from themoneyconverter.com
    Please change BASE_CURRENCY accordingly
    params :  - base_currency, currency symbor ISO-4217 that you want to base to for calculation
    return : list of all exchange rate against base currency
    '''
    feed_exchange = feedparser.parse(CURRENCY_FEED_LINK)
    if base_currency:
        feed_exchange = feedparser.parse('http://themoneyconverter.com/%s/rss.xml' % base_currency)
    return feed_exchange['entries']

