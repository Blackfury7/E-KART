from django.db import models
from customer . models import user_basics
from items . models import item
class order(models.Model):

 	item =models.ForeignKey(item,null=True,on_delete=models.SET_NULL)
 	user =models.ForeignKey(user_basics,null=True,on_delete=models.SET_NULL)
 	status = models.CharField(max_length = 20, default = "active")
 	address = models.CharField(max_length = 200)
 	contact = models.CharField(max_length = 200)
 	contact_verify = models.CharField(max_length = 200)
 	email = models.CharField(max_length = 200)
 	email_verify = models.CharField(max_length = 200)
 	bank = models.CharField(max_length = 200)
 	ifsc = models.CharField(max_length = 50)
 	transacton_id = models.CharField(max_length = 200)
 	date=models.DateTimeField(auto_now_add=True)
