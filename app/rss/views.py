import json

from django.shortcuts import render, HttpResponse
from django.views import View
from rss.models import ExchangeRate

# Create your views here.
class IndexView(View):
    def get(self, request):
        exchange_data = {}
        base = request.GET.get('base')
        target = request.GET.get('target')
        if base and target:
            results = ExchangeRate.objects.filter(base_currency=base, target_currency=target).order_by('-timestamp')
            result = results.values_list()[0]
            exchange_data = {
                "target": target,
                "base": base,
                "value": result[3],
                "date": result[4]
            }
        return render(request, 'index.html', context=exchange_data)
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            base = data.get('base')
            target = data.get('target')
            if base and target:
                results = ExchangeRate.objects.filter(base_currency=base, target_currency=target).order_by('-timestamp')
                result = results.values_list()[0]
                return HttpResponse(f'{result[1]} -> {result[2]} = {result[3]} on {result[4]}') or HttpResponse('Bad base or target currency', status=400)
            return HttpResponse('Bad request', status=400)
        except:
            return HttpResponse('Bad request format', status=400)