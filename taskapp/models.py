from django.db import models

# Create your models here.
class Destination(models.Model):
	text1 = models.TextField()
	text2 = models.TextField()
	text3 = models.TextField()
	text4 = models.IntegerField()
	text5 = models.TextField()
	text6 = models.TextField()
	num1 = models.IntegerField()
	text7 = models.TextField()
	date1 = models.DateField()
	num2 = models.FloatField()

