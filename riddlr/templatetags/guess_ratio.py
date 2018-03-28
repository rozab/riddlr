from django import template

register = template.Library()

@register.simple_tag
def guess_ratio(percentage):
    if percentage is None:
        return "N/A"
    else:
        return str(int(round(percentage)))+"%"