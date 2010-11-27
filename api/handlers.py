from piston.handler import BaseHandler
from piston.utils import rc, require_extended

from stations.models import Station

class StationHandler(BaseHandler):

    allowed_methods = ('GET')
    model = Station
    #anonymous = AnonymousStationHandler
    fields = ('title', 'city', 'address',
              'latitude', 'longitude',
              ('company', ('name',)),
              ('prices', ('type','updated', 'price',),),)
    #fields = ('title', 'content', ('author', ('username',)), 
    #          'created_on', 'content_length')
    
    def read(self, request, id=None):
        """
        Returns a blogpost, if `title` is given,
        otherwise all the posts.
        
        Parameters:
         - `title`: The title of the post to retrieve.
        """
        base = Station.objects
        
        if id:
            return base.get(id=id)
        else:
            return base.all()
    
    def content_length(self, station):
        return len(station.content)
        
    @require_extended
    def create(self, request):
        """
        Creates a new blogpost.
        """
        attrs = self.flatten_dict(request.POST)

        if self.exists(**attrs):
            return rc.DUPLICATE_ENTRY
        else:
            station = Station(title=attrs['title'], 
                            address=attrs['address'])
            station.save()
            
            return station
    
    @classmethod
    def resource_uri(self):
        return ('stations', [ 'id', ])