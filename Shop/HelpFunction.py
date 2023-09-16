from .models import *


def get_all_kuntics():
    return Kuntic.objects.filter(custom=False)


def add_kuntic(_title, _color, _material, _size):
    kuntic = Kuntic()
    kuntic.title = _title
    kuntic.color = _color
    kuntic.material = _material
    kuntic.size = _size
    kuntic.save()


def add_custom_kuntic(_title, _color, _material, _size):
    kuntic = Kuntic()
    kuntic.title = _title
    kuntic.color = _color
    kuntic.material = _material
    kuntic.size = _size
    kuntic.custom = True
    kuntic.save()


def add_custom_with_extra(_title, _color, _material, _size, _extra):
    kuntic = Kuntic()
    kuntic.title = _title
    kuntic.color = _color
    kuntic.material = _material
    kuntic.size = _size
    kuntic.custom = True
    kuntic.extra = _extra
    kuntic.save()


def add_to_order(_kuntic, _user):
    order = Order()
    order.kuntic = _kuntic
    order.user = _user
    order.state = 'отправлено'
    order.save()


def get_orders_users(_user):
    return Order.objects.filter(user=_user)

def get_format_kuntic(_kuntic):
    return {'title':_kuntic.title, 'color':_kuntic.color.title, 'material':_kuntic.material, 'size':_kuntic.size.title, 'id':_kuntic.id}