from django.db import models

class Driver(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    score = models.IntegerField()

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
