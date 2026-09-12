from django.db import models

class Tags(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Expenses(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    amount = models.IntegerField()

