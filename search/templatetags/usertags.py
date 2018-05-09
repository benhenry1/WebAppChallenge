from django import template
from search.models import Job

register = template.Library()

class UserTags():

	def get_context_data(self, **kwargs):
		context = super(UserTags, self).get_context_data(**kwargs)
		context['tags'] = Tag.objects.all()
		return context
