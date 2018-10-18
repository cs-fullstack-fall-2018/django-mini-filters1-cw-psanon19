from django import template
from datetime import date, timedelta

register = template.Library()

# THIS FILE WILL CONTAIN OUR CUSTOM FILTERS

# THIS FILTER CONVERTS THE DATE TO A HUMAN READABLE STRING
@register.filter(name='get_due_date_string')
def get_due_date_string(value):
    delta = value - date.today()

    if delta.days == 0:
        return "TODAY!"
    elif delta.days < 1:
        return "%s %s ago!" % (abs(delta.days), ("day" if abs(delta.days) == 1 else "days"))
    elif delta.days == 1:
        return "TOMORROW"
    elif delta.days > 1:
        return "In %s days" % delta.days


