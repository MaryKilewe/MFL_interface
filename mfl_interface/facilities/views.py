from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
import urllib.request, json
import requests
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
import mysql.connector
from .models import *
from .forms.facilities.forms import *

def index(request):
    #facilitydata = Facilities.objects.select_related('implementation').get(pk=1)
    facilitiesdata = Facilities.objects.prefetch_related('partner').select_related('implementation')\
                                                     .select_related('emr_type').select_related('emr_status')\
                                                     .select_related('hts_use_and_deployment').select_related('hts_status')\
                                                     .select_related('il_status').select_related('owner').all()

    print('get ready', facilitiesdata)

    return render(request, 'facilities/facilities_list.html', {'facilitiesdata': facilitiesdata})


def update_facility_data(request, facility_id):
    # does item exist in db
    facility = get_object_or_404(Facilities, pk=facility_id)

    facilitydata = Facilities.objects.prefetch_related('partner').select_related('implementation') \
        .select_related('emr_type').select_related('emr_status') \
        .select_related('hts_use_and_deployment').select_related('hts_status') \
        .select_related('il_status').select_related('owner').get(pk=facility_id)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Update_Facility_Data(request.POST)
        # check whether it's valid:

        if form.is_valid():
            # Save the new category to the database.
            Facilities.objects.update(mfl_code = form.cleaned_data['mfl_code'],
                name = form.cleaned_data['name'],
                county = form.cleaned_data['county'],
                sub_county = form.cleaned_data['sub_county'],
                owner = int(form.cleaned_data['owner']),
                partner = int(form.cleaned_data['partner']),
                #facilitydata.agency = facilitydata.partner.agency.name
                lat = form.cleaned_data['lat'],
                lon = form.cleaned_data['lon'],
                implementation = int(form.cleaned_data['implementation']),
                emr_type = int(form.cleaned_data['emr_type']),
                emr_status = int(form.cleaned_data['emr_status']),
                hts_use_and_deployment = int(form.cleaned_data['hts_use']),
                #facilitydata.deployment = facilitydata.hts_use_and_deployment.deployment)
                hts_status = int(form.cleaned_data['hts_status']),
                il_status = int(form.cleaned_data['il_status']),
            )

            #facility.save(force_update=True)

            # Redirect to home (/)
            return HttpResponseRedirect('/facilities')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)

        # if a GET (or any other method) we'll create a blank form
    else:
        initial_data = {  # 1st Method
            'mfl_code': facilitydata.mfl_code,
            'name': facilitydata.name,
            'county': facilitydata.county,
            'sub_county': facilitydata.sub_county,
            'owner': facilitydata.owner.name,
            'sdp': facilitydata.partner.name,
            'agency': facilitydata.partner.agency.name,
            'lat': facilitydata.lat,
            'lon': facilitydata.lon,
            'implementation': facilitydata.implementation.type,
            'emr_type': facilitydata.emr_type.type,
            'emr_status': facilitydata.emr_status.status,
            'hts_use': facilitydata.hts_use_and_deployment.hts_use_name,
            'deployment': facilitydata.hts_use_and_deployment.deployment,
            'hts_status': facilitydata.hts_status.status,
            'il_status': facilitydata.il_status.status,
        }
        form = Update_Facility_Data(initial=initial_data)

    return render(request, 'facilities/update_facility.html', {'facilitydata': facilitydata, 'form': form})

def partners(request):
    partners_data = Partners.objects.prefetch_related('agency').all()

    return render(request, 'facilities/partners_list.html', {'partners_data': partners_data})