from django.db import models

# Create your models here.
CHOICES =  [
    ("CE", "CE"),
    ("EXTC", "EXTC"),
    ("ME","ME"),
    ("AI","AI"),
    ("IT","IT")
]



class Student(models.Model):
    fname = models.CharField(max_length= 20)
    lname = models.CharField(max_length= 20)
    email = models.EmailField()
    phone = models.PositiveBigIntegerField()
    brand = models.CharField(max_length= 30,choices= CHOICES)


    def __str__(self):
        return self.fname
