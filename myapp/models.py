from django.db import models

# Create your models here.
class users(models.Model):
	uname=models.CharField(max_length=100)
	unum=models.CharField(max_length=800)
	ugmail=models.CharField(max_length=100)
	upass=models.CharField(max_length=100)
	uaddress=models.CharField(max_length=100)
	ucity=models.CharField(max_length=100,blank=True)
	uzip=models.CharField(max_length=100,blank=True)
	unum2=models.CharField(max_length=100,blank=True)
	ucart=models.CharField(max_length=100)
class product(models.Model):
	pname=models.CharField(max_length=100)
	pprice=models.CharField(max_length=800)
	pdes=models.CharField(max_length=1000)
	pq=models.CharField(max_length=100)
	pp1= models.ImageField(upload_to="gallery/",null=True)
	pp2= models.ImageField(upload_to="gallery/",null=True)
	pp3= models.ImageField(upload_to="gallery/",null=True)
	rate=models.CharField(max_length=200)
	cmt=models.CharField(max_length=500)
class order(models.Model):
	productid=models.CharField(max_length=100)
	productq=models.CharField(max_length=100)
	unum=models.CharField(max_length=100,null=True)
	uname=models.CharField(max_length=100,null=True)
	txnid=models.CharField(max_length=100,null=True)
	status=models.CharField(max_length=100,null=True)
	amount=models.CharField(max_length=100,null=True)
	userid=models.CharField(max_length=100,null=True)

class comment(models.Model):
	cunum=models.CharField(max_length=100)
	cuname=models.CharField(max_length=100,null=True)
	cpid=models.CharField(max_length=100)
	cmt=models.CharField(max_length=500)
class rating(models.Model):
	runum=models.CharField(max_length=100)
	rat=models.CharField(max_length=100)
	rpid=models.CharField(max_length=100)			
    