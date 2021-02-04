from django.http import JsonResponse
from crawler_app.models import PCHStock
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def list_of_stock_by_date(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            if 'search_date' in data:
                items = PCHStock.objects.all()
                list_stock = list_filter_by_date(items, data['search_date'])
                return parsed_list(list_stock)
            else:
                return none_response()
    except Exception as e:
        raise e


@csrf_exempt
def stock_by_name(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            if 'search_name' in data:
                items = PCHStock.objects.filter(stock_name=data['search_name'])
                if 'search_date' in data:
                    items = list_filter_by_date(items, data['search_date'])
                return parsed_list(items)
            else:
                return none_response()
    except Exception as e:
        raise e


def list_filter_by_date(items, search_date):
    search_date = datetime.strptime(search_date.split(' ')[0], '%Y/%m/%d')
    start_datetime = search_date.replace(hour=0, minute=0, second=0)
    end_datetime = search_date.replace(hour=23, minute=59, second=59)
    list_stock = items.filter(
        create_datetime__gte=start_datetime,
        create_datetime__lte=end_datetime
    )
    return list_stock


def parsed_list(list_stock):
    result_data = []
    for item in list_stock:
        temp_obj = {
            'stock_name': item.stock_name,
            'buy_price': item.buy_price,
            'sell_price': item.sell_price,
            'average_buy_price': item.average_buy_price,
            'average_sell_price': item.average_sell_price,
            'net_buy': item.net_buy,
            'stock_date': item.stock_date
        }
        result_data.append(temp_obj)
    return JsonResponse({
        "data": result_data,
    })


def none_response():
    return JsonResponse({
        "data": []
    })
