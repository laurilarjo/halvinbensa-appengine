'''
Created on Oct 28, 2010

@author: larkki
'''
from polls.models import Poll, Choice
from django.contrib import admin

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic data',       {'fields': ['question']}),
        ('Date information', {'fields' : ['pub_date'], 'classes' : ['collapse']}),
        ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_today')
    list_filter = ['pub_date'] #ei toimi NonRelin kanssa
    search_fields = ['question'] #ei toimi NonRelin kanssa
    #date_hierarchy = 'pub_date' #ei edes rendaa tan kanssa

admin.site.register(Poll, PollAdmin)