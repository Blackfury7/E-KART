from django.db import models




class item(models.Model):

	name = models.CharField(max_length = 200)
	category= models.CharField(max_length = 100)
	photo = models.CharField(max_length = 500)
	quantity = models.IntegerField()
	price = models.IntegerField()
	discount = models.IntegerField()
	dis_price = models.IntegerField()
	status = models.CharField(max_length = 20, default = 'active')
	about = models.CharField(max_length = 200)
	
