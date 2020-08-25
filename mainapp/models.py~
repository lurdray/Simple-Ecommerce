from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=15, default="")
	image = models.ImageField(upload_to="images/")
	descrp = models.TextField()
	pub_date = models.DateTimeField("date published")
	
	def __str__(self):
		return self.name
		
		
class Order(models.Model):
	product_id = models.CharField(max_length=15, default="") #, on_delete=models.CASCADE)
	quantity = models.CharField(max_length=15, default="")
	name_owner = models.CharField(max_length=35, default="")
	phone_owner = models.CharField(max_length=15, default="")
	email_owner = models.EmailField()
	comment = models.TextField()
	pub_date = models.DateTimeField("date published")
	
	def __str__(self):
		return self.name_owner
		
		

