from django.db import models
from railway.models import Train
from django.core.exceptions import ValidationError

# Create your models here.
class User(models.Model):
    Name=models.CharField(max_length=50, default="" , null= False)
    email=models.CharField(max_length=50, default="" , null= False)
    Phone_number=models.IntegerField(max_length=50, default="" , null= False)
    password=models.CharField(max_length=50, default="" , null= False)
    def __str__(self):
        return self.name

class Booked_Train(models.Model):
      user=models.ForeignKey(User, on_delete=models.CASCADE)
      train_name= models.ForeignKey(Train, on_delete=models.CASCADE)
      No_of_tickets=models.IntegerField(default=0)
      Ammount=models.IntegerField(default=0)
      def clean(self):
        if self.start_journey == self.departure_journey:
            raise ValidationError('Start journey and departure journey cannot be the same.')

      def __str__(self):
         return f"{self.user.username} - {self.train_name.train_name}"