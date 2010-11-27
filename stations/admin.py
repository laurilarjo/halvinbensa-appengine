from stations.models import Station, Price, Company
from django.contrib import admin

    
class StationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic stuff',       {'fields': ['title', 'city', 'address', 'company']}),
        ('Location', {'fields' : ['latitude', 'longitude']}),
    ]
    #list_display = ('question', 'pub_date', 'was_published_today')
    #list_filter = ['pub_date'] #ei toimi NonRelin kanssa
    #search_fields = ['question'] #ei toimi NonRelin kanssa
    #date_hierarchy = 'pub_date' #ei edes rendaa tan kanssa

class PriceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic', { 'fields' : ['station', 'type', 'updated', 'price']}
         )
    ]
    
admin.site.register(Station, StationAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Company)