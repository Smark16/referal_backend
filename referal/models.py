from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BackgroundInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    FullName = models.CharField(max_length=100)
    TelephoneNumber = models.PositiveBigIntegerField()
    Age = models.PositiveIntegerField()
    Gender = models.CharField(max_length=6)
    MaritalStatus = models.CharField(max_length=10)
    EmailAddress = models.EmailField(null=True, blank=True)
    Nationality = models.CharField(max_length=100)
    Ugandan_Identification_Number = models.CharField(max_length=100, null=True, blank=True)
    Refugee_Number = models.CharField(max_length=100, null=True, blank=True)
    settlement = models.CharField(max_length=255, blank=True, null=True)
    district_city = models.CharField(max_length=255, blank=True, null=True)
    subcounty_division = models.CharField(max_length=255, blank=True, null=True)
    parish_ward = models.CharField(max_length=255, blank=True, null=True)
    village_cell_zone = models.CharField(max_length=255, blank=True, null=True)

# Model to store business information
class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_of_bussiness = models.CharField(max_length=255)
    year_of_establishment = models.PositiveIntegerField()
    type_of_bussiness = models.CharField(max_length=255)
    Business_location = models.CharField(max_length=255)


class Modules(models.Model):
    module = models.CharField(max_length=255)

class Services(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason_for_additional_services = models.CharField(max_length=255)
    modules_interested_in = models.JSONField()
    confirmation = models.BooleanField(default=False)

    def __str__(self):
        return f"Request by {self.user.username} for {self.reason_for_additional_services}"