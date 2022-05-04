from unicodedata import category
from django.db import models, router
from django.utils import timezone
from django.db.models import Sum

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Inactive')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    departure_point = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Inactive')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.departure_point

class Bus(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE, blank= True, null = True)
    bus_number = models.CharField(max_length=250)
    route = models.CharField(max_length=100)
    seats = models.FloatField(max_length=5, default=0)
    cost_per_seat = models.IntegerField()
    depart = models.DateTimeField(auto_now=False)
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Inactive')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bus_number

    @classmethod
    def add_bus(self):
        self.save()

    @classmethod
    def update_bus(cls, id):
        cls.objects.filter(id=id).update()
    
    @classmethod
    def delete_bus(cls, id):
        cls.objects.filter(id=id).delete()
    

class Schedule(models.Model):
    code = models.CharField(max_length=100)
    bus = models.ForeignKey(Bus,on_delete=models.CASCADE)
    depart = models.ForeignKey(Location,on_delete=models.CASCADE, related_name='depart')
    arrival = models.ForeignKey(Location,on_delete=models.CASCADE, related_name='arrival')
    route =  models.CharField(max_length=100)
    schedule= models.DateTimeField()
    fare= models.FloatField()
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Cancelled')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.code + ' - ' + self.bus.bus_number)




