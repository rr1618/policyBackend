from django.db import models
from .validators import validate_premium
# Create your models here.

#

class Customer(models.Model):
    customer_id = models.CharField(max_length=6, primary_key=True)
    customer_gender = models.CharField(max_length=1, null=False)
    customer_marital_status = models.BooleanField(null=False)
    customer_region = models.CharField(max_length=10,null=False)
    customer_income_group = models.CharField(max_length=15 ,null=False)

    def __str__(self):
        return self.customer_id


class Vehicle(models.Model):
    vehicle_segment_id = models.IntegerField(auto_created=True,primary_key=True)
    vehicle_segment = models.CharField(max_length=1)
    fuel = models.CharField(max_length=15,null=False)

    def __str__(self):
        return self.vehicle_segment



class Policy(models.Model):
    policy_id = models.CharField(max_length=10, primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_of_purchase = models.DateField()
    vehicle_segment_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    bil = models.BooleanField(null=False)
    premium = models.IntegerField(validators=[validate_premium], null=False, default=0)
    pip = models.BooleanField(null=False)
    pdl = models.BooleanField(null=False)
    collision = models.BooleanField(null=False)
    comprehensive = models.BooleanField(null=False)

    def __str__(self):
        return self.policy_id






