from django import template

register = template.Library()

@register.filter
def join_args(var, arg):
    return "%s,%s" % (var, arg)
