from django.db import models

# Create your models here.
class Category(models.Model):
    Cat_Id=models.PositiveIntegerField(primary_key=True)
    Cat_name=models.CharField(max_length=30,unique=True)
    Age_group=models.PositiveIntegerField(unique=True)
    Special_offers=models.TextField(unique=True)
    

    def __str__(self):
        return self.Cat_Id
class Myntra(models.Model):
    Cat_Id=models.ForeignKey(Category,on_delete=models.CASCADE)
    MId=models.PositiveIntegerField(primary_key=True)
    Pname=models.CharField(max_length=30,unique=True)
    Price=models.DecimalField(max_digits=6, decimal_places=2,unique=True)

    Discount=models.SmallIntegerField(unique=True)
    def __str__(self):
        return self.Cat_Id
    def __str__(self):
        return self.MId


class Flipcart(models.Model):
    Cat_Id=models.ForeignKey(Category,on_delete=models.CASCADE)
    FId=models.PositiveIntegerField(primary_key=True)
    Fname=models.CharField(max_length=30,unique=True)
    Price=models.DecimalField(max_digits=6, decimal_places=2,unique=True)
    Discount=models.SmallIntegerField(unique=True)

    def __str__(self):
        return self.Cat_Id
    def __str__(self):
        return self.FId

class Customer(models.Model):
    CId=models.PositiveIntegerField(unique=True)
    Cname=models.CharField(max_length=30,unique=True)
    Contact=models.PositiveIntegerField(unique=True)
    Address=models.TextField(unique=True)
    MId=models.ForeignKey(Myntra,on_delete=models.CASCADE)
    FId=models.ForeignKey(Flipcart,on_delete=models.CASCADE)
    





