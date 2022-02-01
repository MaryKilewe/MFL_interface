from django.db import models

# Create your models here.


class IPdata(models.Model):
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)



class SDP_agencies(models.Model):
    name = models.CharField(max_length=100)

class Partners(models.Model):
    name = models.CharField(max_length=100)
    agency = models.ForeignKey(SDP_agencies, on_delete=models.CASCADE)

class Implementation(models.Model):
    type = models.CharField(max_length=100)

class EMR_type(models.Model):
    type = models.CharField(max_length=100)

class EMR_status(models.Model):
    status = models.CharField(max_length=100)

class HTS_use_and_deployment(models.Model):
    # combined use and deployment because data seems linked
    hts_use_name = models.CharField(max_length=100)
    deployment = models.CharField(max_length=100)

class HTS_status(models.Model):
    # if only two options are available (N/A or active), a Boolean field might be better
    status = models.CharField(max_length=100)

class IL_status(models.Model):
    # consider Boolean field
    status = models.CharField(max_length=100)

class Owner(models.Model):
    name = models.CharField(max_length=100)

class Facilities(models.Model):
    mfl_code = models.IntegerField()
    name = models.CharField(max_length=100)
    county = models.CharField(max_length=50)
    sub_county = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    hts_use_and_deployment = models.ForeignKey(HTS_use_and_deployment, on_delete=models.CASCADE)
    hts_status = models.ForeignKey(HTS_status, on_delete=models.CASCADE)
    il_status = models.ForeignKey(IL_status, on_delete=models.CASCADE)
    emr_type = models.ForeignKey(EMR_type, on_delete=models.CASCADE)
    emr_status = models.ForeignKey(EMR_status, on_delete=models.CASCADE)
    implementation = models.ForeignKey(Implementation, on_delete=models.CASCADE)
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE)
    #agency = models.ForeignKey(SDP_agencies, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)






