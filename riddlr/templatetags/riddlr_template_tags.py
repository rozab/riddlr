from django import template
from riddlr.models import Riddle

register = template.Library()

# TODO wtf is this
@register.inclusion_tag('riddlr/riddles.html')
def get_top_riddles():
    return {'riddles': Riddle.objects.all().order_by('-rating')}