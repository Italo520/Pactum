from django import template

register = template.Library()

@register.filter
def get_alert_class(tags):
    tags = tags.lower()
    if 'error' in tags or 'danger' in tags:
        return 'bg-red-100 text-red-700'
    elif 'success' in tags:
        return 'bg-green-100 text-green-700'
    elif 'warning' in tags:
        return 'bg-yellow-100 text-yellow-700'
    else:
        return 'bg-blue-100 text-blue-700'