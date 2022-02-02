from django import forms
from ...models import *


class Update_Partner(forms.Form):
    partner = forms.CharField(label='SDP', max_length=100)
    agency = forms.CharField(label='SDP Agency', max_length=100)


class Update_Facility_Data(forms.Form):

    mfl_code = forms.IntegerField(label='MFL Code', required=True)
    name = forms.CharField(label='Facility Name', max_length=100)
    county = forms.CharField(label='County', max_length=100)
    sub_county = forms.CharField(label='Sub-County', max_length=100)
    owner = forms.ChoiceField(label='Owner',
                                       choices=((i.id, i.name) for i in Owner.objects.all()))
    lat = forms.DecimalField(label='Latitude')
    lon = forms.DecimalField(label='Longitude')
    partner = forms.ChoiceField(label='SDP',
                                       choices=((i.id, i.name) for i in Partners.objects.all()))
    agency = forms.CharField(label='SDP Agency', max_length=100)
    implementation = forms.ChoiceField(label='Implementation',
                                            choices=((i.id, i.type) for i in Implementation.objects.all()))
    emr_type = forms.ChoiceField(label='EMR',
                                       choices=((i.id, i.type) for i in EMR_type.objects.all()))
    emr_status = forms.ChoiceField(label='EMR Status',
                                       choices=((i.id, i.status) for i in EMR_status.objects.all()))
    hts_use = forms.ChoiceField(label='HTS Use',
                                 choices=((i.id, i.hts_use_name) for i in HTS_use_and_deployment.objects.all()))
    deployment = forms.CharField(label='Deployment', max_length=100)
    hts_status = forms.ChoiceField(label='HTS Status',
                                   choices=((i.id, i.status) for i in HTS_status.objects.all()))
    il_status = forms.ChoiceField(label='IL Status',
                                   choices=((i.id, i.status) for i in IL_status.objects.all()))
