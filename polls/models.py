from django.db import models

class stu(models.Model):
    sName=models.CharField(max_length=20)
    sFee=models.IntegerField()
    sPhoto=models.ImageField()

    def __str__(self):
        return self.sName