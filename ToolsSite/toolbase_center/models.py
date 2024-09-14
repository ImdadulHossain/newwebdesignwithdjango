from django.db import models


# Create your models here.
# admin user name = titil
# admin password = imdad1234

class Item(models.Model):

    def __str__(self):
        return self.item_name
    item_name = models.CharField(max_length=200)
    item_dis = models.CharField(max_length=200)
    item_price = models.IntegerField()
