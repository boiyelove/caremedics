from django import template

register = template.Library()

@register.simple_tag
def get_catc(category, cat):
	answer = category.filter(catalog=cat)
	return answer