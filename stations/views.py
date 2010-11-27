from django.shortcuts import render_to_response, get_object_or_404
from django.core import serializers
from django.http import HttpResponse
from api.models import Station


def index(request):
    station_list = Station.objects.all()
    return render_to_response('api/index.html', {'station_list' : station_list})

def details(request, station_id):
    station = [get_object_or_404(Station, pk=station_id)] #haetaan querysettiin
    #station = Station.objects.select_related().all()
    serializer = serializers.get_serializer("json")()
    response = HttpResponse()
    serializer.serialize(station, ensure_ascii=False, stream=response)
    return HttpResponse(response)

def all(request):
    stations = Station.objects.all()
    for s in stations:
        prices = s.prices.all()
        s.prices = prices
    
    serializer = serializers.get_serializer("json")()
    response = HttpResponse()
    serializer.serialize(stations, ensure_ascii=False, stream=response)
    return HttpResponse(response)