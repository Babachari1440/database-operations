# creating django environment
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','project16.settings')

# setting up the features of django

import django
django.setup()
# importing models
from app.models import *
from faker import Faker
f=Faker()
import random
categories=['fashion','mobiles','appliances','furniture']

def Add_categories():
    c=Category.objects.get_or_create(Cat_Id=random.choice(categories) ,Cat_name=Cat_name,Age_group=Age_group,Special_offers=Special_offers)[0]
    c.save()
    return c



def Add_myntra(Cat_name,Age_group,Special_offers):
    Cat_Id=Add_categories()
    m=Myntra.objects.get_or_create(MId=MId,Pname=Pname,Price=Price,Discount=Discount)[0]
    m.save()
    return m
def Add_flipcart(FId,Fname,Price,Discount):
    Cat_Id=Add_categories()
    MId=Add_myntra()
    f=Flipcart.objects.get_or_create(FId=FId,Fname=Fname,Price=price,Discount=Discount)[0]
    f.save()
    return f
def Add_customer(Cat_name,Age_group,Special_offers):
    Cat_Id=Add_categories()
    FId=Add_flipcart()
    cu=Customer.objects.get_or_create(CId=CId,Cname=Cname,Contact=Contact,Address=Address)[0]
    cu.save()
    return cu


n=int(input('enter number of rows to be inserted'))

def Add_data(n):
    for i in range(n):
        
        fakename=f.first_name()
        fakeage=f.Age_group()
        fakeoffers=f.Special_offers()
       
      

        Add_customer(first_name, Age_group, Special_offers)

if __name__=='__main__':
    print('population hass started')
    Add_data(n)
    print('population has ended')
