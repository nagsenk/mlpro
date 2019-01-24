from django.db import models


class User(models.Model):
	name = models.CharField(max_length=128)
	password = models.IntegerField()
	email = models.EmailField(max_length=128)
	choice = models.CharField(max_length=128)
class educators(models.Model):
	name = models.CharField(max_length=128)
	email = models.EmailField(max_length=128)
	educourse = models.CharField(max_length=128)
class file(models.Model):
        name=models.CharField(max_length=128)
        educourse = models.CharField(max_length=128)
        filename=models.CharField(max_length=128)

        

        
		
		
		

   
   
   
