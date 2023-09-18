from django.db import models

# Create your models here.


class EmployDetails(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"
