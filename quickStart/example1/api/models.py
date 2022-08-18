from django.db import models

# Create your models here.
class Task(models.Model):
    titel=models.CharField(max_length=200)
    complate:models.BooleanField(default=False,blank=True,null=True)

    def __str__(self):
     return self.titel