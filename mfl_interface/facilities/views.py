from django.http import HttpResponse
import urllib.request, json
import requests
import json
from django.shortcuts import get_object_or_404, render

from .models import IPdata
from requests.auth import HTTPBasicAuth
from requests.structures import CaseInsensitiveDict
import environ

def index(request):
    #with urllib.request.urlopen("http://api.kmhfltest.health.go.ke/api/facilities/facilities/?format=json") as url:
    #    data = json.loads(url.read().decode())
    #    print(data)
    # create a password manager

    '''url = "http://api.kmhfltest.health.go.ke/api/facilities/facilities/?format=json"

    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer dGVzdEB0ZXN0bWFpbC5jb206IFRlc3RAMTIzNA=="

    resp = requests.get(url, headers=headers)

    print(resp.status_code)
    print('lets see', resp.content)'''

    response = requests.get('http://ip-api.com/json')
    data =json.loads(response.content)
    print(data['city'])

    #new = IPdata(city=data['city'], country=data['country'], lat=data['lat'], lon=data['lon'])
    #new.save()

    facilitydata = IPdata.objects.all()
    print('get ready', facilitydata)
    context = {'facilitydata': facilitydata}
    #return HttpResponse("Hello, world. You're at the facilities index.", context)
    return render(request, 'facilities/facilities_list.html', {'facilitydata': facilitydata})