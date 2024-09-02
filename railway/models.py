from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
class Station(models.Model):
      station_name = models.CharField(max_length=100 , null=False, default="")
      station_code= models.CharField(max_length=100 , null=False, default="")
      def __str__(self):
        return self.station_name

class Train(models.Model):
      Train_no= models.IntegerField(default=0,unique=True, null=False)
      Train_name= models.CharField(max_length=100,default="", null=False)
      start_journey = models.ForeignKey(Station, related_name='start_journeys', on_delete=models.CASCADE)
      end_journey = models.ForeignKey(Station, related_name='end_journeys', on_delete=models.CASCADE)
      start_time = models.DateTimeField(null=False, default=timezone.now)
      end_time = models.DateTimeField(null=False, default=timezone.now)
      price= models.IntegerField(default=0) 
      def clean(self):
        if self.start_journey == self.end_journey:
            raise ValidationError('Start journey and departure journey cannot be the same.')

      def __str__(self):
         return f"{self.Train_name} ({self.Train_no})"

class Availability(models.Model):
      Total_no_of_seats=models.IntegerField(default=0)
      train_no= models.ForeignKey(Train,related_name='end_journeys', on_delete=models.CASCADE, unique=True)
      def __str__(self):
        return self.train_no