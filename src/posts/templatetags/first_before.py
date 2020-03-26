from django import template

register = template.Library()

def first_before(str_date, separator):
    return str_date.split(separator)[0]

register.filter('first_before', first_before)
