from django.db import models

# Create your models here.
class Contacts(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)

    class Meta:
        db_table="contacts"

class Customer(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    city = models.CharField(max_length=100)
    class Meta:
        db_table="customer"

class Admin(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    class Meta:
        db_table="admin"

class Sell(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.BigIntegerField()
    technologies = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    datetime = models.DateField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)


    class Meta:
         db_table="sell"

class Buy(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sell = models.ForeignKey(Sell, on_delete=models.CASCADE)
    description = models.TextField()
    cost = models.BigIntegerField()



class AddFeedback(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Message = models.TextField()

    class Meta:
        db_table = "addfeedback"


class Comment(models.Model):
    sell = models.ForeignKey(Sell, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.BigIntegerField()

    class Meta:
        db_table = "comment"
