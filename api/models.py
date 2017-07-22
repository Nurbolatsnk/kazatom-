from django.db import models

# Create your models here.
class Table(models.Model):
    chink=models.TextField()
    full_name=models.TextField(max_length=255)
    flowmeter_id=models.TextField(max_length=255)
    meter=models.IntegerField()
    counter=models.IntegerField()
    def __unicode__(self):
        return self.chink
