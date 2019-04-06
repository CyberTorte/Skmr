from django import template

register = template.Library()

@register.filter
def access_list(value, arg):
    args = []
    if ',' in arg:
        for string in arg.split(','):
            args.append(string)
    
    if args[1] == 'url':
        return value[int(args[0])].picture.url
    elif args[1] == 'title':
        return value[int(args[0])].title
    elif args[1] == 'created_at':
        return value[int(args[0])].diff_date()
    