from django.db import models

class Employee(models.Model):
    firstname=models.CharField(max_length=12)
    lastname=models.CharField(max_length=12)
    emp_id=models.IntegerField()

    def __str__(self):
        return self.firstname