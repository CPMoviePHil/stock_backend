from django.http import JsonResponse
from crawler_app.models import PCHStock
import time
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def list_of_stock_by_date(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            # return JsonResponse({"data": data})
            if 'search_date' in data:
                search_date = data['search_date']
                search_date = datetime.strptime(search_date.split(' ')[0], '%Y/%m/%d')
                start_datetime = search_date.replace(hour=0, minute=0, second=0)
                end_datetime = search_date.replace(hour=23, minute=59, second=59)
                list_stock = PCHStock.objects.filter(
                    create_datetime__gte=start_datetime,
                    create_datetime__lte=end_datetime
                )
                result_data = []
                for item in list_stock:
                    temp_obj = {}
                    temp_obj['stock_name'] = item.stock_name
                    temp_obj['buy_price'] = item.buy_price
                    temp_obj['sell_price'] = item.sell_price
                    temp_obj['average_buy_price'] = item.average_buy_price
                    temp_obj['average_sell_price'] = item.average_sell_price
                    temp_obj['net_buy'] = item.net_buy
                    temp_obj['stock_date'] = item.stock_date
                    result_data.append(temp_obj)
                return JsonResponse({
                    "data": result_data,
                })
    except Exception as e:
        raise e
