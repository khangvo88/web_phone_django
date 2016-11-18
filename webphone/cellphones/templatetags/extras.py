from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
from django.contrib.staticfiles.storage import staticfiles_storage

from image_cropping.templatetags.cropping import cropped_thumbnail


from cellphones.models import Device


register = template.Library()


# @register.filter(name="cut", is_safe=True)
# def cut(value, arg):
#     pass

@register.filter(name="currency")
def currency(dollars,symbol="$"):
    dollars = round(float(dollars), 2)
    if symbol== u"đ":
        return "%s%s %s" % (intcomma(int(dollars)), ("%0.2f" % dollars)[-3:],symbol)
    return "%s%s%s" % (symbol, intcomma(int(dollars)), ("%0.2f" % dollars)[-3:])


@register.filter(name='removespace')
def removespace(value):
    return value.replace(' ','')

@register.filter
def get_range(value,step=1):
    return range(0,value,step)

@register.filter
def condition_str(value):
    """return the string of devide condition"""
    return Device.condition_status(value).title()

# @register.filter(takes_context=True)
# def device_image(context, object):
#     """return the string of devide condition"""
#     if not object.device_image:
#         return staticfiles_storage.url('cellphones/images/noimg.jpg')
#     return cropped_thumbnail(context, object,'image_ratio')

@register.simple_tag(takes_context=True)
def device_image(context, object):
    """return the string of devide condition"""
    if not object.device_image:
        return staticfiles_storage.url('cellphones/images/noimg.jpg')
    return cropped_thumbnail(context, object,'image_ratio')
