from math import log

from django.template.defaultfilters import register


@register.filter(name='tournament_range')
def tournament_range(number_of_players):
    max_stage = log(number_of_players / 2, 2)
    return [pow(2, x) for x in range(int(max_stage), -1, -1)]
