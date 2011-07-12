from django.core.management.base import BaseCommand, CommandError

from exchange_rate.utils import get_exchange_currency_entries
from exchange_rate.models import ExchangeRate

class Command(BaseCommand):

    def handle(self, *args, **options):
      entries = get_exchange_currency_entries()
      try:
          entries = get_exchange_currency_entries(args[0])
      except:
          pass
      for raw_currency in entries:
            other_currency = raw_currency['title_detail']['value'].split('/')[0]
            base_currency = raw_currency['title_detail']['value'].split('/')[1]
            b_raw = raw_currency['summary'].split('=')[0].split(' ')
            base_currency_name = ''
            for b in b_raw[1:]:
                base_currency_name = base_currency_name + ' ' + b
            base_currency_name = base_currency_name.strip() 
            o_raw = raw_currency['summary'].split('=')[1].strip().split(' ')
            other_currency_name = ''
            for o in o_raw[1:]:
                other_currency_name = other_currency_name + ' ' + o
            other_currency_name = other_currency_name.strip()
            exchange_rate = o_raw[0]
            try:
                exchange_rate_obj = ExchangeRate.objects.get(base_currency=base_currency, other_currency=other_currency)
                exchange_rate_obj.exchange_rate = exchange_rate
                exchange_rate_obj.save()
            except:
                exchange_rate_obj = ExchangeRate(base_currency=base_currency, base_currency_name=base_currency_name, other_currency=other_currency, 
                    other_currency_name=other_currency_name, exchange_rate=exchange_rate)
                exchange_rate_obj.save()
