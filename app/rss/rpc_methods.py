from modernrpc.core import rpc_method
from rss.models import ExchangeRate

@rpc_method
def add_exchange_rate(base_currency, target_currency, value, date):
    if not ExchangeRate.objects.filter(base_currency=base_currency, target_currency=target_currency, value=value):
        rate = ExchangeRate(base_currency=base_currency, target_currency=target_currency, value=value, timestamp=date)
        rate.save()
        return 'success'
    else:
        return 'item already exists'