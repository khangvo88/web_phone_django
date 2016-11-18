
from django.db.models import Count
from cellphones.models import *


def load_menu(request):
    categories = Device.list_category()
    producer_list = Device.objects.filter(status=STATUS_ACTIVE).values('category', 'producer'). \
        annotate(num_product=Count('pk')).order_by('num_product'). \
        values('category', 'producer', 'producer__name', 'num_product', 'producer__description')

    categories_menu = {}
    producer_list_menu = {}
    for x in producer_list:
        producer_info = {"name": x["producer__name"],
                         "id": x["producer"],
                         "num_product": x["num_product"],
                         "desc": x["producer__description"]}
        if x["category"] in categories_menu:
            categories_menu[x["category"]]['producers'].append(producer_info)
        else:
            categories_menu[x["category"]] = {'name': categories[x["category"]], 'producers': [producer_info]}
        if x["producer"] in producer_list_menu:
            producer_list_menu[x["producer"]]['num_product'] += x["num_product"]
        else:
            producer_list_menu[x["producer"]] = producer_info
    return {'categories':categories_menu, 'producer_list': producer_list_menu}