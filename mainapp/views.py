from django.shortcuts import render
from datetime import datetime

nowdate = datetime.date
print(nowdate)

def index(request):
    menu_links = [
        {'view_name': 'index', 'name': 'домой'},
        {'view_name': 'products', 'name': 'продукты'},
        {'view_name': 'contact', 'name': 'контакт'},
    ]
    return render(request, 'mainapp/index.html', context={
        'menu_links': menu_links})


def contact(request):
    menu_links = [
        {'view_name': 'index', 'name': 'домой'},
        {'view_name': 'products', 'name': 'продукты'},
        {'view_name': 'contact', 'name': 'контакт'},
    ]
    return render(request, 'mainapp/contact.html', context={
        'menu_links': menu_links})


def products(request):
    menu_links = [
        {'view_name': 'index', 'name': 'домой'},
        {'view_name': 'products', 'name': 'продукты'},
        {'view_name': 'contact', 'name': 'контакт'},
    ]
    links_menu = [
        {'href': 'products', 'name': 'все'},
        {'href': 'products', 'name': 'дом'},
        {'href': 'products', 'name': 'офис'},
        {'href': 'products', 'name': 'модерн'},
        {'href': 'products', 'name': 'классика'},
    ]
    return render(request, 'mainapp/products.html', context={
        'menu_links': menu_links, 'links_menu': links_menu})
