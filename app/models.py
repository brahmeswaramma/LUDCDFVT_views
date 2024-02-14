from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    Sname=models.CharField(max_length=100)
    principal=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
    

    def __str__(self):
        return self.Sname
    
class Student(models.Model):
    Stname=models.CharField(max_length=100)
    age=models.IntegerField()
    Sname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')
   