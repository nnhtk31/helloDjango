from django.contrib import admin
from polls.models import Poll
from polls.models import Choice
from polls.models import Blog
from polls.models import Author
from polls.models import Entry
# Register your models here.

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3
	
class PollAdmin(admin.ModelAdmin):
  fieldsets = [
      (None,               {'fields': ['question']}),
      ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
  ]
  inlines = [ChoiceInline]
  list_display = ('question', 'pub_date', 'was_published_recently')
  list_filter = ['pub_date']
  search_fields = ['question']
  
admin.site.register(Poll,PollAdmin)
admin.site.register(Choice)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
