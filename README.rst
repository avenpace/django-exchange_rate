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
- See utils.py for acquire exchange_rate method
- There's a command 'feed_exchange_rate' that will filled exchange_rate.models.ExchangeRate with all current currency exchange rate
  against base currency that you can define at BASE_CURRENCY on your settings.py
