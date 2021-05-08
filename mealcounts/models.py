from django.db import models

# Create your models here.
class Tarikh(models.Model):
    din = models.CharField(max_length=3, null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.din)

class Member(models.Model):
    name = models.CharField(max_length=200,null=True)
    username = models.CharField(max_length=200,null=True)
    joma = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Meal(models.Model):
    tarikh = models.ForeignKey(Tarikh,null=True, on_delete=models.SET_NULL)
    member = models.ForeignKey(Member,null=True, on_delete=models.SET_NULL)
    poriman = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.member.name

class Khoroch(models.Model):
    tarikh = models.ForeignKey(Tarikh,null=True,on_delete=models.SET_NULL)
    poriman = models.IntegerField(null = True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.poriman) + " " + self.tarikh.din

# class Sheet(models.Model):
#     khoroch = models.IntegerField(null=True)
#     motMeal = models.IntegerField(null=True)
#     mealRate = models.FloatField(null=True)
#     date_created = models.DateTimeField(auto_now_add=True,null=True)