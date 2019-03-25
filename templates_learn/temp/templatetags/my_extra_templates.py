from django import template

register= template.Library()

@register.filter(name='cut')  # decoraters
def cut(value,args):
    """
    cut specific string
    """
    return value.replace(args,'')


# register.filter('myCut',cut)
