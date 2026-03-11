from django.db import models

class Zepto(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    mrp = models.IntegerField()
    quantity = models.IntegerField()
    discount_percent = models.FloatField()
    available_quantity = models.IntegerField()
    discounted_selling_price= models.FloatField()
    weight_in_gms = models.IntegerField()
    out_of_stack = models.BooleanField()
    quantity = models.IntegerField()
