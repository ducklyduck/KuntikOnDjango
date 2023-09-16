from django.shortcuts import render
from Shop.models import *
from Shop.HelpFunction import *

def product_page(request, id_kuntic):
    kuntic = Kuntic.objects.get(id=id_kuntic)

    return render(request, 'kuntic.html', context={'kuntic':get_format_kuntic(kuntic)})

def create_view(request):
    materials = Material.objects.all()
    materialArray = []
    for material in materials:
        materialArray.append({'price': material.price, 'materialName': material.material, 'massa': material.massa})
    sizes = Size.objects.all()
    sizeArray = []
    for size in sizes:
        sizeArray.append({'price': size.price, 'sizeName': size.title, 'massa': size.massa})
    colors = Color.objects.all()
    colorArray = []
    for color in colors:
        colorArray.append({'price': color.price, 'colorName': color.title})
    return render(request, 'custom-kuntic.html', context={'material': materialArray, 'size': sizeArray, 'color': colorArray})


def katalog_view(request):

    _all_kuntics = get_all_kuntics()
    all_kuntic = []
    for kuntic in _all_kuntics:
        all_kuntic.append(get_format_kuntic(kuntic))

    return render(request, 'catalog.html', context={'kuntics':all_kuntic})


def orders_view(request):
    return render(request, 'order.html', context={'orders': get_orders_users(request.user.id)})