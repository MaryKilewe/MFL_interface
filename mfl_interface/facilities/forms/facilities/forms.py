from django import forms
from ...models import *


class Update_Partner(forms.Form):
    partner = forms.CharField(label='SDP', max_length=100)
    agency = forms.CharField(label='SDP Agency', max_length=100)


class Facility_Data_Form(forms.Form):

    mfl_code = forms.IntegerField(label='MFL Code', required=True)
    name = forms.CharField(label='Facility Name', max_length=100)
    county = forms.ChoiceField(label='County',
                                       choices=((i.id, i.name) for i in Counties.objects.all()))
    sub_county = forms.ChoiceField(label='Sub County',
                                       choices=((i.id, i.name) for i in Sub_counties.objects.all()))
    owner = forms.ChoiceField(label='Owner',
                                       choices=((i.id, i.name) for i in Owner.objects.all()))
    lat = forms.DecimalField(label='Latitude')
    lon = forms.DecimalField(label='Longitude')
    partner = forms.ChoiceField(label='SDP', required=False,
                                       choices=((i.id, i.name) for i in Partners.objects.all()))
    agency = forms.CharField(label='SDP Agency', max_length=100)
    CT = forms.BooleanField(label='CT', required=False)
    HTS = forms.BooleanField(label='HTS', required=False)
    KP = forms.BooleanField(label='KP', required=False)
    IL = forms.BooleanField(label='IL', required=False)
    # emr info
    emr_type = forms.ChoiceField(label='EMR',
                                       choices=((i.id, i.type) for i in EMR_type.objects.all()))
    emr_status = forms.ChoiceField(label='EMR Status',
                                       choices=(('Active','Active'),('Stalled/Inactive', 'Stalled/Inactive'),('Discontinued', 'Discontinued')))
    # hts info
    hts_use = forms.ChoiceField(label='HTS Use',
                                 choices=((i.id, i.hts_use_name) for i in HTS_use_type.objects.all()))
    hts_deployment = forms.ChoiceField(label='Deployment',
                                 choices=((i.id, i.deployment) for i in HTS_deployment_type.objects.all()))
    hts_status = forms.ChoiceField(label='HTS Status',
                                   choices=(('Active','Active'),('Stalled/Inactive', 'Stalled/Inactive'),('Discontinued', 'Discontinued')))
    # il info
    il_status = forms.ChoiceField(label='IL Status',
                                   choices=(('Active','Active'),('Stalled/Inactive', 'Stalled/Inactive'),('Discontinued', 'Discontinued')))
    registration_ie =forms.ChoiceField(label='Registration I.E',
                                   choices=(('Yes','Yes'),('No', 'No'),('N/A', 'N/A')), widget=forms.RadioSelect())
    pharmacy_ie = forms.ChoiceField(label='Pharmacy I.E',
                                   choices=(('Yes','Yes'),('No', 'No'),('N/A', 'N/A')), widget=forms.RadioSelect())
    # mhealth info
    ovc_offered = forms.ChoiceField(label='OVC',
                                        choices=(('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')), widget=forms.RadioSelect())
    otz_offered = forms.ChoiceField(label='OTZ',
                                    choices=(('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')), widget=forms.RadioSelect())
    prep_offered = forms.ChoiceField(label='PrEP',
                                        choices=(('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')), widget=forms.RadioSelect())
    tb_offered = forms.ChoiceField(label='TB',
                                    choices=(('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')), widget=forms.RadioSelect())
