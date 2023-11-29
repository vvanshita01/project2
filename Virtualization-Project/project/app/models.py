from django.db import models

# Create your models here.
class book(models.Model):
    name=models.CharField(max_length=25,blank=False,null=False)
    author=models.CharField(max_length=25,blank=False,null=False)
    isbn=models.IntegerField()
    
    
    def __str__(self) :
        return self.name