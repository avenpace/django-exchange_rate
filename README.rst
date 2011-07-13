====================
Required library
====================
feedparser

====================
Project Description
====================

This django app will gave you realtime exchange rate that feed its data from http://themoneyconverter.com
The currency symbol that being used are 3 chars currency symbol base from ISO-4217

====================
Installation
====================
- Clone this repo by doing 'git clone git@github.com:avenpace/django-exchange_rate.git'
- Make sure you've put exchange_rate into your INSTALLED_APPS in your settings.py
- You need to have following things in your settings.py
  BASE_CURRENCY = 'USD' # or other currency symbol that you want to base on 
  USE_CURRENCY_CACHE = True # or False if you want to have realtime rate, if true that the rate will grab from ExchangeRate model that previously filled
- See utils.py for some exchange_rate method
- There's a command 'feed_exchange_rate' that will filled exchange_rate.models.ExchangeRate with all current currency exchange rate
  against base currency that you can define at BASE_CURRENCY on your settings.py
- You can put base currency symbol for 'feed_exchange_rate' on the first argument, ie: 'manage.py feed_exchange_rate USD' will feed all foreign exchange rate from US Dollar
- There is templatetag that will give you realtime currency exchange, to use this put '{% load exchange_rate %}' on first template line, 
  to get currency exchange rate use '{% get_exchange_rate currency_symbol base_currency_symbol(optional) %},
  or to calculate price to desired currency use '{% convert_price price currency_symbol base_currency_symbol(optional) %}
