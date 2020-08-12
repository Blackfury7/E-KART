from django.db import models
from items . models import item
from customer . models import user_basics
class cart_item(models.Model):

 	item =models.ForeignKey(item,null=True,on_delete=models.SET_NULL)
 	user =models.ForeignKey(user_basics,null=True,on_delete=models.SET_NULL)
 	status = models.CharField(max_length = 20, default = "active")


