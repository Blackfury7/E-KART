from django.db import models
class user_basics(models.Model):

	name = models.CharField(max_length = 200)
	username = models.CharField(max_length = 200)
	address = models.CharField(max_length = 200)
	email = models.CharField(max_length = 200)
	password = models.CharField(max_length = 200, default = "1234")
	status = models.CharField(max_length = 20, default = 'active')
	contact = models.CharField(max_length = 20, default =" ")





