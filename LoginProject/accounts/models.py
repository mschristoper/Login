from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255,null=True)
    email = models.CharField(max_length=255,null=True)
    password = models.CharField(max_length=255,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    address = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255,null=True)
    zipcode = models.CharField(max_length=255,null=True)

def __str__(self):
    return self.name

class SLP(models.Model):
    Status = (
        ('Win', 'Win'), 
        ('lose','lose'),
        ('Adventure','Adventure'),
        ('DailyQuest', 'DailyQuest')
    )

    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    name = models.CharField(max_length=255,null=True)
    slp = models.FloatField(null=True)
    Mode = models.CharField(max_length=255,null=True, choices=Status)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.Mode