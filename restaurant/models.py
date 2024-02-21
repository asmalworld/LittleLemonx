from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    No_of_guests = models.SmallIntegerField(default=6)
    BookingDate = models.DateField()
    

    def __str__(self): 
         return f'{self.name} and {self.no_of_guests} guest(s)'
    
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField(default=5)

    def __str__(self): 
        return f'{self.title} : {self.price}'