from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Login(AbstractUser):
    is_trainer = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    is_physician = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)


class Trainer(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='trainer', null=True, blank=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.TextField()
    qualification = models.CharField(max_length=50)
    achievement = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pic')


class Physician(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='physician', null=True, blank=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.TextField()
    qualification = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pic')


class Equipments(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pic')
    description = models.TextField()


class Customer(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='customer', null=True, blank=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.TextField()
    contact_no = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.name


class Batch(models.Model):
    name = models.CharField(max_length=50)
    time = models.TimeField()


class Complaint(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    complaint = models.TextField()
    reply = models.TextField(null=True, blank=True)
    date = models.DateField()


class Dietplan(models.Model):
    subject = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pic')


class Attendence(models.Model):
    name = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='attendence')
    attendence = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()



class Health(models.Model):
    name = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='health')
    height = models.FloatField(max_length=50)
    weight = models.FloatField(max_length=50)
    healthcondition = models.TextField()
    medicineconsumption = models.TextField()


class Notification(models.Model):
    date = models.DateField()
    subject = models.CharField(max_length=50)
    description = models.TextField()


class Payment(models.Model):
    name=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='payment')
    amount=models.IntegerField()
    due_date=models.DateField()
    card_no=models.IntegerField(null=True,blank=True)
    card_name=models.CharField(max_length=50,null=True,blank=True)
    cvv=models.IntegerField(null=True,blank=True)